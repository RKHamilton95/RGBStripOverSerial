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

    def clickedOn(self):
        self.writeCommands("ON\n")

    def clickedOff(self):
        self.writeCommands("OFF\n")

    def clickedBrighter(self):
        self.writeCommands("BRIGHTER\n")

    def clickedDarker(self):
        self.writeCommands("DARKER\n")

    def clickedRainbow(self):
        self.writeCommands("RAINBOW\n")

    def closeConnect(self):
        self.writeCommands("CLOSE")

    def getColor(self, color):
        if color[0] != None:
            self.writeCommands("SOLID\n")
            print(str(str(color[0][0]) + " " + str(color[0][1]) +
                      " " + str(color[0][2])) + '\n')
            self.writeCommands(
                str(str(color[0][0]) + " " + str(color[0][1]) +
                    " " + str(color[0][2])) + '\n')
