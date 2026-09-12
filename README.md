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









