from datetime import datetime
from pathlib import Path
import json
import uuid
import os


ruta_base = Path("./data")

ruta_base.mkdir(parents = True, exist_ok = True)

archivos = {
    "tareas": ruta_base/'tareas.json',
    "tipo_tarea": ruta_base/'tipo_tarea.json'
}

def limpiar_pantalla():
    if os.name == 'nt':
        print("cls")
    else: 
        print("clean")

def _cargar_datos(ruta_archivo):
    """Lee y retorna los datos del archivo JSON"""

    if not os.path.exists(ruta_archivo): 
        return {}
    
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return {}


def _guardar_datos(ruta_archivo, datos):
    """Guarda todos los datos en el archivo JSON"""
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def crear(archivo, registro):
    """Añade un nuevo registro usando un UUID aleatorio como llave principal"""

    datos = _cargar_datos(archivo)

    nuevo_id = str(uuid.uuid4())

    datos[nuevo_id] = registro

    _guardar_datos(archivo, datos)

    return nuevo_id

def leer_archivo(ruta_archivo):
    """Devuelve el diccionario completo con todos los registros"""
    return _cargar_datos(ruta_archivo)

def mostrar_id(ruta_archivo):

    ruta = Path(ruta_archivo)

    with ruta.open('r', encoding='utf-8') as archivo:
        datos = json.load(archivo)

    id_obtenido = [id for id in datos]

    return id_obtenido

def validar_fecha(fecha_texto):
    """Sirve para validar si una fecha tiene el formato DD-MM-YY y es una fecha real"""

    try:
        datetime.strptime(fecha_texto, '%d-%m-%Y')
        return True
    except ValueError:
        return False
    
def validar_hora(hora_texto):
    """Sirve para validar la hora, tiene el formato h:m y su formato es 24 hrs"""

    try:
        datetime.strptime(hora_texto, '%H:%M')
        return True
    except:
        return False