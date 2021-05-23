#!/usr/bin/python3

"""
# ----------------------------------------------------------------------------
Verwaltung von Konten:
- anlegen neuer Konten
- Ueberweisungen
- Einzahlungen
- Auszahlungen

# ----------------------------------------------------------------------------
Ein Dictionary für ein vereinfachtes Konto sieht dann folgendermaßen aus:
konto = {
    "Inhaber" : "Hans Meier",       # str
    "Kontonummer" : 567123,         # integer
    "Kontostand" : 12350.0,         # float
    "MaxTagesumsatz" : 1500,        #
    "UmsatzHeute" : 10.0            #
}
"""

# ----------------------------------------------------------------------------
def neues_konto(inhaber, kontonummer, kontostand, max_tagesumsatz=1500):
    # k1 = neues_konto("Heinz Meier", 567123, 10_000.0)
    # k2 = neues_konto("Erwin Schmidt", 396754, 20_000.0)
    return {
        "Inhaber" : inhaber,
        "Kontonummer" : kontonummer,
        "Kontostand" : kontostand,
        "MaxTagesumsatz" : max_tagesumsatz,
        "UmsatzHeute" : 0
        }

def geldtransfer(quelle, ziel, betrag):
    # Hier erfolgt der Test, ob der Transfer möglich ist
    # geldtransfer(k1, k2, 160)
    if(betrag < 0 or quelle["UmsatzHeute"] + betrag > quelle["MaxTagesumsatz"] or ziel["UmsatzHeute"] + betrag > ziel["MaxTagesumsatz"]):
        # Transfer unmöglich
        return False
    else:
        # Alles OK - Auf geht's
        quelle["Kontostand"] -= betrag
        quelle["UmsatzHeute"] += betrag
        ziel["Kontostand"] += betrag
        ziel["UmsatzHeute"] += betrag
        return True

def einzahlen(konto, betrag):
    if betrag < 0 or konto["UmsatzHeute"] + betrag > konto["MaxTagesumsatz"]:
        # Tageslimit überschritten oder ungültiger Betrag
        return False
    else:
        konto["Kontostand"] += betrag
        konto["UmsatzHeute"] += betrag
        return True

def auszahlen(konto, betrag):
    if betrag < 0 or konto["UmsatzHeute"] + betrag > konto["MaxTagesumsatz"]:
        # Tageslimit überschritten oder ungültiger Betrag
        return False
    else:
        konto["Kontostand"] -= betrag
        konto["UmsatzHeute"] += betrag
        return True

def zeige_konto(konto):
    print("Konto von {}".format(konto["Inhaber"]))
    print("Aktueller Kontostand: {:.2f} Euro".format(konto["Kontostand"]))
    print("(Heute schon {:.2f} von {} Euro umgesetzt)".format(konto["UmsatzHeute"], konto["MaxTagesumsatz"]))

# ----------------------------------------------------------------------------
k1 = neues_konto("Heinz Meier", 567123, 12350.0)
k2 = neues_konto("Erwin Schmidt", 396754, 15000.0)

print('-' * 79)
zeige_konto(k1)
print('-' * 50)
zeige_konto(k2)

geldtransfer(k1, k2, 525)

print('-' * 79)
zeige_konto(k1)
print('-' * 50)
zeige_konto(k2)

print('-' * 79)
print(type(k1))

# ----------------------------------------------------------------------------

"""
K 19.0
Genau diese Wünsche befriedigt die Objektorientierung, indem sie Daten und
Verarbeitungsfunktionen zu Objekten zusammenfasst. Dabei werden die Daten
eines solchen Objekts Attribute und die Verarbeitungsfunktionen Methoden genannt.
Attribute und Methoden werden unter dem Begriff Member einer Klasse zusammengefasst.
Schematisch lässt sich das Objekt eines Kontos also folgendermaßen darstellen

Konto:
Attribute       |   Methoden
----------------|------------------
Inhaber         |   neues_konto()
Kontostand      |   geldtransfer()
MaxTagesumsatz  |   einzahlen()
UmsatzHeute     |   auszahlen()
                |   zeige()

Die Begriffe »Attribut« und »Methode« sind Ihnen bereits aus früheren Kapiteln von
den Basisdatentypen bekannt, denn jede Instanz eines Basisdatentyps stellt ein Objekt dar.
Sie wissen auch schon, dass Sie auf die Attribute und Methoden eines Objekts zugreifen,
indem Sie die Referenz auf das Objekt und das dazugehörige Member durch einen
Punkt getrennt aufschreiben.

Angenommen, k1 und k2 sind Kontoobjekte, wie sie das oben dargestellte Schema
zeigt, mit den Daten von Herrn Meier und Herrn Schmidt; dann können wir das letzte
Beispiel folgendermaßen formulieren:
>>> k1.geldtransfer(k2, 160)    ->  True
>>> k2.geldtransfer(k1, 1000)   ->  True
>>> k2.geldtransfer(k1, 500)    ->  False
>>> k2.einzahlen(500)           ->  False

>>> k1.zeige()                  ->  Konto von Heinz Meier
                                    Aktueller Kontostand: 13190.00 Euro
                                    (Heute schon 1160.00 von 1500 Euro umgesetzt)
>>> k2.zeige()                  ->  Konto von Erwin Schmidt
                                    Aktueller Kontostand: 14160.00 Euro
                                    (Heute schon 1160.00 von 1500 Euro umgesetzt)
                                    
Die Methoden geldtransfer und zeige haben nun beim Aufruf einen Parameter weniger,
da das Konto, auf das sie sich jeweils beziehen, jetzt am Anfang des Aufrufs
steht. Da sich die Methode zeige nun automatisch auf ein Konto bezieht, haben wir
den Namen der Methode entsprechend verkürzt.
Seit der Einführung der Basisdatentypen sind Sie bereits mit dem Umgang von Objekten
und der Verwendung ihrer Attribute und Methoden vertraut. In diesem Kapitel
werden Sie lernen, wie Sie Ihre eigenen Objekte mithilfe von Klassen erzeugen
können.
"""

"""
K 19.1  Klassen
Objekte werden über Klassen erzeugt. Eine Klasse ist dabei eine formale Beschreibung
der Struktur eines Objekts, die besagt, welche Attribute und Methoden es besitzt.
Mit einer Klasse allein kann man noch nicht sinnvoll arbeiten, da sie nur die Beschreibung
eines Objekttyps darstellt, selbst aber kein Objekt ist. Man kann das Verhältnis
von Klasse und Objekt mit dem von Backrezept und Kuchen vergleichen: Das
Rezept definiert die Zutaten und den Herstellungsprozess eines Kuchens und damit
auch seine Eigenschaften. Trotzdem reicht ein Rezept allein nicht aus, um die Verwandten
zu einer leckeren Torte am Sonntagnachmittag einzuladen. Erst beim Backen
wird aus der abstrakten Beschreibung ein fertiger Kuchen.
Ein anderer Name für ein Objekt ist Instanz. Das objektorientierte Backen wird daher
Instanziieren genannt. So, wie es zu einem Rezept mehrere Kuchen geben kann, können
auch mehrere Instanzen einer Klasse erzeugt werden


-->  K 19.1  Klasse  S. 352

"""

"""
# ----------------------------------------------------------------------------
# Begriffe:
# ----------------------------------------------------------------------------

# -----------------------------------------------
# Objektorientierung:
- fasst die Daten und Verarbeitungsfunktionen zu Objekten zusammen
- dabei werden die Daten eines solchen Objekts Attribute
    und die Verarbeitungsfunktionen Methoden genannt
- Attribute und Methoden werden unter dem Begriff Member einer Klasse zusammengefasst
# -----------------------------------------------
# Attribut und Methode:
- jede Instanz eines Basisdatentyps stellt ein Objekt dar 
- zugriff auf die Attribute und Methoden eines Objekts erfolgt:
    indem Sie die Referenz auf das Objekt und das dazugehörige Member durch einen Punkt getrennt aufschreiben
    z.B.: k1.geldtransfer(k2, 160)
# -----------------------------------------------
# Klasse:
stellt die Beschreibung eines Objekttyps dar, ist aber selbst kein Objekt
Objekte werden über Klassen erzeugt
Eine Klasse ist dabei eine formale Beschreibung der Struktur eines Objekts, die besagt, welche Attribute und Methoden es besitzt.
Ein anderer Name für ein Objekt ist Instanz
Instanziieren
es können mehrere Instanzen einer Klasse erzeugt werden

# -----------------------------------------------
# -----------------------------------------------


"""