from flask import Flask, request, jsonify
from cliente import buscar_cliente

app = Flask(__name__)

@app.route('/cliente', methods=['POST'])
def consultar_cliente():
    data = request.get_json()

    if not data or 'ci' not in data:
        return jsonify({
            "accion": "Datos de entrada inválidos",
            "codRes": "ERROR",
            "menRes": "Falta campo 'ci'",
            "ci": data.get("ci", None)
        }), 400

    ci = str(data['ci'])
    respuesta = buscar_cliente(ci)
    return jsonify(respuesta), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003)
