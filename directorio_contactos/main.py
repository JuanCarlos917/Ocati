
import contactos
import cuentas_contables

def main():
    lista_contactos = contactos.cargar_contactos()

    while True:
        print("\nDirectorio de Contactos")
        print("1. Agregar contacto")
        print("2. Ver contactos")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        eleccion = input("Seleccione una opción: ")

        if eleccion == "1":
            cuentas = cuentas_contables.cargar_cuentas_contables()
            codigo_cuenta = input("Seleccione una cuenta contable: ").strip()

            if cuentas_contables.validar_cuenta(cuentas, codigo_cuenta):
                nuevo_contacto = {
                    "nombre": input("Nombre: ").strip(),
                    "apellido": input("Apellido: ").strip(),
                    "tipo_doc": input("Tipo de Documento: ").strip(),
                    "numero_identificacion": input("Número de Identificación: ").strip(),
                    "fecha_nacimiento": input("Fecha de Nacimiento: ").strip(),
                    "correo_personal": input("Correo Personal: ").strip(),
                    "numero_celular": input("Número de Celular: ").strip(),
                    "numero_fijo": input("Número Fijo: ").strip(),
                    "tipo_contacto": input("Tipo de Contacto (Cliente/Proveedor): ").strip(),
                    "cuenta_contable": codigo_cuenta,
                    "valor_descuento": input("Valor Descuento: ").strip()
                }

                if not contactos.validar_correo(nuevo_contacto['correo_personal']):
                    print("Correo inválido. Intente de nuevo.")
                    continue

                if contactos.agregar_contacto(lista_contactos, nuevo_contacto):
                    print("Contacto agregado con éxito.")
                else:
                    print("Error al agregar el contacto. Intente de nuevo.")
            else:
                print("Código de cuenta contable inválido. Intente de nuevo.")

        elif eleccion == "2":
            contactos.listar_contactos(lista_contactos)

        elif eleccion == "3":
            identificacion = input("Ingrese el número de identificación del contacto a actualizar: ")
            contacto_actualizado = {
                "nombre": input("Nuevo Nombre: "),
                "apellido": input("Nuevo Apellido: "),
                "tipo_doc": input("Nuevo Tipo de Documento: "),
                "numero_identificacion": identificacion,
                "fecha_nacimiento": input("Nueva Fecha de Nacimiento: "),
                "correo_personal": input("Nuevo Correo Personal: "),
                "numero_celular": input("Nuevo Número de Celular: "),
                "numero_fijo": input("Nuevo Número Fijo: "),
                "tipo_contacto": input("Nuevo Tipo de Contacto (Cliente/Proveedor): "),
                "cuenta_contable": input("Nueva Cuenta Contable: "),
                "valor_descuento": input("Nuevo Valor Descuento: ")
            }

            if not contactos.validar_correo(contacto_actualizado['correo_personal']):
                print("Correo inválido. Intente de nuevo.")
                continue

            if contactos.actualizar_contacto(lista_contactos, identificacion, contacto_actualizado):
                print("Contacto actualizado con éxito.")
            else:
                print("Contacto no encontrado.")

        elif eleccion == "4":
            identificacion = input("Ingrese el número de identificación del contacto a eliminar: ").strip()
            contactos.eliminar_contacto(lista_contactos, identificacion)
            print("Contacto eliminado con éxito.")

            lista_contactos = contactos.cargar_contactos()


        elif eleccion == "5":
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == '__main__':
    main()
