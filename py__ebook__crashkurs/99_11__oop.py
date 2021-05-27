#!/usr/bin/python3

class Auto():
    def __init__(self, farbe, tuer, ps):
        self.farbe = farbe
        self.tuer = tuer
        self.ps = ps

vw = Auto("rot", 4, 145)
print(vw.farbe)
