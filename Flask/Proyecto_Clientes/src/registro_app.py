from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)

#Rutas de la aplicación
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM usuarios")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('registro.html', data=insertObject)

#Ruta para guardar usuarios en la bdd
@app.route('/user', methods=['POST'])
def addUser():
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    email = request.form['email']
    coche = request.form['password']
    matricula = request.form['confirm']


    if nombre and apellidos and email and password and confirm:
        cursor = db.database.cursor()
        sql = "INSERT INTO usuarios (nombre, apellidos, email, password, confirm) VALUES (%s, %s, %s, %s, %s)"
        data = (nombre, apellidos, email, password, confirm)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))