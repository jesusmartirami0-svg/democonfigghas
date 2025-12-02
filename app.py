from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/buscar")
def buscar_usuario():
    # SOURCE: El dato viene de una petición web (request.args)
    username = request.args.get('username')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # SINK: Vulnerabilidad de Inyección SQL
    # CodeQL ve que 'username' llega sucio a la base de datos
    cursor.execute("SELECT * FROM users WHERE username = '" + username + "'")

    return "Búsqueda completada"
