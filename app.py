import os
from flask import Flask, jsonify, request

app = Flask(__name__)

def fibonacci():
    resp = '0, 1, '
    i = 2
    max = 50

    proximo = 1
    anterior = 0
    numero = 0

    while i < max:
        local = proximo
        numero = anterior + proximo
        resp = resp + str(numero) + ", "
        proximo = numero
        anterior = local
        i += 1

    return resp

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
