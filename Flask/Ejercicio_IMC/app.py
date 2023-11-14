from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_imc(altura, peso):
    altura = float(altura)
    peso = float(peso)
    imc = peso / (altura ** 2)
    return imc


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
    try:
        if request.method == 'POST':
            altura = request.form['altura']
            peso = request.form['peso']
            imc = round(calcular_imc(altura, peso),2)
            clasificacion = clasificar_imc(imc)
            return render_template('resultado.html', imc=imc, clasificacion=clasificacion)
        return render_template('index.html')
    except ValueError:
        return render_template('index.html', texto = "Introduce solo numeros")
    except ZeroDivisionError:
        return render_template('index.html', div0 = "No se puede dividir entre cero, introduce dos nuevos valores")
        

app.run()