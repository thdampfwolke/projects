#!/usr/bin/python3

class BauplanKatzenKlasse():
    """ Klasse für das Erstellen von Katzen """

    def __init__(self, rufname, farbe, alter):
        self.rufname = rufname
        self.farbe = farbe
        self.alter = alter
        self.schlafdauer = 0

    def tut_miauen(self, anzahl=1):
        print(anzahl * "miau ")

    def tut_schlafen(self, dauer):
        print(self.rufname, " schläft jetzt ", dauer, " Minuten ")
        self.schlafdauer += dauer
        print(self.rufname, " Schlafdauer insgesamt: ",
              self.schlafdauer, " Minuten ")


katze_sammy = BauplanKatzenKlasse("Sammy", "orange", 3)
katze_sammy.tut_miauen(3)
katze_sammy.tut_schlafen(3)
katze_sammy.tut_schlafen(6)
