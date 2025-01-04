"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    cont = dict()
    with open('files/input/data.csv') as f:
        for linea in f:
            if linea[0] not in cont:    cont[linea[0]] = int(linea[2])
            else: cont[linea[0]] += int(linea[2])
        
        resul = sorted(cont.items())
    return resul

#print(pregunta_03())