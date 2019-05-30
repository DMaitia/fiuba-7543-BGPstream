'''
IMPORTANT: Load first
export LD_LIBRARY_PATH=/usr/local/lib
'''
import pybgpstream
import pprint
import numpy as np
import netaddr
from itertools import groupby
from netaddr import *
#---------------------------------------------------------
# Definiciones


TIME_INIT="2018-05-31"
TIME_END="2018-05-31 00:05"
COLLECTOR='route-views.sg'

#---------------------------------------------------------

# Configuracion de la consulta

stream = pybgpstream.BGPStream(from_time=TIME_INIT,
    until_time=TIME_END,
    filter='type ribs and collector %s' % (COLLECTOR))

#---------------------------------------------------------

# Ejecucion y parseo de la consulta
#


# Este loop puede tardar mucho porque la RIB que estamos mirando es sumamente grande
table = list()
cant_usadas = 0
cant_descartadas = 0
for elem in stream:
    as_path = elem.fields["as-path"]
    #Algunas entradas tienen arrays adentro, no se como interpretarlas, las descarto
    if not "}" in as_path:
        cant_usadas = cant_usadas + 1
        as_path_list = as_path.split(' ')
        as_id = int(as_path_list[-1])
        prefix = elem.fields["prefix"]
        table.append((as_id, prefix))
    else:
        cant_descartadas = cant_descartadas + 1

print(
    "Se descartaron el ", \
    float(cant_descartadas)/(cant_descartadas + cant_usadas) * 100, \
    "% de las entradas")

#Saco entradas repetidas
table = list(dict.fromkeys(table))
print("Hay " + str(len(table)) + " de entradas en la tabla desagregada")
#Convierto la string del prefijo en un objeto IPNetwork
table = list(map(lambda (as_id, prefix): (as_id, IPNetwork(prefix)), table))
table.sort(key = lambda x: x[0])

groups = []
uniquekeys = []
for key, group in groupby(table, lambda x: x[0]):
    groups.append(list(group))
    uniquekeys.append(key)
#Groups tiene el formato
# [[(id1, prefijo1_1), (id1, prefijo1_2)],[(id2, prefijo1_1) ....]]
# [x[1] for x in lista] se queda con la segunda columna de una lista de tuplas
tabla_prefijos_mismo_id = list(map(lambda x: [y[1] for y in x], groups))
#Agrego las ips
tabla_agregada = list(map(lambda x: netaddr.cidr_merge(x), tabla_prefijos_mismo_id))
cantidad_entradas_tabla_agregada = map(lambda x: len(x), tabla_agregada)
cantidad_entradas_tabla_agregada = reduce(lambda x, y: x + y, cantidad_entradas_tabla_agregada)

print("Hay " + str(cantidad_entradas_tabla_agregada) + " de entradas en la tabla agregada")
