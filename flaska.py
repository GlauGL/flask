from flask import Flask, render_template, request
from calcula_raiz import calcula_raiz
app = Flask(__name__)

@app.route("/", methods=["GET","POST" ])
def main():
    if request.method == "POST":
        numero = int(request.form.get("campo_numero"))
        calcula_raiz(numero)
    return render_template("index.html")

if __name__ =="__main__":
    app.run()
