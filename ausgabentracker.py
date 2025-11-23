print('mein ausgabentracker')
ausgaben = []
überthemen = [ 'Lebensmittel', 'Freizeit', 'Miete', 'Auto']
Zahl = True
while Zahl :
    eingabe = input('hier betrag einfügen oder f zum beenden drücken>')
    eingabe2 = input('hier von 1 bis 4 die verwendungszecke Lebensmittel, Freizeit, Miete, Auto wählen>')
    try:
        betrag = float(eingabe)
        überthemen = eingabe2
        ausgaben.append([betrag, überthemen])
    except ValueError:
        print('Bitte eine gültige Zahl eingeben')
        Zahl = False
print(ausgaben)