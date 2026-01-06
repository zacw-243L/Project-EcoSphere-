The project required us to do a report, make a prototype of our connected system and present our connected system to the whole class by the end of those 16 weeks. The project had us learn a lot about embedded systems and Web Development. 

Basically we had to use a BeagleBone Black Wireless as an edge computing device running linux, where you put some Python program on it and then connect 3 to 4 Mikrobus click boards (which act as inputs, outputs (displays) and sensors ) via a Mikrobus cape to the BeagleBone Black Wireless... the laptop then hosted the website and acted as "server" where the user can watch things change as you use the inputs from the  BeagleBone Black Wireless or send a input from the website back to the BBBW board and see it output something as a display

In this repo, you will find working files for my own subsystem a Temperature Control System.
The system consists of a PC web server and BBBW board web client to enable centralized control of multiple air conditioning units in a house. The key features of the system include:

1.	Web-based application: 
Allows users to control temperature and state of the air conditioning units, set timers for turning them on and off, and view room and unit temperatures.
2.	Human presence detection: 
Utilizes an IR Eclipse sensor to detect human presence and control the air conditioning unit, accordingly, enabling automatic turning on or off.
3.	Voice control: 
Incorporates voice recognition capabilities to control the air conditioning unit by voice commands, and differentiate users based on their unique voice and speech patterns.
4.	Environmental sensing: 
Utilizes an environment sensor click to detect room temperature and humidity, allowing the system to optimize energy usage and cooling by automatically adjusting the air conditioning unit based on predefined thresholds.
5.	7-segment display: 
Displays the current state of the air conditioning unit (on or off) on a 7-segment display as well as temperature.

By implementing these functionalities, the system ensures efficient and convenient control of air conditioning units while promoting energy-saving practices.

# Block Diagram

<img width="906" height="460" alt="image" src="https://github.com/user-attachments/assets/4a60d2dd-3e4c-4f6c-8230-7b552d07f229" />

# Schematic / Circuit Diagram

<img width="917" height="909" alt="image" src="https://github.com/user-attachments/assets/dc0da38e-70da-4535-b8a7-0657995a5034" />

<img width="883" height="794" alt="image" src="https://github.com/user-attachments/assets/fb08d687-bb8b-4a25-8d2f-196fc94a8ab2" />

<img width="901" height="874" alt="image" src="https://github.com/user-attachments/assets/7de66962-d86b-46e5-946e-0a382e85015d" />

<img width="900" height="573" alt="image" src="https://github.com/user-attachments/assets/637a74b7-96d4-4d60-bcc5-22b85c822fd7" />

# Flow Chart

## BBBW Web Client
<img width="896" height="750" alt="image" src="https://github.com/user-attachments/assets/11fd08e8-2090-4280-9b7d-6415e0433a38" />

## PC Web Server
<img width="845" height="643" alt="image" src="https://github.com/user-attachments/assets/a8b93617-cbff-4562-843e-3dee4f65aca2" />

## PC Web Page
<img width="803" height="765" alt="image" src="https://github.com/user-attachments/assets/1b4e432a-ff73-4747-9fd4-3ea001b04276" />


# Link below to demonstration of the project
Below is a prototype of a smart light (from one of the team, each one had to do one subsystem), which has an occupancy detector and a dimmer <br>

[![Watch the video](https://img.youtube.com/vi/Rt7HITLo_ZI/0.jpg)](https://www.youtube.com/watch?v=Rt7HITLo_ZI)

