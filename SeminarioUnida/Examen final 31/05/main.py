from flask import Flask
from cliente import cliente
app=Flask(__name__)

app.register_blueprint(cliente)

@app.route('/',methods=['GET'])
def hello():
    return 'DerlisCaballeroMendoza_2010100521'

if __name__=="__main__":
    app.run(host='127.0.0.1',port=5003,debug=True)
