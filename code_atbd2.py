# -*- coding: utf-8 -*-
"""Code atbd2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-IwWTGAl9eEoNU1ZsHaQsyakvL7H94SE
"""

import random
import csv
from datetime import datetime, timedelta

# Configuración general
equipos = ['A', 'B', 'C', 'D']
jugadoras_por_equipo = 6
paises = ["Europa", "America", "Africa", "Asia"]
partidos = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "C"), ("B", "D"), ("C", "D")]
duracion_partido = 60  # minutos
fecha_inicial = datetime.strptime("2024-11-10 20:00:00", "%Y-%m-%d %H:%M:%S")

# Generar jugadoras
def generar_jugadoras():
    jugadoras = []
    for equipo in equipos:
        for i in range(1, jugadoras_por_equipo + 1):
            pais = random.choice(paises)
            jugadoras.append({
                "jugadora_id": f"{equipo}_{i}",
                "team": equipo,
                "country": pais
            })
    return jugadoras

# Generar datos de partidos
def generar_datos_partidos(jugadoras):
    datos = []
    partido_id = 1
    for equipo1, equipo2 in partidos:
        fecha_partido = fecha_inicial + timedelta(days=(partido_id - 1))
        hora_actual = fecha_partido
        for minuto in range(duracion_partido):
            for jugadora in jugadoras:
                if jugadora["team"] in [equipo1, equipo2]:
                    frecuencia = random.randint(60, 180)
                    datos.append({
                        "result": "",
                        "table": 0,
                        "time": (hora_actual + timedelta(minutes=minuto)).strftime("%Y-%m-%dT%H:%M:%SZ"),
                        "measurement": "frecuencia_cardiaca",
                        "partido_id": partido_id,
                        "jugadora_id": jugadora["jugadora_id"],
                        "team": jugadora["team"],
                        "country": jugadora["country"],
                        "field": "frecuencia",
                        "value": frecuencia
                    })
        partido_id += 1
    return datos

# Guardar en formato correcto
def guardar_csv(datos, archivo):
    with open(archivo, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Encabezados de anotación
        writer.writerow(["#group", "false", "false", "false", "false", "false", "false", "false", "false", "false"])
        writer.writerow(["#datatype", "string", "long", "dateTime:RFC3339", "string", "long", "string", "string", "string", "long"])
        writer.writerow(["#default", "", "", "", "", "", "", "", "", ""])
        # Encabezados de las columnas
        writer.writerow(["", "result", "table", "_time", "_measurement", "partido_id", "jugadora_id", "team", "country", "_field", "_value"])
        # Escribir datos
        for dato in datos:
            writer.writerow([
                "", dato["result"], dato["table"], dato["time"], dato["measurement"], dato["partido_id"],
                dato["jugadora_id"], dato["team"], dato["country"], dato["field"], dato["value"]
            ])

# Generar dataset
jugadoras = generar_jugadoras()
datos_partidos = generar_datos_partidos(jugadoras)

# Guardar en archivo
archivo_salida = "frecuencias.csv"
guardar_csv(datos_partidos, archivo_salida)

print(f"Archivo generado: {archivo_salida}")

df = pd.read_csv('frecuencias.csv', skiprows=3)

jugadoras_agrupadas = df.groupby(['jugadora_id', 'country'])

for (jugadora_id, country), group in jugadoras_agrupadas:
         print(f"Jugadora: {jugadora_id}, País: {country}")

import csv
from datetime import datetime, timedelta
import random

# Configuración general
equipos_actuales = {
    "A": "Manchester United",
    "B": "Atletic Bilbao",
    "C": "Colo-Colo",
    "D": "Iberia"
}
equipos_anteriores = ["Real Sociedad", "Huachipato", "Palestino", "Milan"]
nombres = ["Sofia", "Isabella", "Camila", "Valentina", "Mariana", "Lucia", "Emma", "Martina"]
apellidos = ["Gonzalez", "Rodriguez", "Lopez", "Martinez", "Garcia", "Hernandez", "Perez", "Torres"]
fecha_inicial = datetime.strptime("2020-01-01", "%Y-%m-%d")
dias_variacion = 365 * 5  # Hasta 5 años de variación

# Información de países para cada jugadora
jugadoras_paises = {
    "A_1": "Africa", "A_2": "Europa", "A_3": "Asia", "A_4": "America", "A_5": "Africa", "A_6": "Africa",
    "B_1": "Africa", "B_2": "Europa", "B_3": "America", "B_4": "America", "B_5": "Europa", "B_6": "America",
    "C_1": "Africa", "C_2": "Asia", "C_3": "Asia", "C_4": "Asia", "C_5": "Europa", "C_6": "America",
    "D_1": "Asia", "D_2": "Europa", "D_3": "Europa", "D_4": "Africa", "D_5": "Asia", "D_6": "Asia"
}

# Generar datos de jugadoras
def generar_datos_jugadoras():
    datos = []
    for letra_equipo, equipo_actual in equipos_actuales.items():
        for i in range(1, 7):  # 6 jugadoras por equipo
            jugadora_id = f"{letra_equipo}_{i}"  # Cambiar el formato del ID a A_1, B_2, etc.
            equipo_anterior = random.choice(equipos_anteriores)
            pais = jugadoras_paises[jugadora_id]
            nombre = f"{random.choice(nombres)} {random.choice(apellidos)}"
            fecha_ingreso = fecha_inicial + timedelta(days=random.randint(0, dias_variacion))
            frecuencia_promedio = random.randint(60, 180)  # Generar una frecuencia promedio
            datos.append({
                "result": "",
                "table": 0,  # Siempre mantener el valor como 0
                "time": fecha_ingreso.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "measurement": "jugadoras_info",
                "jugadora_id": jugadora_id,
                "nombre": nombre,
                "country": pais,
                "equipo_actual": equipo_actual,
                "equipo_anterior": equipo_anterior,
                "_field": "frecuencia_promedio",
                "_value": frecuencia_promedio
            })
    return datos

# Guardar datos en CSV con el formato adecuado
def guardar_csv(datos, archivo):
    with open(archivo, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Encabezados de anotación
        writer.writerow(["#group", "false", "false", "false", "false", "false", "false", "false", "false", "false", "false"])
        writer.writerow(["#datatype", "string", "long", "dateTime:RFC3339", "string", "string", "string", "string", "string", "string", "long"])
        writer.writerow(["#default", "", "", "", "", "", "", "", "", "", ""])
        # Encabezados de las columnas
        writer.writerow(["", "result", "table", "_time", "_measurement", "jugadora_id", "nombre", "country", "equipo_actual", "equipo_anterior", "_field", "_value"])
        for dato in datos:
            writer.writerow([
                "", dato["result"], dato["table"], dato["time"], dato["measurement"],
                dato["jugadora_id"], dato["nombre"], dato["country"], dato["equipo_actual"],
                dato["equipo_anterior"], dato["_field"], dato["_value"]
            ])

# Archivo de salida
archivo_salida = "jugadoras_datos.csv"

# Ejecutar
datos_jugadoras = generar_datos_jugadoras()
guardar_csv(datos_jugadoras, archivo_salida)

print(f"Archivo generado: {archivo_salida}")