import serial
import io
from time import sleep
import GUI


def init():
    ser = serial.Serial('/COM4', 9600)
    print('Connected on Port', ser.name, '\n')
    if ser.is_open:
        print('Running....')
    else:
        ser.close()
        print('COULD NOT BIND TO PORT: ', ser.name)
    return ser


Serial = init()


def main():
    GUI.buildWindow()
    print('Initiating Port Connection')


def writeCommands(Command):
    print(Command)
    if Command == "CLOSE":
        closeSerial()
    else:
        if Serial.is_open:
            Serial.write(Command.encode())


def closeSerial():
    if Serial.is_open:
        Serial.close()
        print("Closed PORT:", Serial.name)
    else:
        print("PORT WAS ALREADY CLOSED")


if __name__ == "__main__":
    main()
    closeSerial()
    pass
