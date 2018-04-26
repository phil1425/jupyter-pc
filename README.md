# jupyter-pc  
[![PyPI version](https://badge.fury.io/py/jupyterpc.svg)](https://badge.fury.io/py/jupyterpc)  

Tutorial zum Erstellen von PC-Versuchsprotokollen mit iPython Jupyter, jinja2 und LaTeX.

iPython Jupyter (https://jupyter.org) ist ein Browser-basiertes interaktives Python Notizbuch, in dem 
Code, Grafiken und Text zusammen in einem Dokument verwendet werden können.
In Verbindung mit dem Templating-Engine jinja2 (http://jinja.pocoo.org/docs/2.10/) lässt sich aus einer
bestehenden Vorlage (für Format, Formeln und Text) und einem Notebook (für die Auswertung der Messwerte)
ein fertiges LaTeX-Dokument erstellen. Dieses Skript soll den Einstieg in diesen Workflow erleichtern.

**Vortleile**
- Die im Notebook verwendeten Werte, Tabellen und Grafiken können direkt in
die Vorlage eingebettet werden, ohne dass erst csv-dateien abgespeichert oder werte mit ctrl-c/-v kopiert werden müssen.
- Die Fehlerrechnung wird automatisch durchgeführt 
- Wenn man einmal code für eine Aufgabe geschrieben hat, kann man ihn das nächste mal wieder verwenden ohne dass man noch einmal darüber nachdenken muss. Zum Beispiel beim erstellen von ausgleichsgeraden.
- Man lernt ein bisschen programmieren

**Nachteile**
- Dauert wahrscheinlich länger zum einarbeiten/installieren als Origin.
- Fehlermeldungen sind manchmal frustrierend
- man muss ein bisschen programmieren lernen

![https://xkcd.com/974/](https://imgs.xkcd.com/comics/the_general_problem.png)  
https://xkcd.com/974/
# Inhalt
Das von diesem Repository verwaltete Package ```jupyterpc``` enthält einige Funktionen, die dabei helfen. Dokumentation für das Package finden sich in dem zum Repository gehörigen Wiki. Sollten bei der Verwendung Probleme auftauchen kann auf der 'Issues'-Seite eine Problembericht erstellt werden.

- Voraussetzungen

- Testversion

- Setup

  - Texteditor

  - LaTeX

  - Python

- Workflow

- Einführung in Python

  - Arbeiten mit dem Interpreter

  - Datentypen und Variablen:

  - Operatoren

  - Listen

  - Dictionaries

  - Control Flow: if und for

  - Die List comprehension

  - Funktionen

  - Datenausgabe

  - Jupyterpc

  - Weitere hilfreiche Packages

- Beispiele

## Voraussetzungen

- Grundkenntnisse in einer Programmiersprache sind hilfreich, aber nicht unbedingt notewendig

- Grundkenntnisse in LaTeX (muss man wahrscheinlich sowieso lernen)

- Geduld. Trotz vieler Bibliotheken und Dokumentation 
funktioniert oft nicht alles auf Anhieb.

![https://xkcd.com/1739/](https://imgs.xkcd.com/comics/fixing_problems.png)  
https://xkcd.com/1739/
## Testversion

Jupyter Notebook lässt sich auf der Website des Projekts online ausprobieren. (jupyter.org) 

## Setup

Es werden drei unterschiedliche Programme benötigt:

- Einen Texteditor zum Schreiben der LaTeX-Vorlage

- Eine aktuelle LaTeX-Distribution

- Eine aktuelle Python-Distribution

### Texteditor

Als Editor kann von Microsoft Editor (Windows) oder gedit (ubuntu) bis hin zu TeXMaker eigentlich jedes alles benutzt werden. Viele Editoren haben aber Features, die beim Schreiben von LaTeX-Dokumenten helfen. Hier einige Beispiele:

- Atom:
Kostenloser open-source Editor mit vielen Zusatzpaketen, allerdings ist die Auswahl an Paketen unübersichtlich groß.
Empfohlene Pakete: `latex-autocomplete` `latex` 

- TeXMaker:
Zeigt auf der einen Seite den Code und auf der anderen das fertige PDF, kommt schon fertig mit allem was man braucht, einfach zu bedienen. Wurde in der LaTeX-Präsentation auch vorgestellt.

- Overleaf: Die Tex-Dateien sind online gespeichert. Zum Fertig stellen müssen sie dann allerdings herunter geladen und durch das Templating-Programm laufen gelassen werden (nicht getestet).


### LaTeX

Wer Overleaf verwendet muss sich darum nicht mehr kümmern.
Ansonsten

- Windows: lade unter http://tug.org/texlive/ den installer herunter und folge den Anweisungen

- Mac: wie Windows

- Ubuntu: `sudo apt install texlive-full`

### Python

**Wichtig: Beim installieren wird man gefragt, ob man der `$PATH` - Variable etwas hinzufügen möchte. Den haken dafür unbedinkt ankreuzen**

Am einfachsten installiert sich Anaconda: auf https://anaconda.org die Python3-distribution herunterladen und dem Installer folgen. Dann ein Konsolen-Fenster öffnen (Terminal bei Mac und cmd bei Windows) und `pip install uncertainties` eingeben, da dieses package in der standard-installation von anaconda nicht enthalten ist.  

Wer anstatt des gesamten Conda-Paketes (z.b. wegen Speicherplatz) nur das wichtigste installieren möchte, kann auch auf https://python.org python3 und pip installieren. Dann lässt sich mit dem konsolen-command `pip install jupyter-notebook matplotlib numpy jinja2 scipy uncertainties` alles installieren.

#### Das Jupyterpc-package

Das Jupyterpc-package ist eine von mir geschriebene Sammlung an Funktionen, die beim erstellen der Protokolle helfen. Zur installation einfach eine Konsole öffnen und `pip install jupyterpc` eingeben.  

Notfalls kann auch der in der Datei `jupyterpc/jupyterpc.py` enthaltene Code direkt an den Anfang jedes Notebooks gepastet werden.

**Dependencies**
- `uncertainties` https://pythonhosted.org/uncertainties/
- `scipy.odr` https://docs.scipy.org/doc/scipy/reference/odr.html  
Sollten nach der oben durchgeführten Installation aber sowieso schon vorhanden sein.

## Workflow

Das Protokoll wird in zwei Teilen geschrieben: Das LaTeX-Template und der Python-code.
In das Template kommt all das rein, was man normalerweise in ein Protokoll schreiben würde, also Deckblatt, Theorieteil, Formeln etc. Aber anstatt Messwerten, Tabellen und Grafiken werden nur Vermerke auf den Python-teil gemacht. Ein Hilfsprogramm liest später den Code und das Template ein und schreibt an die markierten stellen die von Python generierten Werte und Tabellen. Das entstehende .tex-dokument lässt sich dann ganz normal in eine PDF-Datei konvertieren. Das klingt erst mal umständlich, aber der Großteil davon passiert automatisch.  
Beispiel:  

Vorlage.tex | Python.py | Output.tex
--- | --- | ---
`\VAR{result}` | `result=5` | `5`

## Einführung in Python

Dieser Teil soll die Basics erklären, die notwendig sind, um die Messwerte in jupyter Python auszuwerten.

### Arbeiten mit dem Interpreter

Bei der Installation wurde ein Python-Interpreter mitgeliefert. Besonders praktisch ist die iPython-Konsole. In die Konsole lässt sich Python-Code eingeben, der beim Bestätigen direkt ausgeführt wird. Als ersten Test öffnen wir die Konsole und tippen ein:

```
print('Hello, World!')
```

Mit der `print()` Funktion kann man sich an jeder Stelle eines Programmes Werte als Text ausgeben lassen. 
Die Ausgabe sollte dann sein

```
Hello, World!
```
In der Python-Konsole wird aber sowieso jeder output ausgegeben, es macht also hier keinen unterschied.

Dasgleiche lässt sich natürlich auch direkt in ein jupyter-notebook schreiben. 
Ich empfehle beim Lesen dieses Kapitels einige der Beispiele in die Konsole zu schreiben und verschiedene Eingaben zu probieren, bis man den jeweiligen Befehl verstanden hat.

> mit der "Pfeil nach oben"- Taste lässt sich die letzte Eingabe wiederholen.  

### Datentypen und Variablen:

Variablen sind Platzhalter für Werte: man legt einen Buchstaben oder einen Namen fest, dem man dann einen Wert zuweisen kann. Der Wert kann dabei eine Zahl, aber auch ein String (Zusammenschluss von Buchstaben und Zahlen), Liste(mehrere Items) oder Funktion sein.

```
>>> x = 42
>>> eine_zahl = 2
>>> ein_wort = 'baum'
>>> eine_liste = [1, 2]
>>> ist_wahr = True
```

Bei der Benennung ist wichtig:

- keine Leerzeichen
- keine Sonderzeichen am Anfang des wortes
- am besten so, dass man sie später noch erkennt (`sigma_temp` ist besser als `st`)
Datentypen legen fest, was (Wertebereich, Buchstabe, Zahl etc) der Variable alles zugewiesen werden darf. 

Die Wichtigsten für uns sind int, float, bool und string. 

- int: ganze Zahl

- float: Fließkommazahl

- bool: Wahrheitswert

- string: Sequenz aus Zeichen

In Python werden Datentypen implizit gesetzt, das heißt, das Programm sucht sich den richtigen Datentyp von alleine aus. Wenn man Datentypen ineinander konvertieren möchte, geht das meist so:

```
>>> int('10')
10

>>> int(0.0120)
0

>>> str(2.324)
'2.324'

>>> float(1)
1.0000

>>> int(True)
1
```

### Operatoren

Der Zuweisungs-Operator `=` weist der Variable *davor* den Wert *dahinter* zu

Für normale Zahlen gibt es die klassischen Operatoren `+`,`-`,`*`,`/` und Python kennt auch Punkt-vor-Strich-Regeln.

```
>>> x = 5
>>> x+4
9

>>> x/2
2.5

>>> x = x+5
>>> x 
10
```

Modulo `%` gibt den Rest einer ganzzahligen Division zurück (wie in der Grundschule)
Exponenten werde mit `x**y` dargestellt

Zusammengesetzte Operatoren:

```
>>> x += 5
#ist Äquivalent zu
>>> x = x+5
```

Außerdem gibt es noch Vergleichoperatoren. Diese nehmen zwei Werte und geben einen Wahrheitswert zurück.
Für zahlen:

```
>>> 5 == 5 #gleich
True

>>> 5 == 4
False

>>> 5 > 4 #größer
True

>>> 4 <= 4 #kleiner gleich
True

>>> 'baum' == 'baum'
True

>>> 5 != 4 #nicht
True
```

Wichtig:
Der Zuweisungs-Operator `=` ist nicht gleich dem Vergleichsoperator `==`!

Operatoren für Wahrheitswerte:

```
>>>True is True #gleich
True

>>>True not True #nicht
False

>>>True and False #und 
False

>>>True or False #oder
True
```

Zuletzt gibt es noch einen relevanten Operator für Listen:

```
>>> 1 in [0, 1, 2, 3]
True

>>> 2 in [3, 4, 5, 6]
False
```

Gibt True zurück, wenn das jeweilige Element Teil der Liste ist, ansonsten False.

### Listen

Der wichtigste zusammengesetzte Datentyp für uns ist die Liste. In einer Liste können mehrere Instanzen(=Exemplare) des gleichen Datentyps aneinander gehängt werden. Das ist hilfreich, wenn man zum Beispiel eine Reihe an Messwerten genommen hat. Die Liste steht in eckigen Klammern und die einzelnen Elemente sind durch Kommata getrennt. Es lassen sich auch Listen verschachteln.

```
>>> messung_temp = [23.4, 23.5, 23.5, 23.7, 23.5]
>>> messung_zeit = [  10,   20,   30,   40,   50]

>>> messung_volt = [[1.2, 1.1], [2.3, 2.6], [3.3, 3.4]]
```

Um an eine Liste etwas anzuhängen wird append() verwendet. Ein das n-te Element der liste ruft man mit liste[n] auf.
listen lassen sich auch aneinanderhängen

```
>>> list = [4, 5, 2, 3]
>>> print('list')
[4,5,2,3]
```

Um auf ein einzelnes Element der Liste zuzugreifen, hängt man den Index in eckigen Klammern an. Der Index startet bei 0 und geht bis l-1. Möchte man vom letzten Element mit dem Zählen beginnen, kann man negative Indizes verwenden. -1 ist das letzte, -2 das vorletzte.. 

```
>>> list[0]
4

>>> list[-1]
3
```

Hier noch ein paar nützliche Funktionen

```

>>> list.append(x) 
#Fügt der Liste ein weiteres Element x am ende an

>>> list.insert(i,x) 
#Fügt ein Element x an die stelle i ein

>>> list.pop(i) 
#Entfernt Element an der Stelle i und gibt es zurück.

>>> list_ges = list_1 + list2 
#Fügt zwei listen aneinander

>>> zip([1, 3, 5], [2, 4, 6])
[[1,2],[3,4],[5,6]]
#setzt zwei listen zusammen

>>> list.replace(x, y)
#Ersetzt jedes Element x in der Liste mit y
```

> Strings sind auch Listen, das heißt, `'hallo'[2]` gibt ein 'l' zurück

### Dictionaries

Dircionaries sind auch zusammengesetzte Datentypen, aber im Gegensatz zu Listen müssen sie nicht aus demselben Datentyp zusammen gesetzt sein. Außerdem sind die Werte nicht nach Index, sonder nach ihrem Namen, dem so genannten 'key' sortiert. Ein Dictionary ist nichts anderes als eine Ansammlung aus key:value - Paaren. Man definiert es mit geschweiften Klammern.

```
>>> data_1 = {
...    'konzentration': 0.01,
...    'spannung'     : 30,
... }

>>> data_1['spannung']
30
```

Als keys kann man einige Datentypen verwenden, für unsere Zwecke ergeben meist nur Strings Sinn. Die als Werte können auch zusammengesetzte Datentypen wie eine Liste oder ein anderes Dictionary verwendet werden.
Dictionaries eignen sich besonders gut, um eine gesamte Messung mit allen dafür verwendeten Größen zu bearbeiten.

```
>>> data_2 = {
...    'konzentration':{
...        'einheit':'mol/liter',
...        'wert':0.01,
...        'fehler':0.001
...    },
...    'spannung':[30, 29, 10, 23]
... }

>>> data_2['spannung'][2]
10

>>> data_2['konzentration']['einheit']
'mol/liter'
```

Es lassen sich auch Listen aus Dictionaries machen:

```
>>> alles = [data_1, data_2]
```

### Control Flow: if und for

Diese Funktionen steuern, wann und wie oft ein Teil des Programms ausgeführt wird.
Wichtig: Hier ist das Einrücken ein muss, ansonsten funktioniert das Programm nicht richtig.

#### if

Die allgemeine Struktur ist folgende:

```
if (bedingung_1):
    #mach das eine
elif (bedingung_2):
    #mach das andere
else:
    #ansonsten mach das hier
```

Hierbei muss die Bedingung ein Ausdruck sein, der entweder wahr oder falsch zurückgibt.
`elif` und `else` sind optional. 
Es kann belibeig viele `elif` geben, aber nur ein if und ein else.

```
if(x == 10):
    print('x ist zehn')
else:
    print('x ist nicht zehn')
```

#### for

Wichtig für uns, `for` erlaubt es uns Stück für Stück durch eine Liste zu gehen.

```
for x in liste:
    #mach irgendwas
```

Die for schleife geht dann wie folgt vor:

- setze x auf das erste Element

- führe den Code aus

- setze x auf das zweite Element 

- führe den Code aus

- ...

- bis zum Ende der Liste

Wenn man einfach nur hochzählen möchte, gibt es dafür die `range(n)` funktion.
diese gibt eine Liste mit mit Werten von 0 bis n-1 zurück.

```
>>>for i in range(5):
...    print(i)

0
1
2
3
4
```

`range()` kann man außerdem auch noch einen Startwert und ein Inkrement(i++, zählt in jeder Schleife hoch) übergeben:

```
>>>for i in range(10, 30, 5):
...    print(i)

10
15
20
25
```

Mit der for-Schleife kann man beispielsweise eine Funktion auf eine Reihe von Daten anwenden:

```
>>> messung_celsius = [10, 20, 30, 40]
>>> messung_kelvin = []
>>> for i in messung_celsuis:
... messung_kelvin.append(i+273.15)
```

### Die List comprehension

Diese Funktion kann man für quasi alles verwenden, sie kombiniert die Liste, for und if kompakt in einer Zeile.

Möchte man die oben stehende for-schleife als List-comprehension schreiben, sähe das so aus:

```
messung_kelvin = [x+273.15 for x in messung_celsius]
```

Die allgemeine Struktur ist folgende:

```
[*Ausdruck* for *Variable* in list if *Bedingung*]
```

Dieses Statement führt den genannten Ausdruck über alle Elemente der liste aus, aber nur wenn die Bedingug erfüllt ist. Die Bedingung ist dabei optional

Wenn man die Elemente mehrer Listen braucht, lässt sich `zip()`verwenden:

```
>>>[x+y for x, y in zip([100, 200, 300], [1, 2, 3])]
[101, 202, 303]
```

Da ein Größteil der Arbeit beim Auswerten daraus besteht, Funktionen auf Reihen von Messwerten anzuwenden, ist dieser Befehl sehr nützlich.

Hier einige Beispiele:

```
>>>[x**2 for x in range(6)]
[0, 1, 4, 9, 16, 25]

>>>[0 for x in range(6)]
[0, 0, 0, 0, 0, 0]

>>>[[x, -x] for x in [1, 10]]
[[1, -1], [10, -10]]

>>>[x for x in range(1,50) if not True in [x%i==0 for i in range(2,x)]]
[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

### Funktionen

Funktionen sind Stücke von Code, die an einer anderen stelle aufgerufen werden können. Man kann ihnen Variablen übergeben und sie können auch Variablen (über 'return') zurückgeben.

Allgemein:

```
def Funktion(variable_1, variable_2, ...):
    #mach irgendwas
    return variable_3, variable_4, ...
```

Funktionen werden immer mit runden Klammern am Ende aufgerufen, auch wenn man ihnen nichts übergeben will.
Mit Funktionen kann man einmal geschriebenen Code wieder verwenden.
Man kann zum Beispiel eine Funktion schreiben, die einem die Summe einer Liste berechnet:

```
def summe(liste):
    sum = 0
    for wert in liste:
        summe += wert
    return sum
```

Anstatt des alles oben nochmal zu schreiben, ruft man die Funktion später mit `summe()` auf.

```
>>> liste_volumen = [100, 200, 100, 50]
>>> summe(liste_volumen)
450
```

> Funktionen können andere Funktonen (auch sich selbst) aufrufen. Was gibt diese Funktion zurück?
> 
> ```
> def f(n):
>     if(n == 1):
>         return 1
>     else:
>         return n*f(n-1)
> ```

### Datenausgabe

Innerhalb von LaTeX lässt sich mit bestimmten Markierungen Python-Code und Variablen einbinden.
Variablen werden mit `\VAR{}` eingabunden. Das Programm kopiert dann einfach den Wert für die jeweilige Variable dort hin.

```
%% for i in range(10)
    \VAR{i}
%% endfor

#wird im dokument zu

0
1
2
3
4
5
7
8
9
```

For-Schleifen sind mit zwei Prozent-Zeichen markiert. 

Wichtig: Anders als im Python-Notebook muss hier das Ende der Schleife markiert werden

#### Diagramme

Zum Visualisieren von Daten verwenden wir die externe Bibliothek `matplotlib`:
Dazu schreibt man einfach irgendwo an den Anfang des Notebooks

```
import matplotlib.pyplot as plt
```

Eine Grafik erstellt man damit so:
In diesem Beispiel wollen wir die listen `data_x` und `data_y` mit den Fehlerwerten `sigma_x` und `sigma_y` gegeneinander auftragen:

```
plt.figure() #anfang

plt.xlabel('Temperatur [K]') # achsenbeschriftung x
plt.ylabel('Spannung in Volt') # achsenbeschriftung y

plt.plot(data_x, data_y) # punkte verbunden
plt.scatter(data_x, data_y) # punkte nicht verbunden
plt.errorbar(data_x, data_y, xerr=sigma_x, yerr=sigma_y)# verbunden mit fehlerbalken

plt.errorbar(data_x, data_y, xerr=sigma_x, yerr=sigma_y, fmt='')
# nicht verbunden mit fehlerbalken

plt.savefig('bilder/grafik_V_T.pdf')# Speichert Grafik ab
plt.show() #ende
```

Die Grafik kann dann in LaTeX ganz normal eingebunden werden.

```
\includegraphics{bilder/grafik_V_T.pdf}
```

### Uncertainties
```Uncertainties``` ist ein package zum Rechnen mit Fehlerfortpflanzung. Es enthält vor allem den datentyp ```ufloat```.
Dieser Enthält neben dem normalen Zahlenwert auch die Standardabweichung. Führt man eine Berechnung mit diesem Typ aus, so wird die Standardabweichung über Gauss'sche Fehlerfortpflanzung automatisch mitberechnet. 
```
>>> from uncertainties import ufloat
>>> x = ufloat(10, 1) # 10 +/- 1
>>> y = ufloat(12, 2) # 12 +/- 2
>>> x+y
22.0+/-2.23606797749979
```
Dabei kann die durchgeführte Berechnung beliebig viele fehlerbehaftete Größen haben.

### Jupyterpc-Funktionen
```jupyterpc``` Enthält die Funktionen ```fit(), table(), sci(), ufloat(), num(), sig()``` genaue Dokumentation über die Benutzung der Funktionen gibt es auf der wiki-Seite dieses repos oben rechts. Am besten schaut man sich dazu die Beispiele an.
Eingebunden wird das package am besten mit ```from jupyterpc import *``` am Anfang des Skripts.
- ```fit```: nimmt als input zwei listen (fehlerbehaftet oder nicht) und gibt die Koeffizienten m und b der gefitteten 
Ausgleichsgerade aus.
```
>>> data_x = [1,2,3,4]
>>> data_y = [5,6,7,8]
>>> m, b = fit(data_x, data_y)
>>> m
1.0+/-1.4197849550280142e-16
>>> b
4.0+/-3.888241265752618e-16
```

- ```table```: nimmt einen Titel und eine beliebige Anzahl an Listen und gibt eine von LaTeX-Lesbare Tabelle aus.
```
\VAR{table(
  'Gemessene Werte für c=0.1',
  {
    'Temperatur [K]': data_x,
    'Standardabweichung': sigma_x,
    'Spannung [V]':data_y,
    'Standardabweichug':sigma_y
  }
)}
```
- ```sci```: gibt einen Zahlenwert (auch fehlerbehaftet) in wissenschaflticher Schreibweise LaTeX-Lesbar aus.
```
>>> sci(122321)
1.2232 \times 10^{5}
```
- ```ulist``` produziert eine Liste von fehlerbehafteten Werten. Wichtig, wenn man damit weiter rechnen möchte.
```
data_v = ulist([1,2,3,4], 1) # Alle Werte haben den Fehler 1
data_t = ulist([5,2,3,4], [1, 0.2, 0.5, 0.1]) # Die Datenpunkte haben unterschiedliche Fehler
data_s = [v*t for v,t in zip(data_v, data_t)] # data_s hat jetzt auch einen Fehlerwert. 
```
- ```num``` gibt die **Werte** einer mit ```ulist``` generierten Liste aus.
```
>>> num(data_t)
[5,2,3,5]
```
- ```sig```gibt die **Fehler** einer mit ```ulist``` generierten Liste aus.
```
>>> sig(data_t)
[1, 0.2, 0.5, 0.1]
```

beim nächsten Ausführen des Notebooks wird dann automatisch die Tabelle generiert.

### Weitere Packages
- `peakutils.indexes` (Bestimmung von peaks) http://peakutils.readthedocs.io/en/latest/tutorial_a.html
- `scipy.constants` (Naturkonstanten) https://docs.scipy.org/doc/scipy/reference/constants.html

## Beispiele

Einige Beispiele finden sich im gleichnamigen Ordner. 
Zum Anschauen einfach das ganze Repository herunterladen und und die .ipynb-Dateien mit jupyter notebook öffnen.
