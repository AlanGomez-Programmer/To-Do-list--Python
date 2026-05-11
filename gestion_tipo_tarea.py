import funcionalidades

def tipo_tarea():
    funcionalidades.limpiar_pantalla()
    print("="*50)
    print("          REGISTRO DE TIPO DE TAREA")
    while True:    
        Nombre_tipo = input(" \n  Nombre de tipo de tarea: ").strip().capitalize()

        tipos = funcionalidades.leer_archivo(funcionalidades.archivos["tipo_tarea"])

        existe = any(Nombre_tipo == tipo for tipo in tipos.values())

        if existe:
            print("  Error: Ese nombre ya existe")
            continue
        else:
            funcionalidades.crear(funcionalidades.archivos["tipo_tarea"], Nombre_tipo)
            print("  Tipo de tarea agregada exitosamente")
            print("="*50)    
            input("Presione ENTER para salir...")        
            return
            