'''
IMPORTANT: Load first
export LD_LIBRARY_PATH=/usr/local/lib
'''
import pybgpstream
import pprint
import numpy as np
import pickle
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

# Este loop puede tardar mucho porque la RIB que estamos mirando es sumamente grande
full_bgp = list()
for elem in stream:
    full_bgp.append(elem.fields)

import pickle
with open("test.txt", "wb") as fp:   #Pickling
    pickle.dump(full_bgp, fp)
