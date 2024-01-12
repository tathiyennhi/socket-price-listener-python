import socketio

# Create a Socket.IO client
sio = socketio.Client()

@sio.event
def connect():
    print('Connection established')
    # Emit a 'register' event with the data 'ACB'
    sio.emit('register', 'ACB')
    sio.emit('register', 'FPT')
    sio.emit('register', 'HPG')


@sio.event
def disconnect():
    print('Disconnected from server')

@sio.on('price-change')
def on_price_change(data):
    # This function will be called when a 'price-change' event is received
    print('Price change received:', data)
    # Here, you can add any specific logic to handle the price change data

# Connect to the Socket.IO server
sio.connect('http://192.168.4.166')

# Keep the program running to listen for events
try:
    sio.wait()
except KeyboardInterrupt:
    # Handle the Ctrl+C interruption
    print('Interrupted by user, disconnecting...')
    sio.disconnect()
