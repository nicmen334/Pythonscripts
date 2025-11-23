# Ausgaben-Tracker

Mein allererstes Python-Projekt. Ein einfaches CLI-Tool zur Erfassung von Ausgaben mit Kategorien.

## 📋 Beschreibung

Dies war mein erster Versuch, ein funktionales Python-Programm von Grund auf zu schreiben, nachdem ich die Basics bei freeCodeCamp gelernt hatte. Ziel war es, ein Tool zu bauen, das ich tatsächlich nutzen kann.

## 🎯 Features

- Ausgaben mit Betrag erfassen
- Kategorien: Lebensmittel, Freizeit, Miete, Auto
- Einfache Fehlerbehandlung bei falscher Eingabe
- Ausgabe aller erfassten Ausgaben am Ende

## 💻 Verwendung
```bash
python expense_tracker.py
```

Das Programm fragt nacheinander:
1. Betrag (Zahl oder 'f' zum Beenden)
2. Kategorie-Nummer (1-4)

**Beispiel:**
```
hier betrag einfügen oder f zum beenden drücken> 25.50
hier von 1 bis 4 die verwendungszecke Lebensmittel, Freizeit, Miete, Auto wählen> 1
```

## 🎓 Was ich dabei gelernt habe

- **Listen und Datenstrukturen**: Erste Berührung mit Listen und wie man Daten speichert
- **User Input**: `input()` für Benutzereingaben
- **Fehlerbehandlung**: Mein erster `try-except` Block
- **While-Loops**: Endlosschleife mit Abbruchbedingung
- **Type Conversion**: `float()` für Zahlen-Konvertierung

## 🐛 Bekannte Bugs & Limitierungen

**Ja, der Code hat Bugs. Das war mein erstes Projekt überhaupt.**

Einige Dinge, die ich heute anders machen würde:
- Die Variable `überthemen` wird überschrieben (sollte eigentlich `kategorie` sein)
- 'f' zum Beenden funktioniert nicht richtig (ValueError bricht die Schleife ab)
- Kategorie-Auswahl ist nicht validiert (kann alles eingeben)
- Keine Speicherfunktion (Daten gehen beim Beenden verloren)
- Keine Summen-Berechnung
- Keine Übersicht nach Kategorien

**Aber:** Genau diese Bugs zu finden und zu verstehen, hat mir mehr beigebracht als perfekter Code von Anfang an.

## 🔧 Technologien

- Python 3.x
- Nur Standard-Library, keine externen Dependencies

## 📝 Was ich daraus gemacht habe

Dieser Code ist **absichtlich so geblieben** - als Erinnerung daran, wo ich angefangen habe. 

Was ich durch das Debuggen und Weiterentwickeln gelernt habe:
- Variablen-Naming ist wichtig
- Input-Validierung muss robust sein
- Daten sollten persistiert werden
- Code-Struktur mit Funktionen ist besser als ein linearer Ablauf

## 🚀 Nächste Version (Ideen)

Wenn ich das neu schreiben würde:
- [ ] Funktionen statt linearer Code
- [ ] Ordentliche Kategorie-Validierung
- [ ] CSV-Export für Datenpersistenz
- [ ] Summen nach Kategorie berechnen
- [ ] Datumsangaben hinzufügen
- [ ] 'f' zum Beenden korrekt implementieren

## 👤 Autor

Nico Mench - Mein allererstes Python-Projekt (Herbst 2024)

---

*Dieser Code zeigt, wo ich angefangen habe. Jeder fängt mal klein an. 🚀*
