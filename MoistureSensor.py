"""
lib of moisture sensore

"""

import pyb

# TODO seuil arbitraire
SEUIL = 2200

class MoistureSensor:
    def __init__(self, pinADC="X11"):
        self.value = 0
        self.pin = pyb.ADC(pinADC)
        
    def rawMeasure(self):
        """
        Renvoi la mesure brute du capteur
        :return: renvoie un int entre 0, et le seuil
        """
        return self.pin.read()
    
    def getValue(self):
        """
        getteur de la valeur mesuree
        :return: un float qui represente la valeur en % de l'humiditee du sol
        """
        return self.value
    
    def measure(self):
        """
        fonction qui prend la mesure du capteur la stocke en memoire et la retourne en pourcentage
        :return: float entre 0.0 et 100.0
        """
        self.value = self.pin.read() * 100 / SEUIL
        return self.value