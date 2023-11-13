from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_imc(altura, peso):
    try:
        altura = float(altura)
        peso = float(peso)
        imc = peso / (altura ** 2)
        return imc
    except ValueError:
        return None

def clasificar_imc(imc):
    if imc is None:
        return "Error en la entrada"
    elif imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc <= 24.9:
        return "Normal"
    elif 25.0 <= imc <= 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        altura = request.form['altura']
        peso = request.form['peso']
        imc = calcular_imc(altura, peso)
        clasificacion = clasificar_imc(imc)
        return render_template('resultado.html', imc=imc, clasificacion=clasificacion)
    return render_template('index.html')

app.run()