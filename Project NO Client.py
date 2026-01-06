import time
import board
import adafruit_bme680 as ENV
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.SPI import SPI


def SETUP():
    def setup_ADC():
        ADC.setup()

    def setup_I2C():
        board.I2C()

    def setup_GPIO():
        GPIO.setup("P8_17", GPIO.IN)
        GPIO.setup('USR0', GPIO.OUT)
        GPIO.setup('USR1', GPIO.OUT)
        GPIO.setup('USR2', GPIO.OUT)
        GPIO.setup('USR3', GPIO.OUT)

    setup_ADC()
    setup_I2C()
    setup_GPIO()


def SevenSegInit():
    def setup_GPIO():
        GPIO.setup("P9_16", GPIO.OUT)
        GPIO.setup("P9_23", GPIO.OUT)
        GPIO.output("P9_16", GPIO.HIGH)
        GPIO.output("P9_23", GPIO.HIGH)

    def setup_SPI():
        L_Spi0 = SPI(0, 0)
        L_Spi0.mode = 0
        return L_Spi0

    setup_GPIO()
    return setup_SPI()


def SevenSegDisplay(L_Spi0, L_Number):
    DigitList = [0x7E, 0x0A, 0xB6, 0x9E, 0xCA, 0xDC, 0xFC, 0x0E, 0xFE, 0xDE]
    OnesDigit = L_Number % 10
    TensDigit = L_Number / 10
    L_Spi0.writebytes([DigitList[int(OnesDigit)], DigitList[int(TensDigit)]])


def BIG_X():
    x = ADC.read("P9_38")
    BG_NOISE = x * 49.94007191
    X = round(BG_NOISE, 1)
    return X


def T_NUM():
    T_Offset = -10
    T = ENVIRONMENT.temperature + T_Offset
    try:
        t = round(T)
        print('Data sent!')
    except ValueError:
        t = round(T)
        print('Unable to transmit data.')
    return t


def H_NUM():
    H_Offset = -20
    H = ENVIRONMENT.relative_humidity + H_Offset
    h = round(H)
    return h


def VOICE():
    global State

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


def T_Detect():
    global cold
    global State

    try:
        print("Temperature of room: %i°C" % TT)
        print(f"Humidity of room: {HH}%")
        if not State and HH >= 40 and TT >= 25:
            print("Turn on Air Conditioner")
            State = True
            if State == True:
                print("Air Conditioner is on")
                print('Data sent!')
                time.sleep(1)
        elif State and HH <= 40 and TT <= 25:
            print("Turn on Eco mode")
            cold = True
            if cold == True:
                print("Set Air Conditioner to Eco mode")
                time.sleep(1)
        time.sleep(0.5)
    except TypeError:
        print('Unable to transmit data.')
    return State and cold


def TRIP():
    global Count
    global State

    try:
        y = GPIO.input("P8_17")
        if y == 1:
            Count += 1
            print("Human is Detected")
            print(f"No. of people in the room: {Count}")
            print('Data sent!')
            time.sleep(2)
            if Count == 1:
                State = True
                print("Turn on Air Conditioner")
                if State:
                    print("Air Conditioner is on")
                    print('Data sent!')
    except Adafruit_BBIO.GPIOError as e:
        print('Unable to transmit data. Error:', str(e))

    return Count, State


SETUP()
Count = 0
G_Number = 0
cold = False
State = False
I2C = board.I2C()
G_Spi0 = SevenSegInit()
ENVIRONMENT = ENV.Adafruit_BME680_I2C(I2C, 0x77)

while True:
    XX = BIG_X()
    TT = T_NUM()
    HH = H_NUM()
    G_Number = TT
    if Count == 0:
        TRIP()
        print(f"No. of people in room: {Count}")
        print("AIR CONDITIONER IS OFF")
        print(State)
        print(cold)
        time.sleep(1)
    elif Count >= 1:
        TRIP()
        VOICE()
        T_Detect()
        SevenSegDisplay(G_Spi0, G_Number)
        print(f"No. of people in room: {Count}")
        print(State)
        print(cold)
