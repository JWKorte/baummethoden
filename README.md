# baummethoden

# Headline
## kleine Headline

## These are the git commands I already learned
- git commit
- git branch
- git checkout
- git clone
- git push
- git pull
=======

# Erst die Dateien zum Comitten adden git add . [für alle Dateien, jenseits von .gitgnore]
# Beim Comitten stets an die Message denken [git commit -m "Message"]
# Beim push am besten nur git push, damit der neue Branch richtig im Hub erstellt wird.
# Virtuelle Python Umgebung installieren - muss man machen, um Kompabilitätsprobleme zu umgehen.
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

# Oliver macht es so, dass er einfach im Explorer eine Neue Datei macht und die per Abkürzung der Sprache zuordnet. Geht für .gitignore und auch für die .py

# Strg S fürs Speichern, wird leider nicht so recht angezeigt

# Die nächste Aufgabe besteht darin, das Versionsmanagement zu machen. Das geschieht in einer requirements.txt und über pypi.org. Der Befehl dazu lautet: pip freeze > requirements.txt 
# Bekommt man so eine txt, macht man: pip install -r requirements.txt

# um einen neuen branch zu machen kann man auch git checkout -b "neuerbranch"
# pip freeze zeigt auch einfach die Versionen an 
# pipe freeze > in eine Datei

# Beim bauen von .py Dateien hat man in der Regel auch das Notebook offen, da man dort einfacher Dinge ausprobieren kann. Am Ende nimmt man den fertigen Code ins py.
# man muss aufpassen, wenn man nach in die readme.md schreibt, kann man sich probleme einfangen, hier, ich denke, nach dem adden! Erst arbeiten, dann committen, das ist aber gar nicht so einfach.

# weiter gehts, eher nervig. austausch.
# alles etwas nervig und überfordernd