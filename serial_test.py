import serial

ser =serial.Serial('COM4', 115200, )

while True:
    if ser.readable():
        res = ser.readline()
        print(res.decode()[:len(res)-1])