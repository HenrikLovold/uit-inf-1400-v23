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

Klassediagram Person-klasse:

![Person klasse](https://github.com/henrik2706/uit-inf-1400-v23/blob/main/lectures/oop-02-03-oo-concepts/Person.png)

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

Lage et objekt: Bruk konstruktøren til klassen dvs klassenavnet() <-- med eventuelle argumenter som konstruktøren sier.
Vi ønsker å lage et Person-objekt som har alder på 21 år og som heter Ola Nordmann.

```python
p1=Person(21,"Ola Nordmann")
```




lag objektdiagram og kode
Person("Ola Nordmann", 21)


### Access control
Innkapsling, private/protected/public -> Ikke i python, alt er public. Bruk underscore _ for å symbolisere at man ikke vil at andre skal lese/endre verdien direkte.

### Python Modules
Eksempler import


### Python docstring
"""Tekst""" øverst i moduler/klasser/metoder

### Basic inheritance
Fortsette med Person -> Ansatt, Student

### Extending built-ins
Arve fra build-ins-klasser

### Overriding and super
`__init__` `__str__`
