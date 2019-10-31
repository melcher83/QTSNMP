import sys
from SNMP import SNMP_MIB_WALK
from SNMP import SNMP_MIB_GET
from SNMP import SNMP_OID_GET

# Structure SNMP-CLI.py 192.168.1.255 [community][-o , -m] [OID or MIB] [IF MIB instance][var, only if not walking][-w walk, only for mib at moment]

if sys.argv[3]=='-o':
    print(SNMP_OID_GET(sys.argv[1],sys.argv[2],sys.argv[4])[1])
if sys.argv[3]=='-m' and sys.argv[6]=='-w':
    print(SNMP_MIB_WALK(sys.argv[1],sys.argv[2],sys.argv[4],sys.argv[5]))
if sys.argv[3]=='-m':
    print(SNMP_MIB_GET(sys.argv[1], sys.argv[2], sys.argv[4], sys.argv[5],sys.argv[6]))



