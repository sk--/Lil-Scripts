#!/bin/bash
# scans the network for smtp(25)
# by sk
# The conditions we have to test for:
#       (UNKNOWN) [192.168.13.200] 25 (smtp) : No route to host
#       (UNKNOWN) [192.168.13.201] 25 (smtp) : Connection refused
# Actually, since the output from nc seems to go straight to stdout, just grep the results
# of this script, like | grep "open"

echo "[*] Enter base range xx.xx.xx:"
read baserange

for ip in $(seq 200 254); do
        nc -nv $baserange.$ip 25 &
done
