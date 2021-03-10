"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Lab organizar videos")
    print("3- Req 2 Consultar videos tendencia por país")
    print("4- Req 1 videos por pais/categoría con mas views")
    print("5 Buscar los vídeos con más likes")
    print("6- Req  4/ Buscar videos con más likes y tag")
    print("7- req 3")
    print("0- Salir")


def initCatalog(tipo):
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog(tipo)


def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)


def printResults(ord_videos, sample=10):
    size = lt.size(ord_videos)
    if size > sample:
        print("Los primeros ", sample, " videos ordenados son:")
        i = 0
        while i <= sample:
            video = lt.getElement(ord_videos, i)
            print("Titulo: " + video["channel_title"])
            i += 1


catalog = None
"""1
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        opcion = int(
            input("Elija 1 si quiere Array_list, o opcion 2 Linked_list: "))
        if opcion == 1:
            tipo = "ARRAY_LIST"
            catalog = initCatalog(tipo)
        else:
            tipo = "LINKED_LIST"
            catalog = initCatalog(tipo)

        catalog = initCatalog(tipo)
        loadData(catalog)
        print("Videos cargados:" + str(lt.size(catalog["videos"])))

    elif int(inputs[0]) == 2:
        tipo = "ARRAY_LIST"
        catalog = initCatalog(tipo)
        loadData(catalog)

        opcion = int(input(
            "Elija el tipo de ordenamiento que quiere \n 1. selection \n 2. insertion \n 3. shell \n 4. mergesort \n 5. quicksort "))
        size_lt = int(input("Indique el número de datos: "))

        if int(opcion) == 2:
            tipo = "insertionsort"
            answer = controller.sort_type(catalog, size_lt, tipo)
        elif int(opcion) == 1:
            tipo = "selectionsort"
            answer = controller.sort_type(catalog, size_lt, tipo)
        elif int(opcion) == 4:
            tipo = "mergesort"
            answer = controller.sort_type(catalog, size_lt, tipo)
        elif int(opcion) == 5:
            tipo = "quicksort"
            answer = controller.sort_type(catalog, size_lt, tipo)
        else:
            tipo = "shellsort"
            answer = controller.sort_type(catalog, size_lt, tipo)

        print("videos cargados sort :" + str(size_lt))
        print("Tiempo transcurrido: ", answer[0], " ms")

    elif int(inputs[0]) == 3:
        
        
        print("Este es el req 2")
        country = input(
            "Ingrese el país al que le gustaría ver el vídeo con más días como tendencia:\n")
        result = controller.number_one_video(catalog, country)
        print(result)

    elif int(inputs[0]) == 4:
        size = input("Indique tamaño de la muestra: ")
        pais = input("Indique el pais: ")
        categoria = input("Indique la categoria: ")
        result = controller.sortvideosbypais(
            catalog, int(size), pais, (categoria))
        for x in lt.iterator(result):
            print(x["trending_date"], x["title"], x["publish_time"], x["channel_title"], x["views"], x["likes"], x["dislikes"])

    elif int(inputs[0]) == 5:
        size = input("Indique tamaño de la muestra: ")
        result = controller.sortvideos(catalog, int(size))
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
        print(result[1])

    elif int(inputs[0]) == 6:
        print("Este es el req 4")
        size = input("Indique tamaño de la muestra: ")
        tag = input("Indique el parámetro tag por el que le gustaría buscar")
        country = input("Indique el país por el que le gustaría buscar")
        result = controller.VideoByTagLikes(
            catalog, country, int(size), str(tag))
        for x in lt.iterator(result[0]):
            print({"Title": x["title"], "channel_title": x["channel_title"], "Publish_time": x["publish_time"],
                   "views": x["views"], "Likes": x["likes"], "Dislikes": x["dislikes"], "Tags": x["tags"], "elapsed_time": result[1]})
    elif int(inputs[0]) == 7:
        
        categoria = input("Indique la categoria: ")
        result = controller.sortvideosbycattrending(catalog, categoria)
        print(result["title"], result["channel_title"], result["category_id"])
    else:
        sys.exit(0)
sys.exit(0)
