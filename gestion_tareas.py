import funcionalidades
from tabulate import tabulate

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

    id_tipos_tareas = [int(id_tipo) for id_tipo in tipos_tareas]

    for id, tipo in tipos_tareas.items():
        print(f"  {id}. {tipo}")

    while True:
        try:
            opci_tipo = int(input("  Tipo de tarea seleccionado:  ").strip())

            if not opci_tipo in id_tipos_tareas:
                print("Error: La opción elegida no existe")
                continue
            else:
                tipo_tarea_elegida = tipos_tareas[str(opci_tipo)]
                break
        except ValueError:
            print("Error: Solo se aceptan números")
            continue

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

    contador = 1
    for i in estado:
        print(f"{contador}. {i}")
        contador += 1
    
    while True:
        try:
            estado_tarea = int(input("Seleccione un estado: ").strip())

            if estado_tarea < 0 or estado_tarea > len(estado)+1:
                print("Error: No existe esa opción elegida")
            else:
                estado_elegido = estado[estado_tarea-1]
                tarea = {
                    "nombre": nombre,
                    "descripción": descripcion,
                    "tipo": tipo_tarea_elegida,
                    "fecha inicio": fecha_inicio,
                    "fecha entrega": fecha_entrega,
                    "estado": estado_elegido
                    }
                break
        except ValueError:
            print("Error: Solo se permiten números")

    funcionalidades.crear(funcionalidades.archivos["tareas"],tarea)

def listar_tareas():
    funcionalidades.limpiar_pantalla()
    print("="*110)
    print("LISTADO DE TAREAS\n".center(100))
    tareas_registradas = funcionalidades.leer_archivo(funcionalidades.archivos["tareas"])

    if len(tareas_registradas) == 0:
        print("Error: No hay tareas registradas aún")
        input("Ingrese ENTER para salir..")
        return
    else:
        tareas = [[i,dato["nombre"], dato["descripción"], dato["tipo"], dato["fecha inicio"], dato["fecha entrega"], dato["estado"]] for i,(id,dato) in enumerate(tareas_registradas.items(), start=1)]
        print(tabulate(tareas, headers=['#','NOMBRE','DESCRIPCIÓN','TIPO','FECHA INICIO','FECHA ENTREGA', 'ESTADO']))
        print("="*110)

def cambiar_estado_tarea():

    tareas = funcionalidades.leer_archivo(funcionalidades.archivos["tareas"])
    listar_tareas()
    print("Cambio de Estado".center(100))

    id_tareas = [[i, id] for i,(id) in enumerate(tareas, start=1)]

    while True:  
        try:
            id_elegido = int(input("Ingrese el número de la tarea elegida: ").strip())
        
            id_elegido_corregido = id_elegido -1

            if id_elegido > len(tareas) or id_elegido < 0:
                print("Error: No existe ese número de tarea")
            else:
                id_tarea_elegida = id_tareas[id_elegido_corregido][1]
            break
        except ValueError:
            print("Error: Solo se permiten números")
            continue

    contador = 1
    estados = [[contador + i, estado[i]] for i in range(len(estado))]

    print(tabulate(estados, headers=["#", "ESTADO"]))
            
    while True:
        try:
            estado_tarea = int(input("Seleccione un estado: ").strip())

            if estado_tarea < 0 or estado_tarea > len(estado)+1:
                print("Error: No existe esa opción elegida")
                continue
            else:
                estado_elegido = estado[estado_tarea-1]
                for id in tareas:
                    if id_tarea_elegida == id:
                        tareas[id]["estado"] = estado_elegido
                        funcionalidades._guardar_datos(funcionalidades.archivos["tareas"], tareas)
                        print("Cambio de estado exitoso")
                        return
        except ValueError:
                    print("Error: Solo se permiten números")
