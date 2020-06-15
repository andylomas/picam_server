#### PiCamServer

Example of a webserver using Python to take pictures on a Raspberry Pi connected over a network. Uses aiohttp and socketio.

A p5.js sketch is used to create a web app to send messages to the server to take pictures, request the images from the server, and display them in a browser.

The code is designed to illustrate handling errors and lost connections, including disabling the 'Take Picture' button in the p5.js sketch if the connection is lost, and re-enabling it when the connection is restored.

### Installation

1. Place the files into a suitable directory such as /home/pi/code/python/picam_server.
2. Edit 'server.py' changing the project_root variable to the directory that you used to install the files.
3. Edit 'sketch.js' changing the serverAddress variable to the URL to access the raspberry pi on the network.
4. Enable the Raspberry Pi camera using 'sudo raspi-config', selecting 'Interfacting Options' then 'Camera'.
5. Install the requirements using 'python3 -m pip install -r requirements.txt'.

If you want to automatically run on boot:

1. Add 'sudo -u pi python3 /home/pi/code/python/picam_server/server.py &' to /etc/rc.local just before the final 'exit 0' statement.
2. Change to boot using the command line interface using 'sudo raspi-config', selecting 'Boot Options' then 'Console Autologin'.
