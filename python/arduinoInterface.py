import serial

class arduino:
    def initPort(self, portName):
        #try initializing serial port
        self.s = -1
        try:
            self.s = serial.Serial(portName, 9600)
        except:
            pass
        
        return self.s