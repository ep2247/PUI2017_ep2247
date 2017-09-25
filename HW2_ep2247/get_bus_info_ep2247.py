from __future__ import print_function
import os
import json
import sys
import numpy as numpy
import pandas as pd
import certifi
import urllib.request as urllib

if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: python show_bus_locations_ep2247.py MTA_KEY bus_line bus_line.csv")

MTA_KEY = sys.argv[1]
bus_line = sys.argv[2]
fout = open(sys.argv[3],"w")
fout.write("Latitude, Longitude, Stop Name, Stop Status")

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + MTA_KEY +\
"&VehicleMonitoringDetailLevel=calls&LineRef=" + bus_line


response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

all_bus = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

for i in range(len(all_bus)):
    Latitude = all_bus[i]['MonitoredVehicleJourney']['VehicleLocation']["Latitude"]
    Longitude = all_bus[i]['MonitoredVehicleJourney']['VehicleLocation']["Longitude"]
    Stop_Name = all_bus[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    Stop_Status = all_bus[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    if len(Stop_Name) == 0:
        Stop_Name = "N/A"
    elif len(Stop_Status) == 0:
        Stop_Status = "N/A"

fout.write(str(Latitude) + str(Longitude) + str(Stop_Name) + str(Stop_Status))
