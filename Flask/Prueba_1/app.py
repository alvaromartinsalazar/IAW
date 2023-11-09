from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hola():
    usuario=""
    contrasena=""
    if (request.method == "POST"):
        usuario = request.form.get("usuario")
        contrasena = request.form.get("contrasena")
        print(usuario, contrasena)
    return render_template("index.html")

@app.route("/eustaquio")
def eustaquio():
    return "Hola, esta es la web de eustaquio"

@app.route("/pruebapost", methods=["POST", "GET"])
def pruebapost():
    if (request.method == "POST"):
        return "Esto es un POST"
    elif (request.method == "GET"):
        return "Esto es un GET"
    return "Hola, esta es la web de eustaquio"

app.run()
