"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    cont = dict()
    with open('files/input/data.csv') as f:
        for linea in f:
            a = linea[0]
            v = int(linea[2])
            if a not in cont:    cont[a] = [v,v]
            else: 
                cont[a][0] = max(cont[a][0], v)
                cont[a][1] = min(cont[a][1], v)
        
        resul = sorted(cont.items())
        r = []
        for key,val in resul: r.append((key, val[0],val[1]))
    return r

#print(pregunta_05())
