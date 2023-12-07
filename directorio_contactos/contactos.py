import re
import json

def elegir_cuenta_contable(cuentas_contables):
    print("Seleccione una cuenta contable:")
    for cuenta in cuentas_contables:
        print(f"Código: {cuenta['codigo']}, {cuenta['nombre_cuenta']}")

    codigo_ingresado = input("Ingrese el código de la cuenta: ").strip()
    for cuenta in cuentas_contables:
        if cuenta['codigo'] == codigo_ingresado and cuenta['tipo_cuenta'] == 'gasto':
            return codigo_ingresado

    print("Selección inválida o la cuenta no es del tipo 'gasto'. Intente de nuevo.")
    return None

def cargar_cuentas_contables():
    try:
        with open('cuentas_contables.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def cargar_contactos():
    try:
        with open('contactos.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def guardar_contactos(contactos):
    with open('contactos.json', 'w') as file:
        json.dump(contactos, file, indent=4)


def agregar_contacto(contactos, contacto):

    if any(v.strip() == '' for v in contacto.values()):
        print("Todos los campos son obligatorios.")
        return False

    if any(c['numero_identificacion'] == contacto['numero_identificacion'] for c in contactos):
        print("Ya existe un cliente o proveedor con este número de identificación.")
        return False

    contactos.append(contacto)
    guardar_contactos(contactos)
    return True


def listar_contactos(contactos):
    for contacto in contactos:
        print(contacto)

def actualizar_contacto(contactos, identificacion, contacto_actualizado):
    for i, contacto in enumerate(contactos):
        if contacto['numero_identificacion'] == identificacion:
            contactos[i] = contacto_actualizado
            guardar_contactos(contactos)
            return True
    return False


def eliminar_contacto(contactos, identificacion):

    print("Contactos antes de eliminar:", contactos)

    contactos[:] = [c for c in contactos if c['numero_identificacion'] != identificacion]

    print("Contactos después de eliminar:", contactos)

    guardar_contactos(contactos)


def validar_correo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo)
