import requests

def obtener_distancia_y_duracion(ciudad_origen, ciudad_destino):
    url_base = "https://www.mapquestapi.com/directions/v2/route"
    token = "8Dvx9dwZQ07oJ3jCsA77F1wd57gumSwb"

    parametros = {
        "key": token,
        "from": ciudad_origen,
        "to": ciudad_destino,
        "unit": "k",
        "narrativeType": "none"
    }

    respuesta = requests.get(url_base, params=parametros)
    datos = respuesta.json()

    distancia = datos["route"]["distance"]
    duracion_segundos = datos["route"]["time"]

    return distancia, duracion_segundos

def calcular_combustible(distancia):
    rendimiento_litros_km = 0.12
    combustible_requerido = distancia * rendimiento_litros_km
    return combustible_requerido

def convertir_segundos_a_horas_minutos_segundos(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60
    return horas, minutos, segundos

def imprimir_narrativa_viaje(ciudad_origen, ciudad_destino, distancia, duracion_horas, duracion_minutos, duracion_segundos, combustible_requerido):
    print("Narrativa del Viaje:")
    print(f"Origen: {ciudad_origen}")
    print(f"Destino: {ciudad_destino}")
    print(f"Distancia: {distancia:.2f} km")
    print(f"Duración: {duracion_horas} horas, {duracion_minutos} minutos, {duracion_segundos} segundos")
    print(f"Combustible requerido: {combustible_requerido:.2f} litros")

# Solicitar ciudades de origen y destino al usuario
ciudad_origen = input("Ciudad de Origen: ")
ciudad_destino = input("Ciudad de Destino: ")

# Obtener distancia y duración del viaje
distancia, duracion_segundos = obtener_distancia_y_duracion(ciudad_origen, ciudad_destino)

# Calcular combustible requerido
combustible_requerido = calcular_combustible(distancia)

# Convertir duración a horas, minutos y segundos
duracion_horas, duracion_minutos, duracion_segundos = convertir_segundos_a_horas_minutos_segundos(duracion_segundos)

# Imprimir narrativa del viaje
imprimir_narrativa_viaje(ciudad_origen, ciudad_destino, distancia, duracion_horas, duracion_minutos, duracion_segundos, combustible_requerido)

