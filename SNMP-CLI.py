import sys
from SNMP import SNMP_MIB_WALK
from SNMP import SNMP_MIB_GET
from SNMP import SNMP_OID_GET

# Structure SNMP-CLI.py 192.168.1.255 [community][-o , -m] [OID or MIB] [IF MIB instance][var][-w walk, only for mib at moment]

if sys.argv[3]=='-o':
    print(SNMP_OID_GET(sys.argv[1],sys.argv[2],sys.argv[4])[1])



