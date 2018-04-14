from flask import Flask, jsonify


app = Flask('todoapp')

@app.route('/task')
def listar():
    return jsonify()