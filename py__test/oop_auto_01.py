#!/usr/bin/python3

""" mein erster versuch """


class Auto():

    def __init__(self, tueren, raeder, farbe, geschw, test):
        self.tueren = tueren
        self.raeder = raeder
        self.farbe = farbe
        self.geschw = geschw
        self.test = test
    
    def ausgabe(self):
        print(self.test)


vw = Auto(4, 4, "rot", 150, ["a", "b", "c"])
print(vw)
print(vw.farbe)
print(vw.test)
vw.test.append("d")
print(vw.test)
vw.ausgabe()


