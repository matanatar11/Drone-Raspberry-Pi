
from __future__ import print_function
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative





def arm_and_takeoff(aTargetAltitude):
    
   # Arms vehicle and fly to aTargetAltitude.
    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

#print('Connecting to vehicle on: %s' % connection_string)
vehicle = connect('/dev/ttyAMA0', wait_ready=True,baud=57600)

print("do you wont? read GPS CORD?")
gpsc = input()

while gpsc == "y"       
# Printing Vehicle's Latitude
    print("Vehicle's Latitude              =  ", vehicle.location.global_relative_frame.lat)

# Printing Vehicle's Longitude
    print("Vehicle's Longitude             =  ", vehicle.location.global_relative_frame.lon)
    print("do you wont? read GPS CORD?")
    gpsc = input()

print("which altitude do you wont?")
alt1 = float(input())
print("which GPS Latitude do you wont?")
Latitude = float(input())
print("which GPS Longitude do you wont?")
Longitude = float(input())

arm_and_takeoff(alt1)
time.sleep(3)
vehicle.airspeed = 0.5
time.sleep(3)
print("Going towards first point for 30 seconds ...")
point1 = LocationGlobalRelative(Latitude, Longitude, alt1)
vehicle.simple_goto(point1)

time.sleep(5)

vehicle.mode = VehicleMode("LAND")
time.sleep(10)

print("Close vehicle object")
vehicle.close()

