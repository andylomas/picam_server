### PiCamServer

Example of a webserver using Python to take pictures on a Raspberry Pi connected over a network. Uses aiohttp and socketio.

A p5.js sketch is used to create a web app to send messages to the server to take pictures, request the images from the server, and display them in a browser.

The code is designed to illustrate handling errors and lost connections, including disabling the 'Take Picture' button in the p5.js sketch if the connection is lost, and re-enabling it when the connection is restored.
