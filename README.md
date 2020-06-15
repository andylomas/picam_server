# picam_server

Example of a webserver using Python to take pictures on a Raspberry Pi connected over a network. Uses the aiohttp, socketio and picamera Python modules.

A p5.js sketch is used to create a simple web app to send messages to the server to take pictures, request the images from the server, and display them in a browser.

The code is designed to illustrate handling errors and lost connections, including disabling the 'Take Picture' button in the p5.js sketch if the connection is lost, and re-enabling it when the connection is restored.

## Installation

1. Place the files into a suitable project directory such as /home/pi/code/python/picam_server.
2. Edit 'server.py' changing the project_root variable to the directory that you used to install the files.
3. Edit 'sketch.js' changing the serverAddress variable to the URL to access the raspberry pi on the network.
4. Enable the Raspberry Pi camera using 'sudo raspi-config', selecting 'Interfacting Options' then 'Camera'.
5. Install the requirements by cd-ing to the project directory and using 'python3 -m pip install -r requirements.txt'.

### To run the server:

1. cd to the project directory.
2. Run the server using 'python3 server.py'.

### If you want to automatically run on boot:

1. Add 'sudo -u pi python3 /home/pi/code/python/picam_server/server.py &' to /etc/rc.local just before the final 'exit 0' statement.
2. Change to boot using the command line interface using 'sudo raspi-config', selecting 'Boot Options' then 'Console Autologin'.

### To run the web application:

1. Open a browser on the client computer.
2. Enter the URL to the server such as 'http://localhost:8080', 'http://raspberrypi.local:8080' or 'http://192.168.0.18:8080'.

## Notes

The application saves all the pictures taken in the images directory of the project_root. These images aren't ever deleted by the server, so it will be necessary to occassionally empty this directory to avoid it filling up and the Raspberry Pi running out of disk space.
