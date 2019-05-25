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
COLLECTOR='route-views.sydney'
targetAS=18353

#---------------------------------------------------------

# Configuracion de la consulta

# En este ejemplo se busca un prefijo determinado

stream = pybgpstream.BGPStream(
        from_time=TIME_INIT,
        until_time=TIME_END,
        filter="type ribs and collector %s and path %s"%(COLLECTOR,targetAS))

#---------------------------------------------------------

# Ejecucion y parseo de la consulta

# Este loop puede tardar mucho porque la RIB que estamos mirando es sumamente grande

ASPATHS_set=set()
prefix_set=set()
originAS_set=set()    
for elem in stream:
    #print elem.fields.keys()
    #['communities', 'next-hop', 'prefix', 'as-path']
    #pprint.pprint(elem.fields)
    ASPATHS_set.add(tuple(np.array(elem.fields["as-path"].split(' ')).astype(int).tolist()))
    prefix_set.add(elem.fields["prefix"])
    originAS_set.add(np.array(elem.fields["as-path"].split(' ')).astype(int)[-1])
    
#---------------------------------------------------------

print "---------------------------"
print "AS-PATHS que se observaron hacia el destino\n"
for ASPATH in ASPATHS_set:
    print ASPATH
    
#---------------------------------------------------------

print "---------------------------"
print "Prefijos (incluyendo desagregados) que se observaron\n"
for prefix in prefix_set:
    print prefix
    
#---------------------------------------------------------
print "---------------------------"
print "AS orginante del prefijo\n"

for originAS in originAS_set:
    print originAS
