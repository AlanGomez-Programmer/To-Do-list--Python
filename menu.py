import funcionalidades
from gestion_tareas import agregar_tarea, listar_tareas, cambiar_estado_tarea
from gestion_tipo_tarea import agregar_tipo_tarea, listar_tipos

def menu_pricipal():
    while True: 
        funcionalidades.limpiar_pantalla()
        print("="*50)
        print("                      MENU\n")
        print("  1. Agregar Nueva Tarea")
        print("  2. Ver tareas")
        print("  3. Cambiar Estado de Tarea")
        print("  4. Regristrar Tipo de Tarea")
        print("  5. Ver Tipo de Tarea Registada\n")
        print("="*50)
        try:
            opci = int(input("Ingrese opción elegida: ").strip())

            if opci == 1:
                agregar_tarea()
            elif opci == 2:
                listar_tareas()
            elif opci == 3: 
                cambiar_estado_tarea()
            elif opci == 4:
                agregar_tipo_tarea()
            elif opci == 5:
                listar_tipos()
            else:
                print("Error: Esa opción no existe")
                continue
        except ValueError:
            print("Error: Solo se permiten números")
