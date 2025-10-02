from flask import Flask, render_template, request, flash, redirect, url_for
from data_models import db, Author, Book
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__) # 1. create the app
app.secret_key = os.getenv("KEY_FLASH")


basedir = os.path.abspath(os.path.dirname(__file__)) # 2. absoluter pfad
#3. flask mitteilen wo die datenbankdatei ist, absoluter pfad string!
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"

db.init_app(app) # 4. initialize the app with the extension


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/add_author", methods=["GET", "POST"])
def add_author():

    if request.method == "POST":    # bei GET & POST requests, immer mit "if POST" anfangen, dann "else GET"
        name = request.form["name"]   # Ich habe eine HTML Form, welche Daten erwartet meine authors tabelle?
        birth_date_str = request.form["birth_date"]
        death_date_str = request.form["date_of_death"]

        # Wandelt "11.06.1986" in ein datetime.date Objekt um
        birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y").date()
        date_of_death = datetime.strptime(death_date_str, "%d.%m.%Y").date()

        # neuen Author instanziiert
        new_author = Author(
          name=name,
          birth_date=birth_date,
          date_of_death=date_of_death
        )

        db.session.add(new_author)  # 1. Zur Session hinzufügen
        db.session.commit()  # 2. Dauerhaft speichern

        flash("YAY! The author has been successfully added to your library.", "add_success")
        return redirect(url_for("add_author"))

    else:
        return render_template("add_author.html")


@app.route("/add_book", methods=["GET", "POST"])
def add_book():

    if request.method == "POST":
        isbn = request.form["isbn"]
        title = request.form["title"]
        publication_year = request.form["publication_year"]
        author_id =int(request.form["author_id"])

        new_book = Book(
            isbn=isbn,
            title=title,
            publication_year=publication_year,
            author_id=author_id
        )

        db.session.add(new_book)
        db.session.commit()

        flash("YAY! The book has been successfully added to your library.", "add_success")
        return redirect(url_for("add_book"))

    else:
        # Damit stehen dir im HTML alle Author-Objekte zur Verfügung
        authors = Author.query.all()
        return render_template("add_book.html", authors=authors)


if __name__ == '__main__':
  with app.app_context(): # Google "How to run SQLight flask app" - wichtig, damit db.create_all() funktioniert
    db.create_all()        # erzeugt Tabellen, falls noch nicht vorhanden

  app.run(host="0.0.0.0", port=5005, debug=True) # Google "How to run flask app" - Startet server

