import funcionalidades
from gestion_tareas import agregar_tarea
from gestion_tipo_tarea import tipo_tarea

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
                funcionalidades.limpiar_pantalla()
                agregar_tarea()
            elif opci == 2:
                funcionalidades.limpiar_pantalla()
            elif opci == 3: 
                funcionalidades.limpiar_pantalla()
            elif opci == 4:
                funcionalidades.limpiar_pantalla()
                tipo_tarea()
            elif opci == 5:
                funcionalidades.limpiar_pantalla()
            else:
                print("Error: Esa opción no existe")
                continue
        except ValueError:
            print("Error: Solo se permiten números")

menu_pricipal()