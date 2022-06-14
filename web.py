from flask import Flask, flash, send_from_directory, session
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask.templating import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
import requests
import json
import unicodedata
import urllib.request

from sqlalchemy import text

app = Flask(__name__, template_folder='templates')
app.secret_key = 'secret'
api = Api(app)

# Format: mysql://[username]:[password]@[host]:[port]/[database]'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/score'

db = SQLAlchemy(app)
#cursor = db.cursor()

class Hasil(db.Model):
    __tablename__ = "hasil"

    id_siswa = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    nrp = db.Column(db.String(100), nullable=False)
    fisika = db.Column(db.String(100), nullable=False)
    kimia = db.Column(db.String(100), nullable=False)
    matematika = db.Column(db.String(100), nullable=False)
    biologi = db.Column(db.String(100), nullable=False)
    agama = db.Column(db.String(100), nullable=False)
    indonesia = db.Column(db.String(100), nullable=False)
    inggris = db.Column(db.String(100), nullable=False)

hasil_fields = {
    'id_siswa': fields.Integer,
    'nama': fields.String,
    'nrp': fields.String,
    'fisika': fields.String,
    'kimia': fields.String,
    'matematika': fields.String,
    'biologi': fields.String,
    'agama': fields.String,
    'indonesia': fields.String,
    'inggris': fields.String,
}


@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        nama = request.form.get('nama')
        # sql = text(f'Select * from hasil where nama = `{nama}`')
        results = db.engine.execute("SELECT * from hasil WHERE nama LIKE %s", (nama))
        # results = db.engine.execute(sql)
        return render_template("nilai.html", info = results)
    
    else:
        result = Hasil.query[:25]
        return render_template("index.html", info = result)

@app.route('/download', methods=['GET'])
def download():
    return send_from_directory(directory='file', path='kota.csv', as_attachment=True)

if __name__ == "__main__":
    
    app.run(port=5000, debug=True)