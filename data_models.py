"""Data models for authors and books using SQLAlchemy."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Author(db.Model):
    """Represents an author with personal details."""

    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    birth_date = db.Column(db.Date)
    date_of_death = db.Column(db.Date)
    books = db.relationship("Book", back_populates="author")


class Book(db.Model):
    """Represents a book with bibliographic information."""

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(17), nullable=False, unique=True)
    title = db.Column(db.String(32))
    publication_year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
    author = db.relationship("Author", back_populates="books")