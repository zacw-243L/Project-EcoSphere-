# EcoSphere: Connected Temperature Control System

**Year 2 Connected Systems Design Module Project**  
**Nanyang Polytechnic – Electronic & Computer Engineering**  
**Team Lead & Subsystem Developer** (Group of 5 members)

This project, completed over 16 weeks, required the design, implementation, and demonstration of a **connected embedded system** for a sustainable, green living environment. Using the **BeagleBone Black Wireless (BBBW)** as the edge computing device running Linux, we interfaced multiple **mikroBUS Click boards** (sensors, displays, and actuators) via a mikroBUS cape. A laptop hosted the web server, enabling bidirectional communication: users could monitor real-time data from the BBBW and send control commands back to the board.

The system promoted **energy efficiency** and **user convenience** through intelligent automation. My primary responsibility was the **Temperature Control System** subsystem a centralised solution for managing multiple air conditioning units in a smart home.

### Key Features of the Temperature Control Subsystem

1. **Web-based Application**  
   - Intuitive interface for users to control AC unit state (on/off), set target temperature, configure timers, and monitor room/unit temperatures in real time.

2. **Human Presence Detection**  
   - Uses an **IR Eclipse sensor** to detect occupancy and automatically activate/deactivate the AC unit, reducing unnecessary energy consumption.

3. **Voice Control Integration**  
   - Implements voice recognition to accept commands (e.g., "Turn on the AC") and identifies users based on unique voice patterns for personalised control.

4. **Environmental Sensing & Optimization**  
   - Employs an **environment sensor Click** to measure room temperature and humidity.  
   - Automatically adjusts AC settings based on predefined thresholds to optimise cooling and energy usage.

5. **Local Feedback Display**  
   - 7-segment display shows current AC state (on/off) and real-time temperature for at-a-glance monitoring.

### System Architecture & Hardware Setup

- **Edge Device**: BeagleBone Black Wireless (Linux-based) running Python scripts for sensor/actuator control and web client functionality.
- **Expansion**: mikroBUS cape with 3–4 Click boards (IR sensor, environment sensor, 7-segment display, relays/actuators).
- **Server**: Laptop-hosted web server (Python-based) for centralised dashboard and command relay.
- **Communication**: Bidirectional client-server model enabling seamless monitoring and control.

### Diagrams

#### Block Diagram
<img width="906" height="460" alt="image" src="https://github.com/user-attachments/assets/4a60d2dd-3e4c-4f6c-8230-7b552d07f229" />

*(High-level overview of system components and data flow)*

#### Schematic / Circuit Diagrams
<img width="917" height="909" alt="image" src="https://github.com/user-attachments/assets/dc0da38e-70da-4535-b8a7-0657995a5034" />

<img width="883" height="794" alt="image" src="https://github.com/user-attachments/assets/fb08d687-bb8b-4a25-8d2f-196fc94a8ab2" />

<img width="901" height="874" alt="image" src="https://github.com/user-attachments/assets/7de66962-d86b-46e5-946e-0a382e85015d" />

<img width="900" height="573" alt="image" src="https://github.com/user-attachments/assets/637a74b7-96d4-4d60-bcc5-22b85c822fd7" />

#### Flow Charts

## BBBW Web Client
<img width="896" height="750" alt="image" src="https://github.com/user-attachments/assets/11fd08e8-2090-4280-9b7d-6415e0433a38" />

## PC Web Server
<img width="845" height="643" alt="image" src="https://github.com/user-attachments/assets/a8b93617-cbff-4562-843e-3dee4f65aca2" />

## PC Web Page
<img width="803" height="765" alt="image" src="https://github.com/user-attachments/assets/1b4e432a-ff73-4747-9fd4-3ea001b04276" />

### Demonstration Video
A prototype demonstration of a related smart light subsystem (occupancy detection + dimmer control) from a teammate:

[![Smart Light Prototype Demo](https://img.youtube.com/vi/Rt7HITLo_ZI/0.jpg)](https://www.youtube.com/watch?v=Rt7HITLo_ZI)

### Learning Outcomes
This project provided deep hands-on experience in:
- Embedded systems programming on Linux-based hardware (BeagleBone Black Wireless)
- Interfacing sensors/actuators via mikroBUS Click boards
- Full-stack web development for IoT applications
- System integration, real-time data handling, and energy-efficient design
- Team leadership, task delegation, and collaborative delivery under tight deadlines

**Outcome**: Earned an **A** grade for my subsystem; the overall team project achieved strong performance across all deliverables (prototype, report, and class presentation).

Feel free to explore the code in the repository — especially the Temperature Control System folder — for implementation details.
