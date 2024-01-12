import socketio

sio = socketio.Client(logger=True, engineio_logger=True)

@sio.event
def connect():
    print('Connection established')

@sio.event
def disconnect():
    print('Disconnected from server')

server_ip = '192.168.10.174'
server_port = 3335

sio.connect(f'http://{server_ip}:{server_port}')

# Handle the 'cw-change' event
@sio.on('cw-change')
def on_cw_change(data):
    print('cw-change data received:', data)

# Handle the 'VN30-change' event
@sio.on('VN30-change')
def on_vn30_change(data):
    print('VN30-change data received:', data)

try:
    sio.wait()
except KeyboardInterrupt:
    sio.disconnect()