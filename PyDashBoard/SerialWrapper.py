import serial
import io


class SerialWrapper:
    def __init__(self, device, baudRate):
        self.ser = serial.Serial(device, baudRate)

    def writeCommands(self, Command):
        try:
            if self.ser.is_open:
                self.ser.write(Command.encode())
        except:
            print("Could not connect to serial.")

    def closeSerial(self):
        self.ser.close()
