from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def imc():
    peso=""
    altura=""
    c_imc=""
    if (request.method == "POST"):
        peso = float(request.form.get("peso"))
        altura = float(request.form.get("altura"))
    return render_template("index.html", c_imc=peso/altura*altura, peso=peso, altura=altura)

app.run()