"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    cont = dict()
    with open('files/input/data.csv') as f:
        for linea in f:
            datos = linea.split()
            d = datos[3].split(",")
            v = int(datos[1])
            for letra in d:
                if letra not in cont:    cont[letra] = v
                else:                cont[letra] += v
        
        resul = dict((sorted(cont.items())))
    return resul

#print(pregunta_11())