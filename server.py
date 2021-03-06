from aiohttp import web
import socketio
from picamera import PiCamera
import uuid
import os

print("Starting server.py: web server to handle taking photos with the Raspberry Pi camera")

# Change the working directory to the project root
# This line should be changed depending on where you place the code
project_root = '/home/pi/code/python/picam_server'
os.chdir(project_root)

# Create an images directory if it doesn't already exist
if not os.path.exists(project_root + '/images'):
    print(f'creating images directory in {project_root}')
    os.makedirs(project_root + '/images')
    
# Start the Raspberry Pi camera
camera = PiCamera()
camera.resolution = (1024, 768)

# Setup the web server application
app = web.Application()

# Serve requests for index.html
async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

# Serve request for sketch.js
async def sketch(request):
    with open('sketch.js') as f:
        return web.Response(text=f.read(), content_type='text/javascript')

# Specify callbacks to use when get request for specified routes
app.router.add_get('/', index)
app.router.add_get('/sketch.js', sketch)

# Handle any request using /images/ in the path as a request for
# a static file from the images directory
app.router.add_static('/images/',
                      path=f'{project_root}/images',
                      name='images')

# Attach socketio asynchronous server to the web server application
# to handle messages over sockets
sio = socketio.AsyncServer()
sio.attach(app)

# Client connecting to a socket
@sio.event
def connect(sid, environ):    
    print("connect ", sid)

# 'takepicture' received on the socket
@sio.on('takepicture')
async def takepicture(sid, data):
    # Generate a unique name for the image
    uniqueImageName = f'image_{uuid.uuid4()}.jpg'

    # Print message to the console
    print(f'takepicture: sid:{sid}, file:{uniqueImageName}')

    # Capture an image using the Raspberry Pi camera
    camera.capture(f'images/{uniqueImageName}')

    # Send a message to the client with the name of the image file
    await sio.emit('picturetaken', f'images/{uniqueImageName}', to=sid)

# Client disconnecting from a socket
@sio.event
def disconnect(sid):    
    print('disconnect ', sid)

if __name__ == '__main__':
    # If we're running this file directly, start the web application
    web.run_app(app)
