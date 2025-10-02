from flask import Flask
from data_models import db, Author, Book
import os

app = Flask(__name__) # 1. create the app

basedir = os.path.abspath(os.path.dirname(__file__)) # 2. absoluter pfad
#3. flask mitteilen wo die datenbankdatei ist, absoluter pfad string!
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"

db.init_app(app) # 4. initialize the app with the extension







if __name__ == '__main__':
  with app.app_context(): # Google "How to run SQLight flask app" - wichtig, damit db.create_all() funktioniert
    db.create_all()        # erzeugt Tabellen, falls noch nicht vorhanden

  app.run(host="0.0.0.0", port=5001, debug=True) # Google "How to run flask app" - Startet server

