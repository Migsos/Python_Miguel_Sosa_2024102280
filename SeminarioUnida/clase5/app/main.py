from flask import Flask
from login import login

app = Flask(__name__)

# Registrar el blueprint de login
app.register_blueprint(login)

@app.route('/', methods=['GET'])
def hello():
    return 'Hola Unida'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
