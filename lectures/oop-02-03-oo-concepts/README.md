# Lecture notes - OOP - chapter 2-3

## Chapter 2:
- Creating classes and instantiating objects
- Access control
- Python Modules
- Python docstrings

## Chapter 3
- Basic inheritance
- extending built-ins
- overriding and super


### Creating classes and instantiating objects

Lage en klasse: Nøkkelord `class` 
Klassenavnet bør starte med stor forbokstav (PEP 8). 
Metoder, attributter og parametere bør starte med liten forbokstav.

Klassediagram Person-klasse:

![Person klasse](https://github.com/henrik2706/uit-inf-1400-v23/blob/main/lectures/oop-02-03-oo-concepts/Person4.png)


Kode som tilsvarer klassediagrammet over:
```python
class Person:
    
    def __init__(self,alderen,navnet):
        self.alder = alderen
        self.navn =navnet
        
    def getAlder(self):
        return self.alder
    
    def setAlder(self,alderen):
        self.alder = alderen
             
    def getNavn(self):
        return self.navn
    
    def setNavn(self,navnet):
        self.navn=navnet
```

Lage et objekt: Bruk konstruktøren til klassen dvs klassenavnet() <-- med eventuelle argumenter som konstruktøren (se `__init__()` ) sier.
Vi ønsker å lage et Person-objekt som har alder på 21 år og som heter Ola Nordmann.

```python
p1=Person(21,"Ola Nordmann")
```
Med tilsvarende objekt-diagram:

![Person objektdiagram](https://github.com/henrik2706/uit-inf-1400-v23/blob/main/lectures/oop-02-03-oo-concepts/Person-objekt.png)


### Access control
Innkapsling, private/protected/public -> Ikke i python, alt er public. Bruk underscore _ fremfor attributter/metoder for å symbolisere at man ikke vil at andre skal lese/endre verdien direkte.

```python
class Person:
    
    def __init__(self,alderen,navnet):
        self._alder = alderen
        self._navn =navnet
        
    def getAlder(self):
        return self._alder
    
    def setAlder(self,alderen):
        if self._gyldigAlder(alderen):
            self._alder = alderen
        else:
            self._alder=0
        
        
    def getNavn(self):
        return self._navn
    
    def setNavn(self,navnet):
        self._navn=navnet
        
    def _gyldigAlder(self,alderen):
        if alderen>=0:
            return True
        else:
            return False
```

### Python Modules
For å importere moduler (.py-filer) bruker vi nøkkelordet `import`, eller `from`... `import`.

```python
import math

fakultet=math.factorial(5)
```

eller 

```python
from math import factorial

fakultet=factorial(5)
```

### Python docstring
"""Tekst""" øverst i moduler/klasser/metoder

### Basic inheritance
Fortsette med Person -> Ansatt, Student

### Extending built-ins
Arve fra build-ins-klasser

### Overriding and super
`__init__` `__str__`
