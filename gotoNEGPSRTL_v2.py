
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

    # Wait until the vehicle reaches a safe height before processing the goto
    #  (otherwise the command after Vehicle.simple_takeoff will execute
    #   immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

def red_gps():
    print("do you wont? read GPS coorinates? [y/n]")
    gpsc = input()

    while gpsc == "y":      
# Printing Vehicle's Latitude
        print("Vehicle's Latitude              =  ", vehicle.location.global_relative_frame.lat)

# Printing Vehicle's Longitude
        print("Vehicle's Longitude             =  ", vehicle.location.global_relative_frame.lon)
        print("do you wont? read GPS CORD?")
        gpsc = input()

#print('Connecting to vehicle on: %s' % connection_string)
vehicle = connect('/dev/ttyAMA0', wait_ready=True,baud=57600)

red_gps()

print("do you wont this GPS PIONT [y\n]")

if input() == "y":
   Latitude = vehicle.location.global_relative_frame.lat
   Longitude = vehicle.location.global_relative_frame.lon
else: 
    print("which GPS Latitude do you wont?")
    Latitude = float(input())
    print("which GPS Longitude do you wont?")
    Longitude = float(input())

print("which altitude do you wont?")
alt1 = float(input())

Latitudehome = vehicle.location.global_relative_frame.lat
Longitudehome = vehicle.location.global_relative_frame.lon

arm_and_takeoff(alt1)
time.sleep(1)
vehicle.airspeed = 0.5
time.sleep(1)
print("Going towards first point for 15 seconds ...")
point1 = LocationGlobalRelative(Latitude, Longitude, alt1)
vehicle.simple_goto(point1)
time.sleep(1)
vehicle.mode = VehicleMode("LAND")


# sleep so we can see the change in map
print("sleep  20 seconds")
time.sleep(20)
arm_and_takeoff(alt1)

#print("Going towards second point for 30 seconds (groundspeed set to 10 m/s) ...")

print("Returning to Home")
point2 = LocationGlobalRelative(Latitudehome, Longitudehome, alt1)
vehicle.simple_goto(point2, groundspeed=10)

# sleep so we can see the change in map
#time.sleep(30)

vehicle.mode = VehicleMode("LAN")
time.sleep(5)

print("Close vehicle object")
vehicle.close()

