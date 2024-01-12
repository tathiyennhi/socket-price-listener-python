import socketio

# Create a Socket.IO client
sio = socketio.Client(logger=True, engineio_logger=True)

# Define the event handler for the 'connect' event
@sio.event
def connect():
    print('Connection established')
    # Emit a 'register' event with the 'ACB' symbol to the server
    sio.emit('register', 'ACB')
    # After emitting the register event, we'll disconnect
    sio.disconnect()

# Define the event handler for the 'disconnect' event
@sio.event
def disconnect():
    print('Disconnected from server')

# Connect to the Socket.IO server (defaulting to port 80)
sio.connect('http://192.168.4.166')

# Since we're not using sio.wait(), the script will end after this line.
