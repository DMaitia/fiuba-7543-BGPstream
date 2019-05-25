'''
IMPORTANT: Load first
export LD_LIBRARY_PATH=/usr/local/lib
'''
import pybgpstream
import pprint
import numpy as np
from sets import Set
#---------------------------------------------------------
# Definiciones


TIME_INIT="2019-05-24"
TIME_END="2019-05-24 00:05"
COLLECTOR='rrc10'
targetAS=10481 # Fibertel

#---------------------------------------------------------

# Configuracion de la consulta

stream = pybgpstream.BGPStream(
        from_time=TIME_INIT,
        until_time=TIME_END,
        filter="type ribs and collector %s and path %s"%(COLLECTOR,targetAS))

#---------------------------------------------------------

# Ejecucion y parseo de la consulta

# Este loop puede tardar mucho porque la RIB que estamos mirando es sumamente grande

ASPATHS_v=[]   
for elem in stream:
    #print elem.fields.keys()
    #['communities', 'next-hop', 'prefix', 'as-path']
    if targetAS in np.array(elem.fields["as-path"].split(' ')).astype(int):
        ASPATHS_v.append(np.array(elem.fields["as-path"].split(' ')).astype(int))
        
#---------------------------------------------------------

# OUTPUT: AS proveedores de Internet de fibertel

providers = set()
for ASPATH in ASPATHS_v:
    TargetPosition=np.where(ASPATH==targetAS)[0]
    providers.add(ASPATH[TargetPosition-1][0])

print providers
    
