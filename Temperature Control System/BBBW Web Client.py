import time
import board
import socketio
import adafruit_bme680 as ENV
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.SPI import SPI

sio = socketio.Client()


def SevenSegInit():
    GPIO.setup("P9_16", GPIO.OUT)
    GPIO.setup("P9_23", GPIO.OUT)
    GPIO.output("P9_16", GPIO.HIGH)
    GPIO.output("P9_23", GPIO.HIGH)
    L_Spi0 = SPI(0, 0)
    L_Spi0.mode = 0
    return L_Spi0


def SevenSegDisplay(L_Spi0, L_Number):
    DigitList = [0x7E, 0x0A, 0xB6, 0x9E, 0xCA, 0xDC, 0xFC, 0x0E, 0xFE, 0xDE]
    OnesDigit = L_Number % 10
    TensDigit = L_Number / 10
    L_Spi0.writebytes([DigitList[int(OnesDigit)], DigitList[int(TensDigit)]])


def SETUP():
    ADC.setup()
    board.I2C()
    GPIO.setup("P8_17", GPIO.IN)
    GPIO.setup('USR0', GPIO.OUT)
    GPIO.setup('USR1', GPIO.OUT)
    GPIO.setup('USR2', GPIO.OUT)
    GPIO.setup('USR3', GPIO.OUT)


def BIG_X():
    x = ADC.read("P9_38")
    BG_NOISE = x * 49.94007191
    X = round(BG_NOISE, 1)
    return X


def VOICE(State):
    Voice = 0
    print("Digital Value: %f" % XX)
    print("Background Noise: %f" % XX)
    if XX >= 0.5:
        Voice = XX
        print("Voice: %f" % Voice)
    if not State and 0.6 <= Voice <= 0.7:
        print("Turn on Air Conditioner")
        State = True
        if State:
            print("Air Conditioner is on")
            time.sleep(5)
    elif State and 0.7 <= Voice <= 0.8:
        print("Turn off Air Conditioner")
        State = False
        if not State:
            print("Air Conditioner is off")
            time.sleep(5)
    time.sleep(0.5)
    return State


def T_NUM():
    T_Offset = 0
    T = ENVIRONMENT.temperature + T_Offset
    t = round(T)
    try:
        sio.emit('Room', {'data': t})
        print('Data sent!')
    except:
        pass
        print('Unable to transmit data.')
    return t


def H_NUM():
    H_Offset = 0
    H = ENVIRONMENT.relative_humidity + H_Offset
    h = round(H)
    return h


def T_Detect(State):
    try:
        print("Temperature of room: %i°C" % TT)
        print(f"Humidity of room: {HH}%")
        if not State and HH >= 40 and TT >= 25:
            print("Turn on Air Conditioner")
            State = True
            if State:
                print("Air Conditioner is on")
                sio.emit('State', {'data': State})
                print('Data sent!')
                time.sleep(3)
        elif State and HH <= 40 and TT <= 25:
            print("Turn on Eco mode")
            cold = True
            if cold:
                print("Set Air Conditioner to Eco mode")
                sio.emit('Eco State', {'data': cold})
                time.sleep(3)
        time.sleep(0.5)
    except:
        pass
        print('Unable to transmit data.')
    return State


def TRIP(Count):
    try:
        y = GPIO.input("P8_17")
        if y == 1:
            Count += 1
            print("Human is Detected")
            print(f"No. of people in room: {Count}")
            sio.emit('Count', {'data': Count})
            print('Data sent!')
            time.sleep(2)
            if Count == 1:
                State = True
                print("Turn on Air Conditioner")
                if State:
                    print("Air Conditioner is on")
                    sio.emit('State', {'data': State})
                    print('Data sent!')
    except:
        pass
        print('Unable to transmit data.')
    return Count


@sio.event
def connect():
    print('Connection established.')
    GPIO.output('USR0', GPIO.HIGH)
    GPIO.output('USR1', GPIO.HIGH)
    GPIO.output('USR2', GPIO.HIGH)
    GPIO.output('USR3', GPIO.HIGH)


@sio.event
def connect_error(data):
    print("The connection failed!")


@sio.event
def disconnect():
    print('Disconnected from server.')
    GPIO.output('USR0', GPIO.LOW)
    GPIO.output('USR1', GPIO.LOW)
    GPIO.output('USR2', GPIO.LOW)
    GPIO.output('USR3', GPIO.LOW)


while True:
    try:
        sio.connect('http://192.168.0.103:5000')
        break
    except:
        print("Try to connect to the server.")
        pass

SETUP()
Count = 0
State = False
G_Number = 0
G_Spi0 = SevenSegInit()

while True:
    I2C = board.I2C()
    ENVIRONMENT = ENV.Adafruit_BME680_I2C(I2C, 0x77)
    XX = BIG_X()
    TT = T_NUM()
    HH = H_NUM()
    Count = TRIP(Count)
    G_Number = TT
    if Count == 0:
        print(f"No. of people in room: {Count}")
        print("AIR CONDITIONER IS OFF")
        time.sleep(5)
    elif Count >= 1:
        State = T_Detect(State) and VOICE(State)
        SevenSegDisplay(G_Spi0, G_Number)
