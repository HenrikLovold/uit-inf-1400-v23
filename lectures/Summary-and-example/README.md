
# 					UTLEIE 
 
Et firma som driver utleie av kjøretøy har behov for å lagre disse. Firmaet har 3 forskjellige typer kjøretøy: Personbil, motorsykkel og varebil. Dette firmaet har forskjellige garasjer hvor de lagrer kjøretøyene når de ikke er i bruk. Hver garasje har en id og ligger i en bygning som inneholder flere garasjer. For personbil er antall seter, registreringsnummer og årstall viktig. For motorsykler er registreringsnummer og årstall viktig, mens for varebil er registreringsnummer, årstall og antall liter den rommer viktig. 
Vi definerer følgende klasser: 

**Personbil:** 	Består av antall seter, registreringsnummer og årstall.

**Motorsykkel:** 	Består av registreringsnummer og årstall. 

**Varebil:** 	Består av antall liter, registreringsnummer og årstall. 

**Garasje:** 	Har en id og inneholder en liste over kjøretøy som er i denne garasjen. 

**Bygning:** 	Har navn og inneholder en liste over garasjer som er i denne bygningen. 
	
**a)**	Klassene Personbil, Motorsykkel og Varebil har noe til felles, og vi ønsker å generalisere ved å legge til en ny klasse og introdusere arv. Tegn klassediagram for klassene dine med denne generaliseringen. Du trenger ikke å ta med metoder i diagrammet, men ta med attributtene for klassene. 
 
**b)**	Implementer klassene (skriv kode for klassene). Du trenger bare å ha med __init__() og  get/set-metoder. 
 
**c)**	Lag en metode finnAntall() for Garasjeklassen som vil returnere antall kjøretøy som er lagret i denne garasjen. 
 
**d)**	Lag en metode finnIGarasje() for Garasjeklassen som vil returnere sann dersom kjøretøyet finnes i garasjen eller usann dersom den ikke gjør det. Metoden finnIGarasje() tar registreringsnummeret som parameter og bruker dette til å søke etter kjøretøyet. Eksempel på kall på metoden: garasjeobjekt.finnIGarasje("XX99999")  
 
**e)**	Lag en metode skrivutAlle() for Bygningklassen som vil skrive ut informasjon om alle kjøretøyene som er lagret i bygningen.  
 
**f)**	Lag en funksjon som tester det du har laget

**g)**	Legg til andre metoder du tenker kan være nyttig og test dem ut i funksjonen du har laget i oppgave f)
