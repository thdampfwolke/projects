#!/usr/bin/python3

class Inventar():
    """ Klasse: Invertar """

    def __init__(self, hw, ip):
        """ def __init__ """
        self.hw = hw
        self.ip = ip

    def print_inventar(self):
        print(self.hw)
        print(self.ip)

server_01 = Inventar("server", "1.2.3.4")

server_01.print_inventar()
