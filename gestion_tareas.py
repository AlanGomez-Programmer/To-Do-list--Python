import funcionalidades

estado = ["Pendiente", "En Proceso", "Finalizado"]

def agregar_tarea():

    funcionalidades.limpiar_pantalla()
    print("="*50)
    print("          REGISTRO DE TAREA\n")

    nombre = input("  Nombre Tarea: ").strip().capitalize()
    descripcion = input("  Descripción: ").strip().capitalize()

    tipos_tareas = funcionalidades.leer_archivo(funcionalidades.archivos["tipo_tarea"])

    if len(tipos_tareas) == 0:
        print("Error: Aún no has registrado algun tipo de tarea")
        input("Presione ENTER para regresar... ")
        return

    i = 1
    for id, tipo in tipos_tareas.items():
        print(f"{1. }")

    while True: 
        fecha_inicio = input("  Fecha Inicio (DD-MM-AA): ").strip()
        validar_f_i = funcionalidades.validar_fecha(fecha_inicio)

        if validar_f_i:
            break
        else:
            print("\n  Error: Debe ingresar bien la fecha")
            continue 

    while True: 
        fecha_entrega = input("  Fecha Entrega (DD-MM-AA): ").strip()
        validar_f_e = funcionalidades.validar_fecha(fecha_entrega)

        if validar_f_e:
            break
        else:
            print("\n  Error: Debe ingresar bien la fecha")
            continue 

    contador = 0
    for i in estado:
        print(f"{i}. {estado[contador]}")
    
    while True:
        try:
            estado_tarea = int(input("Seleccione un estado: ").strip())

            if estado_tarea < len(estado) or estado_tarea > len(estado):
                print("Error: No existe esa opción elegida")
            else:
                estado_elegido = contador[estado_tarea-1]
        except ValueError:
            print("Error: Solo se permiten números")
            continue

    tarea = {
        "nombre": nombre,
        "descripción": descripcion,
        "tipo": tipo
    }

    funcionalidades.crear(funcionalidades.archivos["tareas"], )

agregar_tarea()