import funcionalidades

def listar_tipos():
    tipos_tareas = funcionalidades.leer_archivo(funcionalidades.archivos["tipo_tarea"])

    for id, tipo in tipos_tareas.items():
        print(f"  {id}. {tipo}")

def validar_id():
    while True:
        tipos = funcionalidades.leer_archivo(funcionalidades.archivos["tipo_tarea"])
        print("="*50)
        print("          REGISTRO DE TIPO DE TAREA")

        if tipos == {}:
            print("Aún no hay tipos de tareas registradas")
            print("Realiza tu primer registro de tipo de tarea")
        else:
            print("  Tipos de tareas ya registrados:")
            listar_tipos()

        while True:
            id_existentes = [int(id_e) for id_e in tipos]

            try:
                id = int(input("\n  ID: ").strip())

                if id < 0:
                    print("  Error: Ingrese otro nuemero de Id mayor a 0 ")
                    continue
                elif id > len(tipos)+1:
                    print("  Error: El Id debe tener la misma secuencia")
                    continue
                elif id in id_existentes:
                    print("  Eror: ese id ya existe")
                    continue
                else:
                    return id
            except ValueError:
                print("  Error: Solo se perminten números")
                continue

def tipo_tarea():
    funcionalidades.limpiar_pantalla()
    tipos = funcionalidades.leer_archivo(funcionalidades.archivos["tipo_tarea"])

    id = validar_id()

    while True:
        Nombre_tipo = input(" \n  Nombre de tipo de tarea: ").strip().capitalize()
        
        existe = any(Nombre_tipo == tipo for tipo in tipos.values())

        if existe:
            print("  Error: Ese nombre ya existe")
            continue
        else:
            tipos[id] = Nombre_tipo
            funcionalidades._guardar_datos(funcionalidades.archivos["tipo_tarea"], tipos)
            print("  Tipo de tarea agregada exitosamente")
            print("="*50)    
            input("Presione ENTER para salir...")        
            return
           