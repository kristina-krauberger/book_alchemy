from flask_sqlalchemy import SQLAlchemy #kein Column

db = SQLAlchemy()  # instanziierung des objekts ORM system für Kommunikation mit Datenbank, damit kann ich die Objekte erstellen

class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.STRING(50))
    birth_date = db.Column(db.DATE)
    date_of_death = db.Column(db.DATE)


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    isbn = db.Column(db.STRING(17)) #mit strichen
    title = db.Column(db.STRING(32)) #binäre schwellenwerte
    publication_year = db.Column(db.INTEGER)




