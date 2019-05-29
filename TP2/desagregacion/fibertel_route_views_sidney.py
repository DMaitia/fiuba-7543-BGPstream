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
COLLECTOR='route-views.sydney'
targetAS=10481 # Fibertel

#---------------------------------------------------------

# Configuracion de la consulta

stream = pybgpstream.BGPStream(
        from_time=TIME_INIT,
        until_time=TIME_END)

#---------------------------------------------------------

# Ejecucion y parseo de la consulta

# Este loop puede tardar mucho porque la RIB que estamos mirando es sumamente grande
i = 1
for elem in stream:
    #i = i + 1
    pprint.pprint(elem.fields)
	if i == 10:
		break;
