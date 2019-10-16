#! /bin/python3.7

# written by BSzekley on October 17, 2019 for refereance

import requests

# designate the file location for the TOR exit node IP list
inputpath = '/root/Downloads/toreip.txt'

url = 'https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1'
r = requests.get(url, allow_redirects=True)
open('TorBulkExitList.py', 'wb').write(r.content)

# urllib.urlretrieve("https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1", inputpath)

# read the file contents at 'inputpath'
#inputlist = inputpath.read()
# designate the file path for the cleaned up IP list
outputpath = '/root/Downloads/exit_ip_list.txt'

# reads the file designated in 'inputpath' and splits the information into a lsit of IP addresses
with open(inputpath) as ips:
    onlyips = ips.read().splitlines()
# remove the 3 non-IP lines at the beginning of the file
del onlyips[0:3]
# Write the 'onlyips' variable to the text file that 'outputpath' points to
with open(outputpath, 'w') as f:
    for eachline in onlyips:
        f.write('%s\n' % eachline)

