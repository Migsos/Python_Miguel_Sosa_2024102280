clientes_existentes = {"4133266"}

def buscar_cliente(ci):
    if ci in clientes_existentes:
        return {
            "accion": "Success",
            "codRes": "SIN_ERROR",
            "menRes": "OK",
            "ci": ci
        }
    else:
        return {
            "accion": "Cliente no está en el sistema",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": ci
        }
