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
@app.route('/registro', methods=['POST'])
def addUser():
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    email = request.form['email']
    password = request.form['password']
    confirma = request.form['confirma']


    if nombre and apellidos and email and password and confirma:
        cursor = db.database.cursor()
        sql = "INSERT INTO usuarios (nombre, apellidos, email, password, confirma) VALUES (%s, %s, %s, %s, %s)"
        data = (nombre, apellidos, email, password, confirma)
        cursor.execute(sql, data)
        db.database.commit()
    return render_template('login.html')


# Ruta para el formulario de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Verificar las credenciales en la base de datos
        cursor = db.database.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            # Si las credenciales son correctas, redirige a la página principal
            return render_template('registro.html')
        else:
            # Si las credenciales son incorrectas, puedes renderizar nuevamente el formulario de inicio de sesión con un mensaje de error
            return render_template('login.html', error="Credenciales incorrectas. Inténtalo de nuevo.")
    else:
        # Si la solicitud es GET, muestra el formulario de inicio de sesión
        return render_template('login.html')




"""@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM clientes WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    email = request.form['email']
    coche = request.form['coche']
    matricula = request.form['matricula']

    if nombre and apellidos and email and coche and matricula:
        cursor = db.database.cursor()
        sql = "UPDATE clientes SET nombre = %s, apellidos = %s, email = %s, coche = %s, matricula = %s WHERE id = %s"
        data = (nombre, apellidos, email, coche, matricula, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))"""


if __name__ == '__main__':
    app.run(debug=True, port=4000)