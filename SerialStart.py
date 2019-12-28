import serial
import io


class SerialWrapper:
    def __init__(self, device):
        self.ser = serial.Serial(device, 9600)

    def writeCommands(self, Command):
        if self.ser.is_open:
            self.ser.write(Command.encode())

    def closeSerial(self):
        self.ser.close()
