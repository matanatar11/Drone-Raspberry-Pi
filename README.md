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

<img src="https://github.com/matanatar11/Drone-Raspberry-Pi-/assets/101950216/af9290fb-06f4-46eb-b9ea-6c429c936531" width="300"  />




   Connecting the ESCS to the Pixhawk

<img src="https://github.com/matanatar11/Drone-Raspberry-Pi-/assets/101950216/b38fad30-746c-4303-b380-7baf7e2aad01" width="300"  />


## Connecting Pixhawk to FS-iA6B receiver
connection the Pixhawk (RCIN) to receiver (PPM/CH1)

<img src="https://github.com/matanatar11/Drone-Raspberry-Pi-/assets/101950216/bad2ae77-4b02-4a4f-8521-57d1e9f512b6" width="300"  />



## Raspberry Pi to Pixhawk Electric diagram 

<img src="https://github.com/matanatar11/Drone-Raspberry-Pi-/assets/101950216/da9c3078-5146-40d2-8bda-5e12142c2a5a" width="600"  />




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


## create a private network with zerotier

ZeroTier provides a convenient way for us to easily connect the drone and the ground station through the 4G network without having to build a VPN by ourselves.

1. Register and set up a ZeroTier account
Register a new account on zerotier.com
Login and create a new Network

2. Install zerotier-one client on Raspberry Pi
Through Zerotier, we can create a VLAN that put the Raspberry Pi drone and Ground Station in the same local network. Let us connect the Raspberry Pi to the ground station more easily.

Execute the following shell command in Raspberry Pi to download the Zerotier:

         curl -s https://install.zerotier.com | sudo bash

Testing the installation

         sudo zerotier-cli status

If you can see 200 info [ID] [version] ONLINE then successed

Make the Zerotier auto-start on system boot

       sudo systemctl enable zerotier-one

Join the zerotier to your network

       sudo zerotier-cli join [Network ID]

3. Install the Zerotier One client on the ground station PC
Download and install the Zerotier to your PC

Then select Join Network and input the Network ID

4. Approve the connection of Raspberry Pi and ground station in your Zerotier account


## Raspbrry pi intrnet briudg to Pixhawk and Connecting to ground station

      sudo mavproxy.py --master=/dev/ttyAMA0 --baudrate 57600 --out [ip pc ground station]:14550

      sudo mavproxy.py --master=/dev/ttyAMA0 --baudrate 57600 --out 10.0.0.10:14550
      
      #** sudo mavproxy.py --master=udp:192.168.8.100:14550 --out=/dev/ttyAMA0.5760
      #** sudo mavproxy.py --master=udp:10.0.0.10:14550 --out=/dev/ttyAMA0

      

  
## Run a script 
     
      python3 scriptnem.py
            python3 gotoNE.py

<img src="https://github.com/matanatar11/Drone-Raspberry-Pi-/assets/101950216/a7978788-da8f-452b-a103-98ebee92a2ab" width="300"  />
         

## video Run script  gotoNEgps.py

https://youtu.be/C_EwRV1htT0














































