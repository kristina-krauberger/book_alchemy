from flask_sqlalchemy import SQLAlchemy #kein Column

db = SQLAlchemy()  # instanziierung des objekts ORM system für Kommunikation mit Datenbank, damit kann ich die Objekte erstellen

class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    birth_date = db.Column(db.Date)
    date_of_death = db.Column(db.Date)


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(17)) #mit strichen
    title = db.Column(db.String(32)) #binäre schwellenwerte
    publication_year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id")) # FOREIGNKEY neue Spalte die die ID des autor abspeichern
    author = db.relationship("Author", backref="books")



