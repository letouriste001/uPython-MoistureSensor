__author__ = "Christophe AUBERT"
__copyright__ = "Copyright 2016"
__credits__ = ["Christophe AUBERT"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Christophe AUBERT"
__status__ = "development"

import pyb

# TODO seuil arbitraire
SEUIL = 2200

class MoistureSensor:
    def __init__(self, pinADC="X11"):
        self.pin = pyb.ADC(pinADC)
        
    def rawMeasure(self):
        """
        Renvoi la mesure brute du capteur
        :return: renvoie un int entre 0, et le seuil
        """
        return self.pin.read()
        
    def measure(self):
        """
        fonction qui prend la mesure du capteur la stocke en memoire et la retourne en pourcentage
        :return: float entre 0.0 et 100.0
        """
        return self.pin.read() * 100 / SEUIL