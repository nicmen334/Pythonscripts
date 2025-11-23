# RPG Character Creator

Ein einfaches Python-Tool zur Erstellung von Rollenspiel-Charakteren mit Attribut-Verteilung.

## 📋 Beschreibung

Dieses Projekt war mein zweites Python-Projekt nach dem Ausgaben-Tracker. Ziel war es, ein System zu bauen, das:
- Charaktere mit Namen und Stats erstellt
- Input-Validierung implementiert
- Eine visuelle Darstellung der Attribute liefert

## 🎯 Features

- **Attribut-System**: Verteile 7 Punkte auf Strength, Intelligence und Charisma
- **Input-Validierung**: Umfassende Fehlerprüfung für alle Eingaben
- **Visuelle Darstellung**: Attribute werden mit gefüllten/leeren Kreisen angezeigt (bis max. 10)
- **Restriktionen**: 
  - Charaktername max. 10 Zeichen, keine Leerzeichen
  - Jeder Stat zwischen 1-4
  - Summe muss exakt 7 Punkte sein

## 💻 Verwendung
```python
create_character('Ren', 4, 2, 1)
```

**Output:**
```
Ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
```

## 🎓 Was ich dabei gelernt habe

- **Input-Validierung**: Wie wichtig es ist, alle möglichen Fehleingaben abzufangen
- **Type Checking**: Verwendung von `isinstance()` für robuste Validierung
- **Return-Strategie**: Early returns für Fehlerfälle, statt verschachtelte if-else-Blöcke
- **String-Formatierung**: Multi-line strings und Wiederholung von Zeichen für visuelle Ausgabe

## 🐛 Bekannte Limitierungen

- Aktuell nur CLI-basiert, kein GUI
- Keine Speicherfunktion für erstellte Charaktere
- Stats sind auf 1-4 begrenzt (Design-Entscheidung für Balance)

## 🔧 Technologien

- Python 3.x
- Keine externen Dependencies

## 📝 Nächste Schritte

Wenn ich das Projekt weiterentwickeln würde:
- [ ] JSON-Export für Charaktere
- [ ] Mehrere Charaktere gleichzeitig verwalten
- [ ] Einfaches Tkinter-GUI
- [ ] Zusätzliche Attribute (z.B. Dexterity, Wisdom)
- [ ] Save/Load-Funktionalität

## 👤 Autor

Nico Mench - Erste Python-Projekte während Selbststudium neben Vollzeitjob

---

*Dieses Projekt entstand im Rahmen meines selbstständigen IT-Lernwegs. Feedback und Verbesserungsvorschläge willkommen!*
