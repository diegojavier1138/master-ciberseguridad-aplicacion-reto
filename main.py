import urllib.parse
import requests
import os

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "ykuqqndSwpFXtEmSrL6nzuB71luq02Ar"
while True:
    orig = input("Origen ")
    if orig == "s":
        break
    dest = input("Destino: ")
    if orig == "s":
        break
    cls = lambda: os.system('cls')
    cls ()
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + url)

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("Estatus de la API: " + str(json_status) + "= Se encontró la ruta. \n")
        print("Instrucciones de: " + (orig) + " a: " + (dest))
        print("Duración aproximada: " + str(json_data["route"]["formattedTime"]))
        # Distancia se provee en millas por 1.61
        print("Kilómetros aprox: " + str("{:2f}".format((json_data["route"]["distance"]) * 1.61)))
        # Combustible se provee en Galones por 3.78 litros
        print("Litros aprox: " + str("{:2f}".format((json_data["route"]["fuelUsed"]))))
        print("------INICIO DE INSTRUCCIONES DE LA RUTA------")
        contador = 1
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print("Paso No. " + str(contador) + ": " + (each["narrative"]))
                  #+ "(" + str("{:2f".format((each["distance"])*1.61 + "Kms. ")))
            contador = contador + 1
            print("------FIN DE INSTRUCCIONES DE LA RUTA------")
    elif json_status == 402:
        print("No se ha encontrado la ruta")
    else:
        print("Revisar la documentación")
