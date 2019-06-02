'''
IMPORTANT: Load first
export LD_LIBRARY_PATH=/usr/local/lib
'''
import pybgpstream
from netaddr import *
import numpy as np

TIME_INIT = "2018-04-24 11:00"
TIME_END = "2018-04-24 13:00"
COLLECTOR = 'route-views2'
AS1 = 10297
AS2 = 16509

streamAs1 = pybgpstream.BGPStream(
        from_time=TIME_INIT,
        until_time=TIME_END,
        filter="type ribs and collector %s and path %s" %
            (COLLECTOR, AS1)
        )

streamAs2 = pybgpstream.BGPStream(
        from_time=TIME_INIT,
        until_time=TIME_END,
        filter="type ribs and collector %s and path %s" %
            (COLLECTOR, AS2)
        )

prefixAs1_set = set()
for elem in streamAs1:
    prefixAs1_set.add(elem.fields["prefix"])

prefixAs2_set = set()
for elem in streamAs2:
    prefixAs2_set.add(elem.fields["prefix"])

# interseccion
intersection = set()
for prefixAs1 in prefixAs1_set:
    network1 = IPNetwork(prefixAs1)
    for prefixAs2 in prefixAs2_set:
        network2 = IPNetwork(prefixAs2)
        if (network1.__contains__(network2) or network2.__contains__(network1)):
            intersection.add((AS1, prefixAs1))
            intersection.add((AS2, prefixAs2))

# ====================Impresion del output======================
print "------------Prefijos anunciados por ambos AS's------------"
print str(AS1) + ":"
for prefix in intersection:
    if (prefix[0]) == AS1:
        print prefix

print str(AS2) + ":"
for prefix in intersection:
    if (prefix[0]) == AS2:
        print prefix
