import json

def cargar_cuentas_contables():
    try:
        with open("cuentas_contables.json", "r") as archivo_cuentas_contables:
            cuentas_contables = json.load(archivo_cuentas_contables)
    except FileNotFoundError:
        cuentas_contables = []
    return cuentas_contables

def elegir_cuenta_contable():
    cuentas_contables = cargar_cuentas_contables()
    print("Cuentas Contables")
    for cuenta_contable in cuentas_contables:
        print(f"{cuenta_contable['codigo']}. {cuenta_contable['nombre']}")
    while True:
        codigo_cuenta_contable = input("Seleccione una cuenta contable: ")
        for cuenta_contable in cuentas_contables:
            if cuenta_contable["codigo"] == codigo_cuenta_contable:
                return cuenta_contable
        print("Código de cuenta contable inválido. Intente de nuevo.")

def validar_cuenta(cuentas_contables, codigo):
    for cuenta in cuentas_contables:
        if cuenta['codigo'] == codigo:
            return True
    return False

def agregar_cuenta_contable(cuentas_contables, nueva_cuenta_contable):
    cuentas_contables.append(nueva_cuenta_contable)
    try:
        with open("cuentas_contables.json", "w") as archivo_cuentas_contables:
            json.dump(cuentas_contables, archivo_cuentas_contables, indent=4)
        return True
    except:
        return False

def listar_cuentas_contables(cuentas_contables):
    print("Cuentas Contables")
    for cuenta_contable in cuentas_contables:
        print(f"{cuenta_contable['codigo']}. {cuenta_contable['nombre']}")
