#  Drone project Autonomous
Pixhawk + Raspberry Pi + LTE(4G) 
It is the source code of the Raspberry Pi files.

## Hardwares/Components
- Frme: **F450**
- FC: **Pixhawk1**
- Onboard computer: **Raspberry 3**
- Network: **dongel** (3G/4G)
- Radio system: **FS-I6X**  receiver **IA10B**

## Features
- Connect Pixhawk and Raspberry Pi using `mavlink`;
- Raspberry Pi runs a python script that controls the drone;
- Raspberry Pi send mavlink data to ground station through UDP;
- FPV camera send video streaming to ground station;
- The pilot can use radio control to switch on/off the video streaming;

## Software
- MissionPlanner;
- QGroundControl;
- Dronekit, Mavlink.;


## Raspberry Pi to Pixhawk Electric diagram 

![Pixhawk-to-Raspberry-PI-3-scheme](https://github.com/matanatar11/Drone-Raspberry-Pi-/assets/101950216/db418a83-dc8f-466f-a249-8d93be9606d3)


## Raspberry Pi setup 
installed Python3 mavproxy dronekit

      sudo apt-get update
      sudo apt-get upgrade
      sudo apt-get install python-pip
      sudo apt-get install python-dev
      sudo apt-get install python3-lxml
      sudo apt-get install screen python3-wxgtk4.0 python3-lxml
      sudo pip3 install pyserial
      sudo pip3 install donekit
      sudo pip3 install  MAVProxy

## Connecting to Pixhawk from raspbrry pi
      sudo mavproxy.py --master=/dev/ttyAMA0 --baudrate 57600 


## Raspbrry pi intrnet briudg to Pixhawk and Connecting to ground station
      sudo mavproxy.py --master=udp:192.168.8.100:14550 --out=/dev/ttyAMA0.5760
      sudo mavproxy.py --master=udp:10.0.0.8:14550 --out=/dev/ttyAMA0
  
## Run a script 
     
      python3 scriptnem.py
            python3 gotoNE.py


![IMG20231010133839](https://github.com/matanatar11/Drone-Raspberry-Pi-/assets/101950216/f6176a0b-ea8d-49b1-83d7-5c259091426e)

























































   
   


