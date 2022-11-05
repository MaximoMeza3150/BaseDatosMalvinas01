from flask import Flask,render_template,Blueprint
from flask_sqlalchemy import SQLAlchemy
from routes.equipos import equipos
from routes.emisiones import emisiones

app = Flask(__name__)
app.register_blueprint(equipos)
app.register_blueprint(emisiones)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/equipos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SQLAlchemy(app)

