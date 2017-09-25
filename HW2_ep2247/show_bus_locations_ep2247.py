from __future__ import print_function
import os
import json
import sys
import numpy as numpy
import pandas as pd
import certifi
import urllib.request as urllib


if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python show_bus_locations_ep2247.py MTA_KEY bus_line")

MTA_KEY = sys.argv[1]
bus_line = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + MTA_KEY +\
"&VehicleMonitoringDetailLevel=calls&LineRef=" + bus_line


response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

all_bus = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

bus_position = []
for i in range(len(all_bus)):
    bus_position.append([all_bus[i]['MonitoredVehicleJourney']['VehicleLocation']["Latitude"], all_bus[i]['MonitoredVehicleJourney']['VehicleLocation']["Longitude"]])

print("Bus Line : " + all_bus[0]['MonitoredVehicleJourney']['PublishedLineName'])
print("Number of Active Buses: " + str(len(bus_position)))

for i in range(len(bus_position)):
    print("Bus " + str(i + 1) + " is at lattitude " + str(bus_position[i][0]) + " and longitude " + str(bus_position[i][1]))
