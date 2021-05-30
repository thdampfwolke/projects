#!/usr/bin/python3

""" uebung: 02
"""

class Auto():

    def __init__(self, farbe, reifen, tueren, geschwindigkeit):
        self.farbe = farbe
        self.reifen = reifen
        self.tueren = tueren
        self.geschwindigkeit = geschwindigkeit

auto_1 = Auto("rot", 4, 5, "150km/h")
auto_2 = Auto("blua", 4, 2, "250km/h")

print(auto_1.farbe)
print(auto_2.geschwindigkeit)
