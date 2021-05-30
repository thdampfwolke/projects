#!/usr/bin/python3

class Pkw():
    """ Klasse für das Erstellen von Personenkraftwagen """

    def __init__(self, farbe, baujahr, kmstand, sitze, marke):
        self.farbe   = farbe
        self.baujahr = baujahr
        self.kmstand = kmstand
        self.sitze   = sitze
        self.marke   = marke
        self.km_gesamt = 0

    def hupen(self, anzahl = 3):
        print(anzahl * "hup ")

    def fahren(self, km):
        print(f"fahren: {km}km")
        self.kmstand += km
        print(f"ges. gefahren: {self.kmstand}km")

    def parken(self):
        print("parken")

    def ausgabe_km(self):
        print(f"ges. gefahren: {self.kmstand}km")


trabi = Pkw("rot", 1981, 143000, 4, "Trabi")
vw = Pkw("blau", 1966, 85, 4, "opel")
print(vw.kmstand)
vw.fahren(10)
vw.ausgabe_km()


# C:/Users/dargth/AppData/Local/Programs/Python/Python39/python.exe -i c:/Users/dargth/projects/py__oop/oop__05__uebung_auto.py