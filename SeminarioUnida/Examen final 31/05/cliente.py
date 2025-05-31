from flask import Blueprint, request, jsonify
cliente=Blueprint('cliente', __name__)

@cliente.route('/cliente',methods=['POST'])
def verificar_cliente():
    ci = request.json.get('ci')
    codRes, menRes,accion=verificar_existencia_cliente(ci)

    salida = {
        'accion':accion,
        'codRes':codRes,
        'menRes':menRes,
        'ci': ci
    }
    return jsonify(salida)
def verificar_existencia_cliente(ci):
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    accion = 'Success'
    clientes_validos = ['4133266']
    try:
        print("Verificando cliente...")
        if str(ci) in clientes_validos:
            print("Cliente encontrado")
            accion = "Success"
        else:
            print("Cliente no encontrado")
            accion="Cliente no está en el sistema"
            codRes='ERROR'
            menRes='Error cliente'
    except Exception as e:
        print("ERROR", str(e))
        codRes='ERROR'
        menRes='Msg: ' + str(e)
        accion="Error interno"
    return codRes, menRes, accion
