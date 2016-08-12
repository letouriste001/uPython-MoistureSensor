import pyb

class MoistureSensor:
    
    
    def __init__(self):
        self.value : 0
        self.pin = pyb.Pin