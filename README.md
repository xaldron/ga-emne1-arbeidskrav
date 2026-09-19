# Jøran Tvedt



**Introduksjon**



Hei!

Mitt navn er Jøran Tvedt. Jeg er student på Backend-programmering ved Gokstad og dette er første arbeidskrav på studiet.


Jeg har lært en del grunnleggende Python på egenhånd gjennom følgende kurs på Udemy: https://www.udemy.com/course/complete-python-bootcamp/?couponCode=MT260907G2



Jeg bruker kursmateriellet som kilde og referanse til studiet nå i dag som student ved Gokstad akademiet. 
Kursmateriell for kurset finnes på dette repoet: https://www.udemy.com/course/complete-python-bootcamp/?couponCode=MT260907G2



Siden jeg har gjort dette kurset før går jeg inn med en innstilling om å bruke minst mulig KI. Jeg har en ambisjon om å minimum løse oppgave 1 helt uten hjelp av KI. Jeg liker godt å finne ut ting selv, som for eksempel å bruke kilder som w3schools og kikke på tilgjengelige methods til ulike datatyper for eksempel, når jeg skal løse en kode-oppgave. 



Når jeg må ty til KI for å finne ut av ting, kommer jeg i hovedsak til å benytte meg av den innebygde modellen "Junie" i PyCharm editor. Det har noen fordeler, som for eksempel at KI'en kan "lese" koden min direkte i editor uten at jeg må drive å kopiere og lime så mye frem og tilbake, i tillegg til at den ikke oppgir så mange eksterne lenker som gjør svarene lengre. Dette gjør også at denne readme-filen kan holdes noe kortere. 





**Oppgave 1:**



Her har jeg lykkes med ambisjonen min om å ikke bruke KI i løsningen. 

Jeg kan heller ikke se at det kommer frem av arbeidskravet at jeg skal oppgi noen refleksjoner eller begrunnelser rundt denne oppgaven her i readme. 



**oppgave 2:**



I denne oppgaven blir jeg innledningsvis bedt om "en list som inneholder elementer av typen dict eller tuple." Avslutningsvis blir jeg bedt om å forklare datastrukturvalget i denne readme. 



Jeg valgte å benytte en list med dictionaries til denne oppgaven. Først og fremst fordi jeg er fra før kjent med at tuples er immutable i Python. Da jeg ikke var helt sikker på om jeg ville komme til å måtte skrive kode som skulle gjøre endringer i listen så jeg for meg at dette kunne by på upraktiske utfordringer. Jeg vet at med dictionaries kan man uansett bruke "tuple unpacking" for å hente ut nøkler og verdier, og at jeg sånn sett ville få litt trening i begge datastrukturene. Videre synes jeg at dictionaries med sin oppbygging med key/value pairs egnet seg best for denne oppgaven sin "natur", og da jeg ikke har benyttet dictionaries så mye tidligere syntes jeg det var en god mulighet for litt ekstra trening i dette, særlig siden disse ville vært plassert i en liste og jeg vet at jeg da ville få en ekstra utfordring med å hente ut ordbøkene ut fra listen før jeg kunne hente ut dets egne verdier. 



I denne oppgaven har jeg ikke kommet utenom litt KI-hjelp for å løse noen utfordringer underveis. I tillegg har jeg benyttet meg av en god kilde jeg fant på nettet som løsning på en utfordring rundt det å sortere verdier fra ordbøkene i listen, og brukte da "-ai" i søket bevisst for å ikke få opp KI-svar på dette. Jeg legger ved alle KI-prompts, svar og dette google-søket med benyttet kilde i kronologisk rekkefølge under: 



**1)**

"Prompt:  

“Traceback (most recent call last): 

File "C:\\Users\\Studier\\PycharmProjects\\GA\\Emne1\\ga-emne1-arbeidskrav\\oppgave-2.py", line 59, in <module> 

display\_sessions() 

\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~^^ 

File "C:\\Users\\Studier\\PycharmProjects\\GA\\Emne1\\ga-emne1-arbeidskrav\\oppgave-2.py", line 55, in display\_sessions 

for k,v in dicts: 

^^^ 

ValueError: too many values to unpack (expected 2) 



Kva betyr denne feilmeldinga?” 



Svar:  



“Configured authentication: Managed by agent 

Forklaring på feilmeldinga 

Feilmeldinga ValueError: too many values to unpack (expected 2) oppstår på linje 55: 

for k, v in dicts: 

Kvifor skjer dette? Når du itererer over ei ordbok (dictionary) direkte i Python med for ... in dicts:, itererer Python berre over nøklane (keys), ikkje både nøklar og verdiar.  

Nøklane i ordbøkene dine er strenger som "topic", "duration\_minutes" og "status".  

Når du skriv for k, v in dicts:, prøver Python å pakke ut kvar enkelt nøkkelstreng inn i to variablar (k og v). Sidan strengen "topic" har 5 teikn (eller "duration\_minutes" har 16 teikn), har strengen fleire enn dei 2 verdiane Python forventar – derav feilmeldinga too many values to unpack (expected 2). 



Korleis fikse det? 

For å iterere over både nøklar og verdiar i ei ordbok, må du bruke metoden .items(): 

def display\_sessions(): 

&#x20;   if study\_sessions == \[]: 

&#x20;       print('Beklager. Det finnes ingen studieøkter registrert ennå.') 

&#x20;   else: 

&#x20;       for dicts in study\_sessions: 

&#x20;           for k, v in dicts.items(): 

&#x20;               print(k, v) 

&#x20;           print('\\n') 

Ved å bruke dicts.items() returnerer Python par med (nøkkel, verdi), som trygt kan pakkast ut i k og v.” "



**2)** 

Prompt: 



def display\_completed():   

&#x20;   for dicts in study\_sessions:   

&#x20;       for k in dicts.items():   

&#x20;           if k\["status"] == "complete":   

&#x20;               print(k)   



display\_completed()   



"Kvifor funker ikkje dette? Eg har prøvd litt ulike variantar for å få det til. Eg reiknar med du skjønar kva eg prøver på?"    



&#x20;



Svar:   



Kvifor koden ikkje fungerer 

Det er hovudsakleg tre grunnar til at denne funksjonen ikkje fungerer som forventa: 

&#x20;   Bruk av dicts.items() i ei indre løkke: 

&#x20;   Variabelen dicts er allereie ei ordbok (dict) frå lista study\_sessions. 

&#x20;   Når du gjer for k in dicts.items():, blir k ein tuppel med eit nøkkel-verdi-par (t.d. ('topic', 'Operators')). 

&#x20;   Når du deretter prøver k\["status"], får du ein TypeError (tuple indices must be integers or slices, not str), fordi ein tuppel ikkje kan indekserast med strengar. Du treng ikkje den indre løkka for å sjekke statusen. 

&#x20;   Statusverdien manglar ein d: 

&#x20;   I study\_sessions er statusen sett til "completed". 

&#x20;   I if-vilkåret sjekkar du mot "complete". 

&#x20;   Utskrift: 

&#x20;   Dersom du berre vil skrive ut heile ordboka eller formatere ho slik du gjer i display\_sessions(), gjer du det direkte på ordbok-objektet. 



Korleis løyse det 

1\. Enkel variant (skriv ut heile ordboka) Her sjekkar du ordboka direkte: 

def display\_completed(): 

&#x20;   for session in study\_sessions: 

&#x20;       if session\["status"] == "completed": 

&#x20;           print(session) 



2\. Formatert variant (tilsvarande display\_sessions()) Dersom du ønskjer same formatering som i display\_sessions(), og vil handtere tilfellet der ingenting er fullført enno: 

def display\_completed(): 

&#x20;   completed\_sessions = \[s for s in study\_sessions if s\["status"] == "completed"]   

&#x20;   if not completed\_sessions: 

&#x20;       print("Ingen fullførte studieøkter funne.") 

&#x20;       return 



&#x20;   for session in completed\_sessions: 

&#x20;       print("") 

&#x20;       for k, v in session.items(): 

&#x20;           print(k.capitalize() + ":", v) 



**3)**

Google søk: 

"how to sort a list of dictionaries in python -ai"



Kilde jeg fant og benyttet meg av med direkte påvirkning i oppgaven: 

https://medium.com/@aayushiagarwal1999/python-grouping-sorting-list-of-dictionaries-3a82747fb09c 



**4)**

Prompt:  

"Kvifor får eg opp denna feilmeldinga når study\_sessions er global?" 



"Traceback (most recent call last): 

File "C:\\Users\\Studier\\PycharmProjects\\GA\\Emne1\\ga-emne1-arbeidskrav\\oppgave-2.py", line 157, in <module> 

choose\_program() 

\~\~\~\~\~\~\~\~\~\~\~\~\~\~^^ 

File "C:\\Users\\Studier\\PycharmProjects\\GA\\Emne1\\ga-emne1-arbeidskrav\\oppgave-2.py", line 143, in choose\_program 

study\_sessions.append(register\_session()) 

^^^^^^^^^^^^^^ 

UnboundLocalError: cannot access local variable 'study\_sessions' where it is not associated with a value" 



Svar:  



Configured authentication: Managed by agent 

Kvifor oppstår UnboundLocalError? 

Grunnen til at denne feilen oppstår er linje 151 i funksjonen choose\_program(): 



elif choice == 5: 

&#x20;   study\_sessions = sort\_duration() 



Når Python kompilerer ein funksjon, sjekkar den om ein variabel blir tilordna ein verdi (med =) ein eller annan stad inne i funksjonen. Dersom variabelen blir tilordna noko inne i funksjonen, reknar Python den automatisk som ein lokal variabel for heile funksjonsblokka – sjølv om det finst ein global variabel med same namn utanfor funksjonen. 

Sidan study\_sessions = ... finst under val 5, trur Python at study\_sessions er ein lokal variabel i heile choose\_program(). Når du då vel 1 og koden prøver å køyre study\_sessions.append(...), har den lokale variabelen enno ikkje fått nokon verdi, og Python kastar feilmeldinga:   UnboundLocalError: cannot access local variable 'study\_sessions' where it is not associated with a value. 



Korleis løyse problemet? 



Alternativ 1: Deklarere global study\_sessions (Raskaste fiks) Dersom du ønskjer å endre på den globale variabelen inne i choose\_program(), må du fortelje Python eksplisitt at du refererer til den globale variabelen øvst i funksjonen: 



def choose\_program(): 

&#x20;   global study\_sessions  # Fortel Python at study\_sessions er global 

&#x20;   menu\_on = True 

&#x20;

&#x20;   while menu\_on: 

&#x20;       ... 



Alternativ 2: Sortere lista "in-place" med .sort() I staden for å overskrive variabelen med study\_sessions = sort\_duration(), kan du sortere lista direkte på staden utan å tilordne med =. Då treng du ikkje global-nøkkelordet: 



\# I menyval 5: 

elif choice == 5: 

&#x20;   from operator import itemgetter 

&#x20;   print('Sorterer... ') 

&#x20;   study\_sessions.sort(reverse=True, key=itemgetter('duration\_minutes')) 

&#x20;   print('Sortering vellykka! Bruk menyvalg 2 for å se oppdatert liste.') 



Prompt 2: 



“Eg fann ei bedre løysing, som var å gje choose\_program eit argument, og deretter bytta ut variabelen study\_session med dict\_list, for så endre elif statement til det samme og putte study\_session som argument når eg køyrer choose\_program” 



Svar 2: 



God tilnærming med argument og parametrar! 



Å sende inn lista som eit argument (dict\_list) til funksjonar er generelt svært god programmeringspraksis. Det gjer koden meir modular, gjenbrukbar og gjer at ein slepp å vere avhengig av globale variablar. 



Det er likevel eit par viktige detaljar i koden din du bør vere merksam på no når du har gått for denne løysinga:  



1\. Nokre funksjonar les framleis frå den globale variabelen 



Når du no sender dict\_list inn i choose\_program(dict\_list), brukar du dict\_list i: 

&#x20;   dict\_list.append(...) (val 1) 

&#x20;   display\_sessions(dict\_list) (val 2) 

&#x20;   dict\_list = sort\_duration(dict\_list) (val 5) 

Men desse tre funksjonane les framleis direkte frå den globale study\_sessions: 

&#x20;   display\_completed() (val 3) 

&#x20;   search\_topic() (val 4) 

&#x20;   display\_duration\_completed() (val 6) 



Dersom du vil fullføre den gode løysinga di, bør desse tre funksjonane også ta imot dict\_list som parameter, til dømes: 



def display\_completed(dict\_list): 

&#x20;   completed\_sessions = \[s for s in dict\_list if s\["status"] == "completed"] 

&#x20;   ... 



2\. Kva som skjer ved tilordning etter sortering (dict\_list = sort\_duration(...)) 

Når du køyrer: 



dict\_list = sort\_duration(dict\_list) 



skjer følgjande: 

&#x20;   sort\_duration brukar sorted(), som lagar ei heilt ny liste i minnet. 

&#x20;   Den lokale variabelen dict\_list inne i choose\_program peikar no på denne nye lista. 

&#x20;   Den globale study\_sessions på utsida peikar framleis på den opphavlege lista. 



Dersom du legg til ei ny økt med menyval 1 etter at du har sortert (val 5), vil økta bli lagt til i den nye lista (dict\_list), medan den globale study\_sessions ikkje får den nye økta med seg.



Oppsummering og anbefaling 



Løysinga di er heilt på rett spor. For å gjere koden 100 % konsekvent og robust: 

&#x20;   Oppdater display\_completed(dict\_list), search\_topic(dict\_list) og display\_duration\_completed(dict\_list) til å ta imot dict\_list. 

&#x20;   Kall dei med dict\_list som argument inne i choose\_program(). 

Då fungerer heile programmet uavhengig av globale variablar inne i menyen. 





**Oppgave 3:** 

I denne oppgaven er jeg bedt om å dokumentere 6 gyldige og ugyldige testtilfeller i tillegg til all dokumentasjon på KI-bruk. 
Den offisielle datetime-modulen fremsto som det opplagte valget til denne oppgaven. Jeg har hørt om modulen før, men aldri brukt den. 
Jeg oppdaget derfor tidlig at jeg hadde behov for litt KI-hjelp med å forstå dokumentasjonen, ettersom jeg opplever den som veldig teknisk og lite "oversiktlig"

| Funksjon/Del         | Type test | Input                                                                                                        | Resultat                                                                                                                                                                 |
|----------------------|-----------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| add_date             | Ugyldig   | 26/06-98                                                                                                     | Fanges opp av except clause i funksjonen og printer tilbakemelding.                                                                                                      |
| add_date             | Gyldig    | 26.06.1998                                                                                                   | Funksjonen returnerer en datoverdi som forventet. Legges til i en liste m/tilbakemelding.                                                                                | 
| start_end            | Gyldig    | 1:30 + 13                                                                                                    | Forventet feilmelding. Men var gyldig. Registreres som kl. ett om natten og avsluttes 1:43.                                                                              | 
| start_end/menyvalg 3 | Ugylidg   | Halv to                                                                                                      | Fanges opp av except og blir bedt om å prøve på nytt.                                                                                                                    | 
| start_end/menyvalg 3 | Ugyldig   | 24:30                                                                                                        | Samme som over. Datetime godtar ikke 24 som en time-input og derfor akitveres except.                                                                                    | 
| days_between         | Gyldig    | 19.09.2026, 15.09.2026                                                                                       | abs-funksjonen (absolute number) sørger for at dager mellom datoene holdes som et positivt heltall selv om første input er lengre frem i tid enn siste.                  | 
| days_between         | ugylidg   | 31.02.2026                                                                                                   | Fanges opp av except clause i funksjonen og printer tilbakemelding. Datetime godtar ikke 31. Februar som en gyldig dato og gir feilmelding.                              | 
| add_date             | gyldig    | 16.10.2026                                                                                                   | Legges til for å få flere datoer i listen                                                                                                                                | 
| add_date             | gyldig    | 25.04.2057                                                                                                   | Legges til for å få flere datoer i listen, litt frem i tid for å sjekke at sortering funker etterpå.                                                                     | 
| list_of_dates_sorted | gyldig    | programmet legger til datoer fra funksjon/menyvalg 1 til en liste. Denne listen brukes når sortering kjøres. | Output sorterer datoer i riktig rekkefølge.                                                                                                                              | 
| list_of_dates_sorted | ugyldig   | Prøver å kjøre funksjonen med tom liste.                                                                     | En tom liste blir også returnert. Genererer ikke feilmelding i seg selv, men det kunne vært en ide å legge til en feilmelding i output om at det ikke er noe å sortere.  | 

**Prompt 1**
Oppgåva seier blant anna at eg skal "en funksjon som tar imot en dato på formatet dd.mm.åååå og returnerer en datoverdi når teksten er gyldig" 

Forstår eg denne delen av python-dokumentasjonen rett, at eg kan be om input av det formatet og så gir python error om input ikkje er lik formatet? 

"classmethod date.strptime(date_string, format) 

Return a date corresponding to date_string, parsed according to 
 format. This is equivalent to: 

date(*(time.strptime(date_string, format)[0:3])) 
  

ValueError is raised if the date_string and format 
 can’t be parsed by time.strptime() or if it returns a value which isn’t a 
 time tuple. See also strftime() and strptime() behavior and 
 date.fromisoformat()." 

**Svar**
Ja — nesten, og du er inne på akkurat rett spor. Det er ein viktig liten nyanse. 

date.strptime() gjer ikkje sjølv input-funksjonen. Du kan først få inn tekst med input(), og så prøve å tolke teksten som ein dato: 

tekst = input("Skriv inn dato (dd.mm.åååå): ") 
dato = date.strptime(tekst, "%d.%m.%Y") 

Her betyr: 

    "%d" → dag med to siffer  

    "%m" → månad med to siffer  

    "%Y" → år med fire siffer  

Så dersom brukaren skriv: 

15.09.2026 

blir dato ein faktisk date-verdi. 

Men dersom brukaren skriv noko som ikkje kan tolkast etter formatet, vil Python normalt gi: 

ValueError 

For eksempel: 

15-09-2026 

eller: 

15.9.2026 

kan føre til ValueError fordi teksten ikkje passar formatet du oppgav. 

Og dette er sannsynlegvis sjølve poenget med oppgåva: Du skal lage ein funksjon som prøver dette, og handtere situasjonen der brukaren skriv noko ugyldig. 

Dokumentasjonen seier altså i praksis: 

«Prøv å tolke denne teksten som ein dato etter dette mønsteret. Klarer eg det ikkje, kastar eg ValueError.» 

Det fine er at dokumentasjonen faktisk fortel deg akkurat kva verktøy du treng. Du treng ikkje finne opp ein masse manuell kontroll av om teikn 3 er ".", om teikn 6 er ".", om månaden er mellom 1 og 12 osv. 😄 

Og ein liten ting å vere obs på: strptime() kan òg avsløre semantisk ugyldige datoar, ikkje berre feil skiljeteikn. 31.02.2026 er til dømes ikkje ein gyldig dato og vil derfor også utløyse ValueError. 

Så eg ville lese oppgåveteksten som: 

tekst → prøv strptime() → gyldig? returner date → ugyldig? handter ValueError. 

Dette er ein fin oppgåve for deg no, fordi ho eigentleg testar akkurat den datetime-modellen vi nettopp gjekk gjennom. 

 
**google-søk med benyttet kilde:**
“is python time class not compatible with timedelta? -ai” 

https://stackoverflow.com/questions/656297/python-time-timedelta-equivalent 

 

**Prompt 2**


one_date = date(1998, 6, 26) 
another_date = date(1990, 12, 18) 
 
def days_between(date_1, date_2): 
    '''Take inn two dates and return (positive) days between them''' 
    return abs(date_1 - date_2) 
 
gimme_days = days_between(another_date, one_date) 
print(gimme_days) 
  

"Kvifor får eg eit klokkeslett med på return her, når eg berre bruker date som ikkje skal ha med klokka? Har prøvd å finne døme i dokumentasjonen og på google, men greier ikkje heilt finne ut av det. Eg vil berre ha antall dagar mellom datoane” 

**Svar:**  

Kvifor klokkeslettet kjem med 

Når du trekkjer to date-objekt frå kvarandre (date_1 - date_2), returnerer Python eit timedelta-objekt frå datetime-modulen. 

Sjølv om du berre brukte datoar (utan tidspunkt), har standard strengrepresentasjon for eit timedelta-objekt formatet: 

X days, HH:MM:SS (til dømes 2747 days, 0:00:00). 

Når du brukar print(gimme_days), blir timedelta-objektet gjort om til ein streng med dette standardformatet, og derfor kjem 0:00:00 med. 

 

Korleis hente berre talet på dagar 

Eit timedelta-objekt har eit eige attributt som heiter .days. Dette gjev deg talet på dagar som eit heiltal (int). 

Du kan endre funksjonen din slik: 

def days_between(date_1, date_2): 
    '''Take in two dates and return (positive) days between them''' 
    return abs((date_1 - date_2).days) 
  

eller alternativt: 

def days_between(date_1, date_2): 
    '''Take in two dates and return (positive) days between them''' 
    delta = abs(date_1 - date_2) 
    return delta.days 
  

Då vil print(gimme_days) berre skrive ut talet på dagar, til dømes 2747. 

 

 

**Prompt 3:**  

“Hmmm. Det gikk ikke helt. TIngen er at jeg i følge arbeidskravet "Dokumenter minst seks gyldige og ugyldige testtilfeller". Nå så jeg det litt sent,  og har ingen logg fra når jeg har forsøkt å kjøre koden underveis” 

 

**Svar:**  

Det gjør ingenting at du ikke har loggen fra tidligere kjøringer!  

Når et arbeidskrav ber om å «Dokumentere minst seks gyldige og ugyldige testtilfeller», betyr det ikke at du må ha tatt vare på historiske logger fra utviklingen. Det betyr at du skal sette opp og dokumentere et sett med planlagte tester (både med riktige og feilaktige inndata) for å vise at koden din oppfører seg som forventet og håndterer feil på en god måte. 

Du kan enkelt utføre disse testene nå og føre dem inn i README.md. 

 

Hvordan strukturere testtilfellene i README.md 

En oversiktlig og ryddig måte å dokumentere tester på er i en tabell eller en punktliste med: 

    Test ID / Funksjon: Hva som testes. 

    Type: Gyldig (happy path) eller Ugyldig (ugyldig format, feil datatype, osv.). 

    Inndata (Input): Hva du sender inn til funksjonen/input-feltet. 

    Forventet resultat: Hva programmet skal gjøre (f.eks. returnere dato, eller gi en feilmelding uten å krasje). 

    Faktisk resultat: Hva programmet faktisk gjorde da du testet det. 

 

Eksempel på 6 gyldige og ugyldige testtilfeller 

Her er et konkret forslag til tester du kan kjøre på funksjonene dine (f.eks. i oppgave-3.py eller oppgave-1/oppgave-2): 

# 
	

Funksjon / Del 
	

Type test 
	

Inndata (Input) 
	

Forventet resultat 
	

Faktisk resultat 

1 
	

add_date 
	

Gyldig 
	

"26.06.1998" 
	

Returnerer et gyldig dato-objekt for 26. juni 1998 
	

Dato-objekt opprettet som forventet 

2 
	

add_date 
	

Ugyldig (feil format) 
	

"1998-06-26" 
	

Fanges opp av except, gir feilmelding om ugyldig format 
	

Feilmelding skrives ut 

3 
	

add_date 
	

Ugyldig (ugyldig dato) 
	

"32.01.2024" 
	

Fanges opp av except (dag 32 finnes ikke), gir feilmelding 
	

Feilmelding skrives ut 

4 
	

days_between 
	

Gyldig 
	

date(2024, 1, 1) og date(2024, 1, 10) 
	

Returnerer 9 (antall dager mellom) 
	

Returnerte 9 

5 
	

start_end 
	

Gyldig 
	

time(13, 0) og 45 minutter 
	

Returnerer "13:45:00" 
	

Returnerte "13:45:00" 

6 
	

choose_program (Meny) 
	

Ugyldig (feil datatype/tall) 
	

Menyvalg "abc" eller 99 
	

Gir beskjed om ugyldig valg og ber om nytt input 
	

Ber brukeren prøve igjen 

 

Viktig tips til oppgave-3.py før du tester: 

I funksjonen add_date i oppgave-3.py står det nå: 

def add_date(new_date): 
    try: 
        return date.strptime(new_date, "%d.%m.%Y") 
    except: 
        print('Beklager, det ser ut til at du har oppgitt en ugyldig dato. Vennligst prøv igjen (dd.mm.åååå)') 
  

I standardbiblioteket til Python finnes strptime på datetime, ikke på date. Derfor vil date.strptime kaste en AttributeError som except-blokken din fanger opp – noe som gjør at selv gyldige datoer feilaktig gir feilmelding. 

Du kan justere den slik: 

def add_date(new_date): 
    '''take in a date with dd.mm.yyyy format and return the date''' 
    try: 
        return datetime.strptime(new_date, "%d.%m.%Y").date() 
    except ValueError: 
        print('Beklager, det ser ut til at du har oppgitt en ugyldig dato. Vennligst prøv igjen (dd.mm.åååå)') 
  

Da vil gyldige datoer (som "26.06.1998") fungere perfekt, mens ugyldige datoer (som "32.13.2024" eller "tekst") fanges opp av except! 

 

**Prompt 4:**  

“Hvorfor fungerer ikke valg 4 slik det står nå? Det returnerer jo en datetime.date verdi på valg nummer en. Men, når jeg prøver å kjøre valg 4 så får jeg opp print statement under if clausen min. :/ Her står jeg litt fast..” 

 

**Svar:**  

“ 

Hvorfor koden alltid går inn i if-blokken 

Det er to hovedgrunner til at if-testen slår til selv når datoene er gyldige: 

 

1. Hvordan Python evaluerer or Når du skriver: 

if one_date or another_date != type(datetime.date): 
  

tolker Python det som to uavhengige uttrykk på hver side av or: 

    one_date (venstre side) 

    another_date != type(datetime.date) (høyre side) 

I Python har et gyldig date-objekt en «sannhetsverdi» som er True (truthy). Fordi venstresiden (one_date) er True, evalueres hele if-betingelsen umiddelbart til True – uten at Python engang sjekker resten. 

 

2. Sammenligning med type(datetime.date) 

    date (eller datetime.date) er allerede en klasse/type i Python. 

    type(datetime.date) returnerer typen til selve typen, altså <class 'type'>.  

    Et vanlig dato-objekt (f.eks. 2024-05-10) har typen <class 'datetime.date'>, så another_date != type(datetime.date) ville uansett alltid vært True. 

 

Hva skjer ved gyldig vs. ugyldig dato i add_date? 

I funksjonen din: 

    Gyldig dato: Returnerer et date-objekt. 

    Ugyldig dato: Fanges opp av except ValueError:, skriver ut en feilmelding, og returnerer ingenting – som i Python betyr at funksjonen returnerer None. 

Dermed trenger du bare å sjekke om enten one_date eller another_date er None (eller mangler verdi). 

 

Løsning 

Du kan endre if-sjekken i menyvalg 4 til: 

   elif choice == 4: 
        one_date = add_date(input('Vennligst oppgi en dato (dd.mm.åååå): ')) 
        another_date = add_date(input('Vennligst oppgi enda en dato (dd.mm.åååå): ')) 
 
        if not one_date or not another_date: 
            print("Beklager. Det ser ut til at du har oppgitt en eller to ugyldige datoer, eller ugyldig format. Vennligst prøv igjen\n") 
        else: 
            print(f"Dager mellom disse to datoene er: {days_between(one_date, another_date)}\n") 
  

Alternativt med eksplisitt sjekk mot None: 

       if one_date is None or another_date is None: 
  

 

Tips for enda bedre brukeropplevelse (løkke ved feil) 

Hvis du vil at programmet skal tvinge brukeren til å skrive inn på nytt med én gang hvis en dato er feil (slik du har gjort i oppgave-1.py og oppgave-2.py), kan du hente datoene i en liten while-løkke: 

   elif choice == 4: 
        one_date = None 
        while not one_date: 
            one_date = add_date(input('Vennligst oppgi en dato (dd.mm.åååå): ')) 
 
        another_date = None 
        while not another_date: 
            another_date = add_date(input('Vennligst oppgi enda en dato (dd.mm.åååå): ')) 
 
        print(f"Dager mellom disse to datoene er: {days_between(one_date, another_date)}\n") 
  

Da slipper brukeren å havne helt tilbake i hovedmenyen dersom den andre datoen ble skrevet feil.” 

 

Prompt:  

“Uff, nå begynner eg å bli litt stressa. Prøver å få til ei løysing på menyvalg 3, med bruk av strptime som du ser. Men, det funker ikkje og eg tykkjer at dokumentation er heilt håplaus å skjøne med rare døme og kompliserte forklaringar. No byrjar eg kraftig å tvile på meg sjølv og om eg har talent for dette studiet.” 

 

Svar:  

“Frustrasjon som investering og læringskostnad 

Å kjenne på motstand i møte med teknisk dokumentasjon er en helt naturlig og forutsigbar del av læringsprosessen. Dokumentasjonen for datetime i standardbiblioteker er skrevet for maksimal teknisk presisjon snarere enn pedagogisk enkelhet, noe som ofte skaper midlertidig friksjon. Å oppleve dette betyr ikke manglende talent, men at du er midt i en overgangsfase der du tilegner deg ferdigheter som gir stor langsiktig verdi. 

Den mest rasjonelle tilnærmingen for å minimere stress og maksimere fremdrift er å bryte ned hva som teknisk skjer i koden, rette de konkrete feilene, og etablere et robust mønster du kan gjenbruke. 

 

Hvorfor koden i menyvalg 3 ikke fungerer 

Linjen du forsøkte: 

if new_time == time.strptime(new_time, "%HH:%MM"): 
  

har tre konkrete årsaker til at den feiler: 

    Formateringskodene (%H vs %HH): 

    I strptime betyr %H i seg selv to-sifret time (00–23) og %M to-sifret minutt (00–59). 

    Skriver du "%HH:%MM", forventer Python at brukeren skriver bokstavene H og M bokstavelig talt (f.eks. 14H:30M). 

    Riktig formatering for 14:30 er "%H:%M". 

    Hva strptime gjør og hvor den bor: 

    Klassen time i datetime-modulen har normalt ikke strptime. Den tilhører datetime-klassen: datetime.strptime(...). 

    datetime.strptime() returnerer et datetime-objekt dersom teksten er gyldig. Hvis teksten er feil, kaster den et ValueError. Den returnerer altså aldri True eller den opprinnelige strengen. 

    Sammenligning: 

    new_time == ... sammenligner en streng ("14:00") med et dato/tid-objekt. Dette vil alltid være False. 

 

Hvordan konvertere streng til et gyldig time-objekt 

Funksjonen din start_end(start_time, duration_in_minutes) forventer et time-objekt og et antall minutter.  

For å gjøre en gyldig tekststreng som "14:30" om til et time-objekt, parser vi med datetime.strptime() og henter ut .time(): 

time_obj = datetime.strptime("14:30", "%H:%M").time() 
  

Hvis brukeren taster noe ugyldig (f.eks. "25:70" eller "tekst"), fanger vi opp ValueError med try/except. 

 

Komplett og effektiv løsning for menyvalg 3 

Her er en strukturert løsning som: 

    Validerer klokkeslettet med try/except. 

    Validerer at varigheten er et positivt heltall (slik oppgaveteksten krever). 

    Kaller start_end() og viser sluttiden for brukeren. 

   elif choice == 3: 
        # 1. Hent og valider starttidspunkt 
        start_time = None 
        while start_time is None: 
            time_input = input("Vennligst oppgi et klokkeslett for når forelesningen starter (TT:MM): ") 
            try: 
                # Gjør om streng til datetime, og hent deretter ut time-objektet 
                start_time = datetime.strptime(time_input, "%H:%M").time() 
            except ValueError: 
                print("Beklager, ugyldig klokkeslett eller format. Vennligst bruk TT:MM (f.eks. 10:15 eller 14:00).\n") 
 
        # 2. Hent og valider varighet (må være et positivt heltall) 
        duration = None 
        while duration is None: 
            duration_input = input("Vennligst oppgi varighet i minutter (positivt heltall): ") 
            if duration_input.isdigit() and int(duration_input) > 0: 
                duration = int(duration_input) 
            else: 
                print("Beklager, varigheten må være et heltall større enn 0. Prøv igjen.\n") 
 
        # 3. Beregn sluttid og vis resultatet 
        end_time = start_end(start_time, duration) 
        print(f"Studieøkten starter {start_time.strftime('%H:%M')} og avsluttes kl. {end_time}\n") 
  

 

Oppsummering av formateringskoder i datetime 

Kode 
	

Betydning 
	

Eksempel 

%d 
	

Dag i måneden (01–31) 
	

26 

%m 
	

Måned som tall (01–12) 
	

06 

%Y 
	

Årstall med fire siffer 
	

1998 

%H 
	

Time i 24-timers format (00–23) 
	

13 

%M 
	

Minutt (00–59) 
	

45 

%S 
	

Sekund (00–59) 
	

00 

Ved å bruke dette mønsteret oppnår du full kontroll på feilhåndtering, oppfyller kravene i oppgaven optimalt, og unngår unødig tidsbruk på formatfeil.

 











