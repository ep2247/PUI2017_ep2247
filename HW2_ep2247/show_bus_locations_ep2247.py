#API key = f7337fad-74d8-46d6-8f5a-0e7c1fec7767

from __future__ import print_function
import os
import json
import sys

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


apikey = os.getenv("MTA_KEY")

key = sys.argv[1]
bus_line = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=key&VehicleMonitoringDetailLevel=calls&LineRef=bus_line"


print (url)
response = urllib.urlopen(url)
#data = response.read().decode("utf-8")
#data = json.loads(data)
