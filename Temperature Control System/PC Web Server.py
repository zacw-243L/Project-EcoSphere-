from flask import Flask
from flask import render_template
from flask_socketio import SocketIO
from flask_socketio import emit

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.event
def Room(RxData):
    socketio.emit('Web_Room', RxData)
    print('Receive Data from Room')


@socketio.event
def State(RxData):
    socketio.emit('Web_state', RxData)


@socketio.event
def Eco_State(RxData):
    socketio.emit('Web_Eco_State', RxData)


@socketio.event
def Count(RxData):
    socketio.emit('Web_Count', RxData)


if __name__ == '__main__':
    app.run(host='192.168.0.103')
