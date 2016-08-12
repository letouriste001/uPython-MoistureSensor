import pyb

class MoistureSensor:
    
    
    def __init__(self, pinADC="X11"):
        self.value = 0
        self.pin = pyb.ADC(pinADC)
        
    def measure(self):
        
        if(self.pin.read() > 1700):
            self.value = 100
        else:
            self.value = self.pin.read() * 100 / 1700
        print("Raw : " + str(self.pin.read()))
        return self.value