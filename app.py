"""Flask app for managing a library of authors and books."""

from flask import Flask, render_template, request, flash, redirect, url_for
from data_models import db, Author, Book
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("KEY_FLASH")


basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"
)

db.init_app(app)


@app.route("/", methods=["GET"])
def home():
    """Show all books, optionally sorted or searched."""
    sort = request.args.get("sort")
    search = request.args.get("search")

    query = Book.query

    if search:
        query = query.filter(Book.title.ilike(f"%{search}%"))

    if search and search.strip():
        query = query.order_by(Book.title)
    elif sort == "author":
        query = query.join(Author).order_by(Author.name)

    books = query.all()

    if not books:
        flash("No books were found.", "no_results_error")

    return render_template("home.html", books=books)


@app.route("/add_author", methods=["GET", "POST"])
def add_author():
    """Add a new author to the library."""
    if request.method == "POST":
        try:
            name = request.form["name"].strip()
            birth_date_str = request.form["birth_date"]
            death_date_str = request.form["date_of_death"]

            if not name or not birth_date_str:
                raise ValueError("Name and birth date are required.")

            birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y").date()
            date_of_death = (
                datetime.strptime(death_date_str, "%d.%m.%Y").date()
                if death_date_str else None
            )

            new_author = Author(
                name=name,
                birth_date=birth_date,
                date_of_death=date_of_death
            )

            db.session.add(new_author)
            db.session.commit()

            flash(
                "YAY! The author has been successfully added to your library.",
                "add_success"
            )
            return redirect(url_for("add_author"))

        except ValueError:
            flash(
                "Oops! Please make sure name and birth date are filled correctly "
                "and the dates are in DD.MM.YYYY format.",
                "form_error"
            )
            return redirect(url_for("add_author"))

    return render_template("add_author.html")


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    """Add a new book to the library."""
    if request.method == "POST":
        try:
            isbn = request.form["isbn"].replace("-", "").strip()
            title = request.form["title"].strip()
            publication_year = request.form["publication_year"].strip()
            author_id = int(request.form["author_id"])

            if not isbn or not title or not publication_year:
                raise ValueError("All fields must be filled.")

            new_book = Book(
                isbn=isbn,
                title=title,
                publication_year=publication_year,
                author_id=author_id
            )

            db.session.add(new_book)
            db.session.commit()

            flash(
                "YAY! The book has been successfully added to your library.",
                "add_success"
            )
            return redirect(url_for("add_book"))

        except Exception:
            flash(
                "Oops! Please make sure all fields are filled correctly.",
                "form_error"
            )
            return redirect(url_for("add_book"))

    authors = Author.query.all()
    return render_template("add_book.html", authors=authors)


@app.route("/book/<int:book_id>/delete", methods=["POST"])
def delete_book(book_id):
    """Delete a book and its author if no other books remain."""
    try:
        book = Book.query.get(book_id)
        if not book:
            flash("Book not found.", "form_error")
            return redirect(url_for("home"))

        author = book.author

        db.session.delete(book)
        db.session.commit()

        if author and len(author.books) == 0:
            db.session.delete(author)
            db.session.commit()

        flash("Book was successfully deleted", "success_delete")

    except Exception:
        flash("An error occurred while trying to delete the book.", "form_error")

    return redirect(url_for("home"))


@app.errorhandler(404)
def page_not_found(e):
    """Handles 404 errors by rendering a custom error page."""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    """Handles 500 errors by rendering a custom error page."""
    return render_template('500.html'), 500


if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
        except Exception:
            print("Could not initialize the database.")

        app.run(host="0.0.0.0", port=5006, debug=True)
