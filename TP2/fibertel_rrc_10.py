'''
IMPORTANT: Load first
export LD_LIBRARY_PATH=/usr/local/lib
'''
import pybgpstream
import pprint
import numpy as np

#---------------------------------------------------------
# Definiciones


TIME_INIT="2019-05-24"
TIME_END="2019-05-24 00:05"
COLLECTOR='rrc10'
targetAS=10481

#---------------------------------------------------------

# Configuracion de la consulta

stream = pybgpstream.BGPStream(
        from_time=TIME_INIT,
        until_time=TIME_END,
        filter="type ribs and collector %s and path %s"%(COLLECTOR,targetAS))

#---------------------------------------------------------

# Ejecucion y parseo de la consulta

# Este loop puede tardar mucho porque la RIB que estamos mirando es sumamente grande
        
for elem in stream:
    # Elementos presentes en el objeto
    #print elem.fields.keys()
    #['communities', 'next-hop', 'prefix', 'as-path']
    if targetAS in np.array(elem.fields["as-path"].split(' ')).astype(int):
        pprint.pprint(elem.fields)
