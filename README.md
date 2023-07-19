# OnePixelCamera

Dieses Projekt zielt darauf ab, eine Kamera zu entwickeln, die mithilfe eines Phototransistors die Helligkeit an einem bestimmten Punkt im Raum erfasst. Um ein vollständiges Bild zu erstellen, wird der Phototransistor mithilfe von Steppermotoren oder Servos gedreht. Sowohl der Phototransistor als auch die Motoren werden von einem Microcontroller gesteuert.

## Mechanik & Elektrik

### 1. Festlegung der Anforderungen

- Plattform mit 2 DOF (Rotation Horizontal und Vertikal)
- Schwenkung durch Servomotoren
- Stromzufuhr und Datenaustausch via USB-Kabel

### 2. Konzeptentwicklung
### 3. Mechanisches Design
### 4. Modellierung und Simulation
### 5. Prototyping und Testing
### 6. Überarbeitung und Optimierung
### 7. Dokumentation und Fertigungsvorbereitung

## (Optik)

## Software


#### Computer

- Auschwenkung der Kamera eingeben
- Daten via UART senden
- Bilddaten via UART empfangen
- (eventuell daten via SD-Karte einlesen)
- Bilddaten mit Bildverarbeitungsalgorithmen bearbeiten
- Bild anzeigen
- Bild speichern


#### Microcontroller

- Auschwenkdaten empfangen
- Servos ansteuern und Bildaufnahme starten
- Daten an Computer senden
- (eventuell Daten auf SD-Karte speichern)
