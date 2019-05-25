'''
IMPORTANT: Load first
export LD_LIBRARY_PATH=/usr/local/lib
'''
import pybgpstream
import pprint
import numpy as np

#---------------------------------------------------------
# Definiciones


TIME_INIT="2017-03-01"
TIME_END="2017-03-01 00:05"
COLLECTOR='route-views.sg'
targetAS=3

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
prefix_set=set()  
for elem in stream:
    #print elem.fields.keys()
    #['communities', 'next-hop', 'prefix', 'as-path']
    if str(targetAS) in elem.fields["as-path"].split(' '):
        try:
            ASPATHS_v.append(np.array(elem.fields["as-path"].split(' ')).astype(int))
        except:
            print "Strange element in AS-PATH"
        try:
            ASPATHS_v.set(elem.fields["prefix"])
        except:
            print "Strange prefix"
        
#---------------------------------------------------------

# OUTPUT: AS proveedores de Internet del MIT (AS3)

# Como tiene muchos PATHS, lo hago mas prolijo que el ejemplo anterior

UpstreamProvider_set=set()
for ASPATH in ASPATHS_v:
    TargetPosition=np.where(ASPATH==targetAS)[0]
    UpstreamProvider_set.add(ASPATH[TargetPosition-1][0])


for UpstreamProvider in UpstreamProvider_set:
    print UpstreamProvider

