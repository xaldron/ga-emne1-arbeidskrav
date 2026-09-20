# Arbeidskrav 1 – Jøran Tvedt

## Introduksjon

Hei!

Mitt navn er Jøran Tvedt. Jeg er student på Backend-programmering ved Gokstad Akademiet, og dette er mitt første arbeidskrav på studiet.

Jeg har lært en del grunnleggende Python på egenhånd gjennom følgende kurs på Udemy:
- Kurslenke: [Complete Python Bootcamp](https://www.udemy.com/course/complete-python-bootcamp/?couponCode=MT260907G2)
- Kursmateriell / referanserepo: [Complete Python Bootcamp Repo](https://www.udemy.com/course/complete-python-bootcamp/?couponCode=MT260907G2)

Jeg bruker kursmateriellet som kilde og referanse til studiet nå i dag. 

### Holdning til bruk av kunstig intelligens (KI)
Siden jeg har gjort dette kurset før, går jeg inn med en innstilling om å bruke minst mulig KI. Jeg har en ambisjon om å minimum løse oppgave 1 helt uten hjelp av KI. Jeg liker godt å finne ut ting selv, som for eksempel å bruke kilder som W3Schools og undersøke tilgjengelige metoder for ulike datatyper når jeg skal løse en kodeoppgave.

Når jeg må ty til KI for å finne ut av ting, benytter jeg i hovedsak den innebygde modellen «Junie» i PyCharm. Det har noen klare fordeler, som at KI-en kan lese koden direkte i editoren uten behov for manuell kopiering frem og tilbake, og gir konsise svar uten unødvendige eksterne lenker.

Helt til slutt i arbeidet har jeg også benyttet Junie til å rydde, formatere og strukturere denne `README.md`-filen, slik at dokumentet fremstår ryddig og oversiktlig for sensor. Dette er dokumentert i en egen seksjon nederst.

---

## Oppgave 1

Her har jeg lykkes med ambisjonen min om å ikke bruke KI i løsningen. 

Jeg kan heller ikke se at det kommer frem av arbeidskravet at det kreves spesifikke refleksjoner eller begrunnelser rundt denne oppgaven her i README.

---

## Oppgave 2: Studieøkter

### Valg av datastruktur og refleksjon
I denne oppgaven blir jeg innledningsvis bedt om *"en list som inneholder elementer av typen dict eller tuple."*

Jeg valgte å benytte en **`list` med `dict` (ordbøker)** til denne oppgaven:
1. **Mutabilitet:** Tuples er *immutable* (uforanderlige) i Python. Da jeg ikke var helt sikker på om jeg ville komme til å skrive kode som skulle gjøre endringer underveis, så jeg for meg at tupler kunne by på upraktiske utfordringer.
2. **Nøkkel/verdi-par:** Dictionaries med sine *key/value pairs* egner seg naturlig for å representere en studieøkt med felter som `topic`, `duration_minutes` og `status`.
3. **Læringsutbytte:** Man kan bruke *tuple unpacking* (`.items()`) for å hente ut nøkler og verdier fra dictionaries. Da jeg ikke har brukt dictionaries så mye tidligere, ga dette god trening i å navigere og hente ut elementer fra ordbøker nøstet i en liste.

### Eksterne kilder
Jeg benyttet bevisst søkestrengen med `-ai` for å finne ordinære kilder på nett:
- **Google-søk:** `"how to sort a list of dictionaries in python -ai"`
- **Kilde benyttet:** [Python: Grouping & Sorting List of Dictionaries (Medium)](https://medium.com/@aayushiagarwal1999/python-grouping-sorting-list-of-dictionaries-3a82747fb09c)

### Dokumentasjon av KI-bruk

<details>
<summary><b>1) Feilmelding: ValueError: too many values to unpack</b></summary>

**Prompt:**
```text
Traceback (most recent call last):
  File "C:\Users\Studier\PycharmProjects\GA\Emne1\ga-emne1-arbeidskrav\oppgave-2.py", line 59, in <module>
    display_sessions()
  File "C:\Users\Studier\PycharmProjects\GA\Emne1\ga-emne1-arbeidskrav\oppgave-2.py", line 55, in display_sessions
    for k,v in dicts:
ValueError: too many values to unpack (expected 2)

Kva betyr denne feilmeldinga?
```

**Svar:**
> **Forklaring på feilmeldinga:**
> Feilmeldinga `ValueError: too many values to unpack (expected 2)` oppstår på linje 55:
> ```python
> for k, v in dicts:
> ```
> **Kvifor skjer dette?** Når du itererer over ei ordbok (dictionary) direkte i Python med `for ... in dicts:`, itererer Python berre over nøklane (keys), ikkje både nøklar og verdiar. Nøklane i ordbøkene dine er strenger som `"topic"`, `"duration_minutes"` og `"status"`. Når du skriv `for k, v in dicts:`, prøver Python å pakke ut kvar enkelt nøkkelstreng inn i to variablar (`k` og `v`). Sidan strengen `"topic"` har 5 teikn, har strengen fleire enn dei 2 verdiane Python forventar – derav feilmeldinga.
>
> **Korleis fikse det?**
> For å iterere over både nøklar og verdiar i ei ordbok, må du bruke metoden `.items()`:
> ```python
> def display_sessions():
>     if study_sessions == []:
>         print('Beklager. Det finnes ingen studieøkter registrert ennå.')
>     else:
>         for dicts in study_sessions:
>             for k, v in dicts.items():
>                 print(k, v)
>             print('\n')
> ```
> Ved å bruke `dicts.items()` returnerer Python par med `(nøkkel, verdi)`, som trygt kan pakkast ut i `k` og `v`.
</details>

<details>
<summary><b>2) Feilsøking i display_completed()</b></summary>

**Prompt:**
```python
def display_completed():
    for dicts in study_sessions:
        for k in dicts.items():
            if k["status"] == "complete":
                print(k)

display_completed()
```
*"Kvifor funker ikkje dette? Eg har prøvd litt ulike variantar for å få det til. Eg reiknar med du skjønar kva eg prøver på?"*

**Svar:**
> **Kvifor koden ikkje fungerer:**
> 1. **Bruk av `dicts.items()` i ei indre løkke:** Variabelen `dicts` er allereie ei ordbok frå lista `study_sessions`. Når du gjer `for k in dicts.items():`, blir `k` eit tuppel med eit nøkkel-verdi-par (t.d. `('topic', 'Operators')`). Når du deretter prøver `k["status"]`, får du ein `TypeError` (tuple indices must be integers or slices, not str).
> 2. **Statusverdien:** I `study_sessions` er statusen sett til `"completed"`, medan du i if-vilkåret sjekkar mot `"complete"`.
>
> **Korleis løyse det:**
> ```python
> # 1. Enkel variant:
> def display_completed():
>     for session in study_sessions:
>         if session["status"] == "completed":
>             print(session)
>
> # 2. Formatert variant:
> def display_completed():
>     completed_sessions = [s for s in study_sessions if s["status"] == "completed"]
>     if not completed_sessions:
>         print("Ingen fullførte studieøkter funne.")
>         return
>     for session in completed_sessions:
>         print("")
>         for k, v in session.items():
>             print(k.capitalize() + ":", v)
> ```
</details>

<details>
<summary><b>3) UnboundLocalError og parameterstyring i choose_program()</b></summary>

**Prompt:**
```text
"Kvifor får eg opp denna feilmeldinga når study_sessions er global?"

Traceback (most recent call last):
  File "C:\Users\Studier\PycharmProjects\GA\Emne1\ga-emne1-arbeidskrav\oppgave-2.py", line 157, in <module>
    choose_program()
  File "C:\Users\Studier\PycharmProjects\GA\Emne1\ga-emne1-arbeidskrav\oppgave-2.py", line 143, in choose_program
    study_sessions.append(register_session())
UnboundLocalError: cannot access local variable 'study_sessions' where it is not associated with a value
```

**Svar:**
> **Kvifor oppstår feilen?** Linje 151 inneheld `study_sessions = sort_duration()`. Når ein variabel blir tilordna med `=` ein stad inne i ein funksjon, reknar Python den automatisk som ein lokal variabel for heile funksjonen.
> - **Løysing 1:** Bruke `global study_sessions`.
> - **Løysing 2:** Sortere lista på staden med `.sort()`.

**Oppfølgingsprompt:**
> *«Eg fann ei bedre løysing, som var å gje `choose_program` eit argument, og deretter bytta ut variabelen `study_session` med `dict_list`, for så endre elif statement til det samme og putte `study_session` som argument når eg køyrer `choose_program`»*

**Svar:**
> **God tilnærming med argument og parametrar!** Å sende inn lista som eit argument (`dict_list`) til funksjonar er god programmeringspraksis som gjer koden modulær og uavhengig av globale variablar.
> - Pass på at også `display_completed()`, `search_topic()` og `display_duration_completed()` oppdaterast til å ta imot `dict_list`.
</details>

---

## Oppgave 3: Datoberegninger

### Refleksjon og valg av bibliotek
I denne oppgaven er jeg bedt om å dokumentere minst 6 gyldige og ugyldige testtilfeller, i tillegg til all dokumentasjon på KI-bruk.

Den offisielle `datetime`-modulen fremsto som det opplagte valget. Jeg har hørt om modulen før, men aldri brukt den. Jeg oppdaget derfor tidlig at jeg hadde behov for litt KI-hjelp med å forstå dokumentasjonen, ettersom standarddokumentasjonen oppleves veldig teknisk.

### Testtilfeller

| Funksjon / Menyvalg | Type test | Inndata (Input) | Forventet resultat | Faktisk resultat |
| :--- | :--- | :--- | :--- | :--- |
| `add_date` (valg 1) | **Ugyldig** | `26/06-98` | Fanges opp av feilhåndtering, gir feilmelding om feil format. | Fanges opp av `except ValueError`, printer tilbakemelding til bruker. |
| `add_date` (valg 1) | **Gyldig** | `26.06.1998` | Returnerer et gyldig `date`-objekt og lagres i listen. | Funksjonen returnerer datoverdi som forventet og legger til i listen. |
| `start_end` (valg 3) | **Gyldig** | `1:30` + `13` minutter | Beregner sluttid til `01:43`. | Registreres som kl. 01:30 og avsluttes 01:43. |
| `start_end` (valg 3) | **Ugyldig** | `Halv to` | Fanges opp av feilhåndtering da det ikke er klokkeslett. | Fanges opp av `except ValueError`, ber brukeren prøve på nytt. |
| `start_end` (valg 3) | **Ugyldig** | `24:30` | Fanges opp som ugyldig timeverdi (timer må være 00–23). | Fanges opp av `except ValueError`, gir feilmelding. |
| `days_between` (valg 4) | **Gyldig** | `19.09.2026`, `15.09.2026` | Returnerer 4 dager (positivt tall). | `abs()` sørger for at differansen forblir positiv (4 dager). |
| `days_between` (valg 4) | **Ugyldig** | `31.02.2026` | Fanges opp som en ikke-eksisterende dato. | Fanges opp av `except`, gir beskjed om ugyldig dato. |
| `add_date` (valg 1) | **Gyldig** | `16.10.2026` | Legges til i listen for videre testing. | Lagt til i listen. |
| `add_date` (valg 1) | **Gyldig** | `25.04.2057` | Legges til frem i tid for å teste sortering. | Lagt til i listen. |
| `list_of_dates_sorted` (valg 2) | **Gyldig** | Liste med registrerte datoer | Skriver ut datoene i kronologisk rekkefølge. | Output sorterer datoene riktig. |
| `list_of_dates_sorted` (valg 2) | **Ugyldig / Tom** | Kjører funksjonen med tom liste | Håndterer tom liste uten å krasje. | Returnerer tom liste uten feilmelding (kan forbedres med infomelding). |

### Eksterne kilder
- **Google-søk:** `"is python time class not compatible with timedelta? -ai"`
- **Kilde benyttet:** [Python time timedelta equivalent (StackOverflow)](https://stackoverflow.com/questions/656297/python-time-timedelta-equivalent)

### Dokumentasjon av KI-bruk

<details>
<summary><b>1) Forståelse av strptime() fra dokumentasjonen</b></summary>

**Prompt:**
> *Oppgåva seier blant anna at eg skal ha "en funksjon som tar imot en dato på formatet dd.mm.åååå og returnerer en datoverdi når teksten er gyldig". Forstår eg denne delen av python-dokumentasjonen rett, at eg kan be om input av det formatet og så gir python error om input ikkje er lik formatet?*
> *(Viser til `date.strptime(date_string, format)` i docs)*

**Svar:**
> Ja – du bruker `input()` først, og så prøver du å tolke teksten med `datetime.strptime(tekst, "%d.%m.%Y")`:
> - `%d` = to-sifret dag, `%m` = to-sifret måned, `%Y` = fire-sifret år.
> - Dersom teksten ikke matcher eller er ugyldig (f.eks. `31.02.2026`), kastes en `ValueError` som fanges opp i `try/except`.
</details>

<details>
<summary><b>2) Klokkeslett i retur fra days_between()</b></summary>

**Prompt:**
```python
one_date = date(1998, 6, 26) 
another_date = date(1990, 12, 18) 
 
def days_between(date_1, date_2): 
    '''Take inn two dates and return (positive) days between them''' 
    return abs(date_1 - date_2) 
 
gimme_days = days_between(another_date, one_date) 
print(gimme_days)
```
*"Kvifor får eg eit klokkeslett med på return her, når eg berre bruker date som ikkje skal ha med klokka? Eg vil berre ha antall dagar mellom datoane."*

**Svar:**
> Subtraksjon av to `date`-objekter gir et `timedelta`-objekt. Standard strengrepresentasjon er `X days, HH:MM:SS`. For å hente kun tallet på dager bruker du `.days`-attributtet:
> ```python
> def days_between(date_1, date_2): 
>     return abs((date_1 - date_2).days)
> ```
</details>

<details>
<summary><b>3) Strukturering av testtilfeller</b></summary>

**Prompt:**
> *«Det gikk ikke helt. Tingen er at jeg i følge arbeidskravet skal "Dokumentere minst seks gyldige og ugyldige testtilfeller". Nå så jeg det litt sent, og har ingen logg fra når jeg har forsøkt å kjøre koden underveis.»*

**Svar:**
> Det gjør ingenting at du ikke har historiske logger. Kravet innebærer at du setter opp en tabell med planlagte testtilfeller (funksjon, testtype, input, forventet og faktisk resultat) og tester koden din strukturert.
> 
> *Tips til `add_date`:* `strptime` ligger under `datetime.strptime`, så husk å kalle `.date()` på resultatet for å få et `date`-objekt.
</details>

<details>
<summary><b>4) Feilsøking i menyvalg 4 og menyvalg 3</b></summary>

**Prompt 1 (Menyvalg 4):**
> *«Hvorfor fungerer ikke valg 4 slik det står nå? `if one_date or another_date != type(datetime.date):` slår alltid til.»*

**Svar:**
> `one_date` evalueres uavhengig på venstresiden av `or` og er «truthy», og `type(datetime.date)` returnerer typen `<class 'type'>`. Sjekk heller om variablene er `None`:
> ```python
> if not one_date or not another_date:
> ```

**Prompt 2 (Menyvalg 3):**
> *«Prøver å få til ei løysing på menyvalg 3, med bruk av strptime. Men det funker ikkje og eg tykkjer dokumentasjonen er heilt håplaus å skjøne.»*

**Svar:**
> Bruk formateringskoden `"%H:%M"` (ikke `"%HH:%MM"`), og gjør om streng til `time`-objekt via:
> ```python
> start_time = datetime.strptime(time_input, "%H:%M").time()
> ```
> Valider varigheten med `.isdigit()` og beregn sluttiden med `start_end(start_time, duration)`.
</details>

---

## Oppgave 4: Analyse av supporthenvendelser

### Eksterne kilder og arkitekturvalg
- **Kilde benyttet:** Tips fra medstudent på Discord om CSV-lesing: [Reading CSV files in Python (GeeksforGeeks)](https://www.geeksforgeeks.org/pandas/reading-csv-files-in-python/)

### Refleksjon rundt oppgaveløsning
Til å begynne med lagde jeg funksjoner for hver deloppgave under 4.2 som lignet veldig på funksjonen i oppgave 4.1. Jeg innså etter hvert at dette ble veldig repeterende. Jeg spurte KI om det ville være lurt å lage en felles funksjon som returnerte alle gyldige rader. KI bekreftet at dette var god praksis (DRY-prinsippet) og kom med forslag til omskrivninger. 

For å holde koden ryddig og modulær delte jeg oppgaven inn i to filer:
- `oppgave_4_helpers.py`: Inneholder alle hjelpefunksjoner, validering og beregningslogikk.
- `oppgave_4_program.py`: Kjører hovedflyten, genererer rapporten og skriver til `data/support-rapport.txt`.

*Merk:* Funksjonene `most_tickets()` og `unsolved_tickets_sorted()` har jeg skrevet selv.

---

### Oppgave 4.4: Feilretting og forklaringer

Her er en oversikt over feilene funnet i den opprinnelige koden og hvordan de ble rettet:

1. **Syntaks i funksjonsdefinisjon (parentes):** Lukket den manglende parentesen for parameterlisten.
2. **Type hints:** Undersøkte parameteren `requests: list[dict[str, str | int]]`. KI forklarte at dette er *type hints* som beskriver at funksjonen forventer en liste med ordbøker.
3. **Returtype-syntaks:** Endret syntax-feilen `>` til `-> int` for returtypen.
4. **Variabelnavn i return:** Endret `return total_minutes` til `return total`, slik at det matcher det lokale variabelnavnet.
5. **Sammenligningsoperator:** Endret tilordningsoperatoren `=` til sammenligningsoperatoren `==` i `if request["is_resolved"] == "yes":`.
6. **Akkumulering av sum:** Endret `total = request["minutes"]` til `total += ...` slik at minuttene summeres løpende i stedet for å overskrives.
7. **Type-konvertering (casting):** Konverterte `request["minutes"]` fra tekst til heiltall med `int(request["minutes"])`.
8. **Målrettet unntakshåndtering for konvertering:** La til `try/except (ValueError, TypeError)` rundt `int()`-konverteringen inni løkken for å håndtere uventede verdier uten å krasje.
9. **Målrettet unntakshåndtering for filfeil:** La til `try/except FileNotFoundError` rundt datainnhentingen og funksjonskjøringen i hovedprogrammet.

---

### Dokumentasjon av KI-bruk (Oppgave 4)

<details>
<summary><b>1) Avrunding og formatering av snittid</b></summary>

**Prompt:**
> *«Korleis korter eg ned snitttida ned til ein desimal, slik eg prøver på her?»*

**Svar:**
> Syntaksen `total_minutes/counter:.1f` gir `SyntaxError` utenfor f-strings.
> - For tallverdier til videre beregninger: Bruk `round(total_minutes / counter, 1)`.
> - For strengvisning: Bruk `f"{total_minutes / counter:.1f}"`.
</details>

<details>
<summary><b>2) Refaktorering til felles get_valid_tickets()-funksjon</b></summary>

**Prompt:**
> *«Er det slik at eg burde/kunne ha laga ein funksjon/brukt valid_ticket_count som returnerer kun dei gyldige radene i fila, og deretter bruk denne funksjonen som parameter/argument i dei andre?»*

**Svar:**
> Ja, dette følger **DRY** (*Don't Repeat Yourself*) og **Single Responsibility Principle**. CSV-filen leses én gang via `get_valid_tickets()`, og listen sendes inn til analysefunksjonene (`ticket_per_category`, `ticket_time_spent`, `tickets_solved_unsolved`).

**Subprompt (Forklaring på generatoruttrykk):**
> *«Kan du bryte ned `solved = sum(1 for row in tickets if row["is_resolved"] == "yes")`? Hva representerer 1-tallet?»*
>
> *Forklaring:* For hver rad som matcher `if`-kravet produseres tallet `1`, og `sum()` legger sammen alle 1-tallene. Dette tilsvarer `solved += 1` i en vanlig for-løkke, men er mer konsist og minneeffektivt.
</details>

<details>
<summary><b>3) Formatering av rapport til tekstfil</b></summary>

**Prompt:**
> *«Oppgaven sier 'og skrive de beregnede analyseresultatene til filen med tydelige overskrifter.' Hvordan skriver jeg tydelige overskrifter i en tekstfil?»*

**Svar:**
> I rene `.txt`-filer lages overskrifter ved hjelp av linjeskift (`\n`), understreking med tegn (`===` eller `---`) og luft mellom seksjoner. Alle tegn må ligge inni tekststrengene i `file.write()`.
</details>

<details>
<summary><b>4) Målrettet try/except og type hints</b></summary>

**Prompt 1 (Unntakshåndtering):**
> *«Kvar skal try/except vere? Kva meiner dei med målretta try/except?»*
>
> *Forklaring:* Unntakshåndtering plasseres tett på den risikofylte operasjonen. Bruk `except ValueError:` ved konvertering av `int(request["minutes"])` inne i funksjonen, og `except FileNotFoundError:` rundt filinnlesingen.

**Prompt 2 (Type hints):**
> *«requests: list[dict[str, str | int]]) -> int – Er dette berre eit tulleargument?»*
>
> *Forklaring:* Dette er standard *type hints* i Python. Det angir at parameteren forventer en liste med ordbøker der nøklene er strenger og verdiene er streng eller tall, og at funksjonen returnerer et heltall (`int`).
</details>

---

## Dokumentasjon av KI til opprydding og strukturering av README

Til slutt benyttet jeg KI (Junie) til å rydde opp, strukturere og formatere hele denne `README.md`-filen, da den opprinnelig fremsto uoversiktlig med mange råutskrifter og lange samtalelogger. 

Her er dialogen og forespørselen som ble brukt for å utføre denne oppryddingen:

<details>
<summary><b>1) Forespørsel om opprydding og plan for struktur</b></summary>

**Prompt:**
> *«Ikke gjør noe endå, svar bare på spørsmålet: Kan du rydde og fikse readme så den blir mer oversiktlig og lesbar? Fremstår veldig rotete per nå»*

**Svar (oppsummering av foreslått plan):**
> KI foreslo å beholde alt eksisterende innhold, refleksjoner, kilder og oppgavelogikk 100 % intakt, men forbedre strukturen ved å:
> 1. Etablere et tydelig Markdown-hierarki (`### Oppgave 1`, `### Oppgave 2` osv.).
> 2. Legge lange samtale- og feillogger inn i nedtrekkbare `<details>`-bokser for å gjøre dokumentet kompakt og lettlest for sensor.
> 3. Formatere testtabeller og feilrettingslister til ryddig Markdown, samt fjerne unødvendig formateringsstøy (som rømte tegn og doble linjeskift).
</details>

<details>
<summary><b>2) Gjennomføring av oppryddingen</b></summary>

**Prompt:**
> *«Takk. Måtte bare commite hele sulamitten først nå, slik at jeg har en backup om oppryddingen din slår feil ut. ;) Da kan du kjøre en opprydding av readme!»*

**Handling / Resultat:**
> KI utførte oppryddingen etter den avtalte planen:
> - Omstrukturerte `README.md` med rene overskrifter, tabeller og nedtrekkbare bokser.
> - Alle opprinnelige tekster, refleksjoner, testtilfeller og KI-logger ble bevart.
</details>
