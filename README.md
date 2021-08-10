# baummethoden

# Virtuelle Python Umgebung installerien
python3 -m venv .venv 
# Ein Ordner mit . am Anfang wird in der Regel nicht erkannt
# Die Virtual Python Umgebung aktivieren
Set-ExecutionPolicy Unrestricted -Scope Process
.venv\Scripts\Activate.ps1  
# Die erste Zeile wurde über Google gefunden, da das Aktivieren ohne nicht funktionierte

# Um die wieder zu deaktivieren:
deactivate

# Um Git zu sagen, was es bewegen soll, muss man eine Ignore-Liste führen.
# Zunächst wird mit "Neue Datei" eine neue Ignore-Datei geöffnet. Dort kann man dann mit den üblichen Mustern und Ausrufezeichen
# auswählen und auch ausnehmen.

# Man kann jetzt hier auch gepflegt eine neue Python Datei öffnen, nur mit dem Speichern haperts noch ein wenig...
# hab ich jetzt aber nicht hingekriegt