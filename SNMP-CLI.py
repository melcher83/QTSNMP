import sys
from SNMP import SNMP_MIB_WALK
from SNMP import SNMP_MIB_GET
from SNMP import SNMP_OID_GET

# Structure SNMP-CLI.py 192.168.1.255 [community][-o , -m] [OID or MIB] [IF MIB instance][var, only if not walking][-w walk, only for mib at moment]

if len(sys.argv)==1 or sys.argv[1]=='-help':
    print ('For OID LOOKUP: SNMP-CLI.exe 192.168.127.52 public -o .1.3.6.1.2.1.1.5.0')
    print ('For MIB GET   : SNMP-CLI.exe 192.168.127.52 public -m IF-MIB ifNumber 0')
    print ('TO WALK MIB   : SNMP-CLI.exe 192.168.127.52 public -m IF-MIB ifTable -w')
    print ('Hint          : You can add MIBS to the MIBS folder')
else:
    if sys.argv[3]=='-o':
        print(SNMP_OID_GET(sys.argv[1],sys.argv[2],sys.argv[4])[1])
    if sys.argv[3]=='-m' and sys.argv[6]=='-w':
        print(SNMP_MIB_WALK(sys.argv[1],sys.argv[2],sys.argv[4],sys.argv[5]))
    if sys.argv[3]=='-m':
        print(SNMP_MIB_GET(sys.argv[1], sys.argv[2], sys.argv[4], sys.argv[5],sys.argv[6]))





