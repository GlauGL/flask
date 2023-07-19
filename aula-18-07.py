
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.app_context().push()
    
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = "Usuario"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(84),nullable=False)
    email = db.Column(db.String(84),nullable=False, unique=True, index=True)
    senha = db.Column(db.String(255),nullable=False)

# db.create_all()
@app.route("/")
def index():
    usuarios = Usuario.query.all()
    return render_template("index.html", usuarios=usuarios)

@app.route("/cadastro",methods=['GET','POST'])
def cadastro():
    if request.method == "POST":
       nome = request.form['login']
       email = request.form['email'] 
       senha =request.form['senha']
       usuario = Usuario()
       usuario.nome = nome
       usuario.email = email
       usuario.senha = senha
       db.session.add(usuario)
       db.session.commit()

    return render_template('cadastro.html')

if __name__== "__main__":
    app.run(debug=True)
