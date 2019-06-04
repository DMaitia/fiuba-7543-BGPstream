'''
IMPORTANT: Load first
export LD_LIBRARY_PATH=/usr/local/lib
'''
import pybgpstream
import pprint
import numpy as np

#---------------------------------------------------------
# Definiciones


TIME_INIT="2012-05-24"
TIME_END="2012-05-24 00:05"
COLLECTOR='rrc10'
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
prefixes = {}
for elem in stream:
    #print elem.fields.keys()
    #['communities', 'next-hop', 'prefix', 'as-path']
    #pprint.pprint(elem.fields)
    ASPATHS_set.add(tuple(np.array(elem.fields["as-path"].split(' ')).astype(int).tolist()))
    prefix_set.add(elem.fields["prefix"])
    originAS_set.add(np.array(elem.fields["as-path"].split(' ')).astype(int)[-1])
    
    origin = np.array(elem.fields["as-path"].split(' ')).astype(int)[-1]
    if not (origin in prefixes):
        prefixes[origin] = [elem.fields["prefix"]]
    else :
        prefixes[origin] += [elem.fields["prefix"]]
    
#---------------------------------------------------------
print "---------------------------"
print "Cantidad de prefijos en funcion de los AS origenes\n"
for origin in prefixes:
    print str(origin) + ": " + str(len(list(dict.fromkeys(prefixes[origin]))))  

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
