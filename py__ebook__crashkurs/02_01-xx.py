#!/usr/bin/python3

"""
2-1
Einfache Nachricht: Weisen Sie eine Nachricht einer Variablen zu und geben Sie sie aus
"""
print("-" * 50, "02-01")
test = "abcdefg"
print(test)

"""
2-2
Einfache Nachrichten: Weisen Sie eine Nachricht einer Variablen zu und geben Sie
sie aus. Ändern Sie dann den Wert der Variablen in eine neue Nachricht und geben Sie
diese ebenfalls aus.
"""
print("-" * 50, "02-02")
test = "abcdefg"
print(test)
test = "xyz"
print(test)

"""
2-3
Persönliche Nachricht: Weisen Sie den Namen einer Person einer Variablen zu und
geben Sie eine einfache Nachricht an diese Person aus, z. B.:
»Hello Eric, would you like to learn some Python today?«
"""
print("-" * 50, "02-03")
name = "max mustermann"
print(f"Hello {name}, would you like to learn some Python today?")

"""
2-4
Groß- und Kleinschreibung von Namen: Weisen Sie den Namen einer Person einer
Variablen zu und geben Sie den Namen in Kleinbuchstaben, in Großbuchstaben sowie
mit großen Anfangsbuchstaben aus.
"""
print("-" * 50, "02-04")
name = "max muster"
print(name.upper())
print(name.lower())
print(name.title())

"""
2-5
Bekanntes Zitat: Geben Sie ein bekanntes Zitat und den Namen von dessen Urheber
aus. Die Ausgabe sollte so aussehen wie im folgenden Beispiel, einschließlich der Anführungszeichen:
Albert Einstein once said, "A person who never made a mistake never tried anything new."
"""
print("-" * 50, "02-05")
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

"""
2-6 Bekanntes Zitat 2: Wiederholen Sie Übung 2-5, weisen Sie aber diesmal den Namen
des Urhebers der Variablen famous_person zu. Bauen Sie die Nachricht zusammen, weisen
Sie sie der neuen Variablen message zu und geben Sie sie aus.
"""
print("-" * 50, "02-06")
famous_person = "Albert Einstein"
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)

"""
2-7
Namen bereinigen: Weisen Sie den Namen einer Person einschließlich
einiger Weißraumzeichen am Anfang und Ende einer Variablen zu.
Verwenden Sie dabei sowohl \t als auch \n jeweils mindestens einmal.
Geben Sie den Namen einmal einschließlich Weißraum aus und dann
dreimal mithilfe der Funktionen lstrip(), rstrip() und strip().
"""
print("-" * 50, "02-07")
name = "   max   \t   muster  \n   "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

"""
2-8
Alles auf 8: Schreiben Sie eine Addition, eine Subtraktion, eine Multiplikation und
eine Division, die jeweils 8 ergeben. Schließen Sie die Operationen in print-Anweisungen
ein, damit Sie das Ergebnis sehen können. Ihr Programm sollte aus vier Zeilen wie den
folgenden bestehen: print(5+3)
Die Ausgabe soll vier Zeilen umfassen, in denen jeweils das Ergebnis 8 auf der rechten
Seite steht.
"""
print("-" * 50, "02-08")


"""
2-9
Lieblingszahl: Weisen Sie Ihre Lieblingszahl einer Variablen zu. Stellen Sie mithilfe
dieser Variablen eine Nachricht zusammen, in der diese Lieblingszahl angegeben wird,
und geben Sie diese Nachricht aus.
"""
print("-" * 50, "02-09")


a = 1_000
b = 2_500
c = a + b
print(c)