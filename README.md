#  Drone project Autonomous
Pixhawk + Raspberry Pi + LTE(4G) 

## Hardwares/Components
- Frme: **F450**;
- Flight Controller: **Pixhawk1**;
- Onboard computer: **Raspberry 3**;
- Network: **dongel** (3G/4G);
- Radio system: **FS-I6X**  receiver **IA10B**;

## Features
- Connect Pixhawk and Raspberry Pi using `mavlink`;
- Raspberry Pi runs a python script that controls the drone, without control from the ground
- Raspberry Pi send mavlink data to ground station through UDP;
- FPV camera send video streaming to ground station;
- The pilot can use radio control to switch on/off the video streaming;

## Software
- MissionPlanner;
- QGroundControl;
- Dronekit, Mavlink.;

## Drone ESCs motors connecting 
   Motor location and direction

<img src="https://github.com/matanatar11/Drone-Raspberry-Pi-/assets/101950216/af9290fb-06f4-46eb-b9ea-6c429c936531" width="100"  />



![motororder-quad-x-2d](https://github.com/matanatar11/Drone-Raspberry-Pi-/assets/101950216/af9290fb-06f4-46eb-b9ea-6c429c936531)

   Connecting the ESCS to the Pixhawk


![Pixhwak_outputs](https://github.com/matanatar11/Drone-Raspberry-Pi-/assets/101950216/b38fad30-746c-4303-b380-7baf7e2aad01)


## Connecting Pixhawk to FS-iA6B receiver
connection the Pixhawk (RCIN) to receiver (PPM/CH1)

![2a920606ed36b02be4c88e081c44bcebc4820e91_2_999x750](https://github.com/matanatar11/Drone-Raspberry-Pi-/assets/101950216/bad2ae77-4b02-4a4f-8521-57d1e9f512b6)


## Raspberry Pi to Pixhawk Electric diagram 

![Pixhawk-to-Raspberry-PI-3-scheme](https://github.com/matanatar11/Drone-Raspberry-Pi-/assets/101950216/da9c3078-5146-40d2-8bda-5e12142c2a5a)


## Raspberry Pi setup 
installed Python3 mavproxy and dronekit

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



![IMG20231010133839](https://github.com/matanatar11/Drone-Raspberry-Pi-/assets/101950216/a7978788-da8f-452b-a103-98ebee92a2ab)

















































