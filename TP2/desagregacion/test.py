'''
IMPORTANT: Load first
export LD_LIBRARY_PATH=/usr/local/lib
'''
import pybgpstream
import pprint
import numpy as np
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
#np.save("full_bgp_file",full_bgp) # Graba la lista, cuidado, usa unos 17GiB de ram para hacerlo
#full_bgp = test_load = np.load("test.npy").tolist() # Carga la lista
