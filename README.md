#  Drone project Autonomous
Pixhawk + Raspberry Pi + LTE(4G) 
It is the source code of the Raspberry Pi files.

## Hardwares/Components
- frme: **F450**
- FC: **Pixhawk1**
- Onboard computer: **Raspberry 3**
- Network: **dongel** (3G/4G)

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



## Source Files in /home/pi/
| files in                                 | descriptions                                                                                    |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------- |
| glympse/glympse.py                       | Send drone's GPS position to Glympse                                                            |
| mavlink-router-service/mavlink-router.sh | Routing mavlink from FC to GCS                                                                  |
| jpeg-stream/sender2.py                   | Sending low bandwidth, low latency video stream                                                 |
| jpeg-stream/receiver2.py                 | Receiving and playback the stream video (moved to https://github.com/rc-bellergy/groundstation) |
| jpeg-stream/control2.py                  | Use remote control to start, stop, recording video                                              |
| offboard/rtl-altitude.py                 | Adjust RTL altitude based on the max elevation on the RTL path (under development)              |




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

   
   


