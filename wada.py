import socketio
import random
import time

sio = socketio.Client()


@sio.event
def connect():
    print('Connection established.')


@sio.event
def connect_error(data):
    print("The connection failed!")


@sio.event
def disconnect():
    print('Disconnected from server.')


while True:
    try:
        sio.connect('http://192.168.0.143:5000')
        break
    except:
        print("Try to connect to the server.")
        pass

while True:
    try:
        RandomNum = random.randint(0, 999)
        sio.emit('BBBW1Event', {'data': RandomNum})
        print('Data sent!')
    except:
        pass
        print('Unable to transmit data.')
    time.sleep(2)
