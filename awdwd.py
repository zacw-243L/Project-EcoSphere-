import socketio
import random
import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

sio = socketio.Client(logger=True, engineio_logger=True)
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
is_connect = False
connected = False
session = requests.Session()
session.mount('http://', adapter)
session.mount('https://', adapter)


@sio.on("connect")
def connect():
    global is_connect
    is_connect = True
    print('Connection established.')
    print(f"connection established with sid {sio.sid}")


def message_received(data):
    print(f'message was received!!!\n')
    print(f"message returned from server: {data}")


@sio.event
def connect_error(data):
    print("The connection failed!")


@sio.event
def disconnect():
    print('Disconnected from server.')


while not connected:
    try:
        session.get('http://192.168.1.65:8080')
        #sio.connect()
        print("Socket established")
        connected = True
        time.sleep(3)
        break
    except Exception as ex:
        print("Try to connect to the server.")
        print("Failed to establish initial connnection to server:", type(ex).__name__)
        time.sleep(5)

while True:
    try:
        RandomNum = random.randint(0, 999)
        sio.emit('BBBW1Event', {'data': RandomNum})
        print('Data sent!')
    except:
        pass
        print('Unable to transmit data.')
    time.sleep(2)
