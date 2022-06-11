from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask.templating import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
import requests
import json
import unicodedata
import urllib.request

app = Flask(__name__, template_folder='templates')
api = Api(app)

# Format: mysql://[username]:[password]@[host]:[port]/[database]'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/score'

db = SQLAlchemy(app)

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

@api.resource('/hasil', '/hasil/<int:siswa_id>')
class Hasil_Resource(Resource):
    @marshal_with(hasil_fields)
    def get(self, siswa_id=None):
        if not siswa_id:
            return Hasil.query[:25]

        result = Hasil.query.filter_by(id_siswa=siswa_id).first()

        if not result:
            abort(404, message=f"hasil dengan ID {siswa_id} tidak ditemukan")
        
        return result
       
@app.route('/nilai/')
def all_nilai():
    # detail = Hasil_Resource()
    url = f"http://localhost:5000/hasil"
    response = urllib.request.urlopen(url)
    data = response.read()
    res = json.loads(data)
    
    # page = request.args.get('page', 0, type=int)
    return render_template('index.html', info=res)

@app.route('/nilai/<int:id>')
def nilai(id=None):
    url = f"http://localhost:5000/hasil/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    res = json.loads(data)
    
    # page = request.args.get('info', 0, type=int)
    return render_template('nilai.html', siswa=res)

if __name__ == "__main__":
    app.run(port=5000, debug=True)



