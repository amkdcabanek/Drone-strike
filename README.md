# Drone Controller Application  


## Overview  
This project is a **drone controller application** built with Python and Pygame. It includes a graphical interface for controlling a simulated drone's altitude, throttle, and movement. The application also integrates client-server communication for data exchange.  



## Components  

### 1. Drone Control (`drone.py`)  
The `Drone` class implements the core logic for drone movement and control.  
- **Features**:  
  - Smooth flight mechanics using Pygame's vector operations.  
  - Mouse-based turning and keyboard inputs for altitude and throttle.  
  - Boundary constraints to keep the drone within the screen.  

### 2. Main Application (`main.py`)  
The main file initializes the Pygame environment and runs the application loop.  
- **Responsibilities**:  
  - Displays the drone, altitude, and throttle on the screen.  
  - Processes user inputs for real-time control.  

### 3. Client-Server Communication  
- **Client (`client.py`)**:  
  - Connects to the server and sends serialized data using `pickle`.  
  - Receives confirmation messages from the server.  
- **Server (`serwer.py`)**:  
  - Listens for incoming connections and processes multiple clients using threads.  
  - Deserializes and logs received data while providing feedback to clients.  

---


