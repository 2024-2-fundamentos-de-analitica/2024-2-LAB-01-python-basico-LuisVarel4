"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    cont = dict()
    with open('files/input/data.csv') as f:
        for linea in f:
            d = linea.split()[-1].split(",")
            for datos in d:
                a,v = datos.split(":")
                v = int(v)
                if a not in cont:    cont[a] = [v,v]
                else: 
                    cont[a][0] = min(cont[a][0], v)
                    cont[a][1] = max(cont[a][1], v)
        
        resul = sorted(cont.items())
        r = []
        for key,val in resul: r.append((key, val[0],val[1]))
    return r

print(pregunta_06())


