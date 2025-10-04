"""Data models for authors and books using SQLAlchemy."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Author(db.Model):
    """Represents an author with personal details."""

    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    birth_date = db.Column(db.Date)
    date_of_death = db.Column(db.Date)


class Book(db.Model):
    """Represents a book with bibliographic information."""

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(17))
    title = db.Column(db.String(32))
    publication_year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
    author = db.relationship("Author", backref="books")