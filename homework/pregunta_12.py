"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    cont = dict()
    with open('files/input/data.csv') as f:
        for linea in f:
            datos = linea.split()
            d = datos[4].split(",")
            a = datos[0]
            for x in d:
                t,v = x.split(":")
                v = int(v)
                if a not in cont:    cont[a] = v
                else:                cont[a] += v
        
        resul = dict((sorted(cont.items())))

    return resul

print(pregunta_12())