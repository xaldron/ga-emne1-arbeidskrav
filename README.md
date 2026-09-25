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
> 
> **Kvifor skjer dette?**
> Når du itererer over ei ordbok (dictionary) direkte i Python med `for ... in dicts:`, itererer Python berre over nøklane (keys), ikkje både nøklar og verdiar. Nøklane i ordbøkene dine er strenger som `"topic"`, `"duration_minutes"` og `"status"`. 
> 
> Når du skriv `for k, v in dicts:`, prøver Python å pakke ut kvar enkelt nøkkelstreng inn i to variablar (`k` og `v`). Sidan strengen `"topic"` har 5 teikn, har strengen fleire enn dei 2 verdiane Python forventar – derav feilmeldinga.
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
> 1. **Bruk av `dicts.items()` i ei indre løkke:** Variabelen `dicts` er allereie ei ordbok frå lista `study_sessions`. Når du gjer `for k in dicts.items():`, blir `k` eit tuppel med eit nøkkel-verdi-par (t.d. `('topic', 'Operators')`). Når du deretter prøver `k["status"]`, får du ein `TypeError` (*tuple indices must be integers or slices, not str*).
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
> **Kvifor oppstår feilen?** Linje 151 inneheld `study_sessions = sort_duration()`. Når ein variabel blir tilordna med `=` ein stad inne i ein funksjon, reknar Python den automatisk som ein lokal variabel for heile funksjonen. Sidan du refererer til `study_sessions.append(...)` *før* denne linja blir nådd, veit ikkje Python kva lokal verdi den skal referere til.
> - **Løysing 1:** Bruke `global study_sessions` øvst i funksjonen.
> - **Løysing 2:** Sortere lista på staden med `.sort()` i staden for ny tilordning.

**Oppfølgingsprompt:**
> *«Eg fann ei bedre løysing, som var å gje `choose_program` eit argument, og deretter bytta ut variabelen `study_session` med `dict_list`, for så endre elif statement til det samme og putte `study_session` som argument når eg køyrer `choose_program`»*

**Svar:**
> **God tilnærming med argument og parametrar!** Å sende inn lista som eit argument (`dict_list`) til funksjonar er god programmeringspraksis som gjer koden modulær og uavhengig av globale variablar.
> - Pass på at også dei andre funksjonane (`display_completed()`, `search_topic()` og `display_duration_completed()`) oppdaterast til å ta imot `dict_list`.
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
> Ja — nesten, og du er inne på akkurat rett spor. Det er ein viktig liten nyanse.
>
> `date.strptime()` gjer ikkje sjølv input-funksjonen. Du kan først få inn tekst med `input()`, og så prøve å tolke teksten som ein dato:
>
> ```python
> tekst = input("Skriv inn dato (dd.mm.åååå): ")
> dato = date.strptime(tekst, "%d.%m.%Y")
> ```
>
> Her betyr:
> - `"%d"` → dag med to siffer
> - `"%m"` → månad med to siffer
> - `"%Y"` → år med fire siffer
>
> Så dersom brukaren skriv:
> `15.09.2026`
> blir dato ein faktisk `date`-verdi.
>
> Men dersom brukaren skriv noko som ikkje kan tolkast etter formatet, vil Python normalt gi:
> `ValueError`
>
> For eksempel:
> `15-09-2026`
> eller:
> `15.9.2026`
> kan føre til `ValueError` fordi teksten ikkje passar formatet du oppgav.
>
> Og dette er sannsynlegvis sjølve poenget med oppgåva: Du skal lage ein funksjon som prøver dette, og handtere situasjonen der brukaren skriv noko ugyldig.
>
> Dokumentasjonen seier altså i praksis:
> *«Prøv å tolke denne teksten som ein dato etter dette mønsteret. Klarer eg det ikkje, kastar eg ValueError.»*
>
> Det fine er at dokumentasjonen faktisk fortel deg akkurat kva verktøy du treng. Du treng ikkje finne opp ein masse manuell kontroll av om teikn 3 er ".", om teikn 6 er ".", om månaden er mellom 1 og 12 osv. 😄
>
> Og ein liten ting å vere obs på: `strptime()` kan òg avsløre semantisk ugyldige datoar, ikkje berre feil skiljeteikn. `31.02.2026` er til dømes ikkje ein gyldig dato og vil derfor også utløyse `ValueError`.
>
> Så eg ville lese oppgåveteksten som:
> tekst → prøv `strptime()` → gyldig? returner `date` → ugyldig? handter `ValueError`.
>
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
<summary><b>1) Avrunding, formatering og tuple return i ticket_time_spent()</b></summary>

**Prompt:**
> *«Korleis korter eg ned snitttida ned til ein desimal, slik eg prøver på her?»*

**Svar:**
> Syntaksen `total_minutes/counter:.1f` fører til ein `SyntaxError` fordi formatspesifikasjonen `:.1f` berre er gyldig inni formaterte strengar (f-strings), og ikkje direkte i numeriske uttrykk eller tuplar.
>
> **1. Avrunding som tal (`float`) – Best for vidare utrekningar:**
> ```python
> avg_minutes = round(total_minutes / counter, 1)
> return (total_minutes, avg_minutes)
> ```
>
> **2. Formatering som streng (`str`) – Best for visning:**
> ```python
> avg_minutes = f"{total_minutes / counter:.1f}"
> return (total_minutes, avg_minutes)
> ```
>
> **Optimalisert funksjon med feilhandtering mot divisjon med null:**
> ```python
> def ticket_time_spent():
>     with open(file_path, "r", encoding="utf-8") as file:
>         content = csv.DictReader(file)
>         total_minutes = 0
>         counter = 0
>         for row in content:
>             if "" in row.values():
>                 continue
>             elif int(row['id']) < 1:
>                 continue
>             elif not row['minutes'].isdigit() or int(row['minutes']) < 0:
>                 continue
>             elif row['is_resolved'] != "yes" and row['is_resolved'] != "no":
>                 continue
>             else:
>                 counter += 1
>                 total_minutes += int(row['minutes'])
>         
>         if counter == 0:
>             return (0, 0.0)
>             
>         return (total_minutes, round(total_minutes / counter, 1))
> ```

**Oppfølgingsprompt:**
> *«Oppgåva ba meg om "samlet og gjennomsnittlig tidsbruk, med gjennomsnitt til én desimal", har eg tenkt rett i å returnere dei to verdiane i ein tuple, siden det ikkje går an å returnere enkeltverdiar fleira gonger? Tanken er tuple unpacking seinere i koden når verdiane skal nyttast/visast»*

**Svar:**
> Ja, du har **heilt rett!** Å returnere fleire verdiar samla i ein **tuple** og deretter bruke **tuple unpacking** er den standard og mest vanlege måten å sende og ta imot fleire verdiar frå ein funksjon på i Python:
> ```python
> total, avg = ticket_time_spent(valid_tickets)
> ```
</details>

<details>
<summary><b>2) Refaktorering til felles get_valid_tickets() og analysefunksjoner</b></summary>

**Prompt:**
> *«hmmm, er det slik at eg burde/kunne ha laga ein funksjon/brukt valid_ticket_count som returnerer kun dei gyldige radene i fila, og deretter bruk denne funksjonen som parameter/argument i dei andre ( i staden for samme ifs og elifs i kvar funksjon)? Eller er det greit slik det står no?»*

**Svar:**
> Ja, det er ein **svært god idé!** Dette følger **DRY-prinsippet** (*Don't Repeat Yourself*) og **Single Responsibility Principle**.
>
> **1. Ein funksjon som hentar og returnerer gyldige saker:**
> ```python
> def get_valid_tickets():
>     valid_rows = []
>     with open(file_path, "r", encoding="utf-8") as file:
>         content = csv.DictReader(file)
>         for row in content:
>             if "" in row.values():
>                 continue
>             elif int(row['id']) < 1:
>                 continue
>             elif not row['minutes'].isdigit() or int(row['minutes']) < 0:
>                 continue
>             elif row['is_resolved'] not in ("yes", "no"):
>                 continue
>             else:
>                 valid_rows.append(row)
>     return valid_rows
> ```
>
> **2. Sende dei gyldige radene inn som argument til dei andre funksjonane:**
> ```python
> def ticket_per_category(tickets):
>     categories = [row["category"] for row in tickets]
>     return Counter(categories)
>
> def ticket_time_spent(tickets):
>     if not tickets:
>         return (0, 0.0)
>     total_minutes = sum(int(row["minutes"]) for row in tickets)
>     avg_minutes = round(total_minutes / len(tickets), 1)
>     return total_minutes, avg_minutes
>
> def tickets_solved_unsolved(tickets):
>     solved = sum(1 for row in tickets if row["is_resolved"] == "yes")
>     unsolved = len(tickets) - solved
>     return solved, unsolved
> ```
>
> **3. Køyring:**
> ```python
> valid_tickets = get_valid_tickets()
> print(f"Tal på gyldige saker: {len(valid_tickets)}")
> print(f"Tidsbruk: {ticket_time_spent(valid_tickets)}")
> print(f"Kategoriar: {ticket_per_category(valid_tickets)}")
> print(f"Løyst / uløyst: {tickets_solved_unsolved(valid_tickets)}")
> ```

**Oppfølgingsprompt:**
> *«kan du bryte ned denne for meg som du skrev? Skjønner for eksmepel ikke helt hva 1 representerer. Er det litt det samme som += 1 om det hadde vært i en løkke? `solved = sum(1 for row in tickets if row["is_resolved"] == "yes")`»*

**Svar:**
> Ja, du har **heilt rett!** Det er i praksis nøyaktig det same som å gjere `solved += 1` inni ei vanleg for-løkke.
> - `for row in tickets`: Går gjennom kvar henvendelse i lista `tickets`.
> - `if row["is_resolved"] == "yes"`: Sjekkar om henvendelsen er markert som løyst.
> - `1`: For kvar rad som oppfyller kravet, genererer uttrykket talet `1`.
> - `sum(...)`: Tek imot alle `1`-tala og legg dei saman.
>
> Tilsvarande tradisjonell løkke:
> ```python
> solved = 0
> for row in tickets:
>     if row["is_resolved"] == "yes":
>         solved += 1
> ```
</details>

<details>
<summary><b>3) Rapportskriving til tekstfil, overskrifter og Counter.most_common()</b></summary>

**Prompt 1 (Overskrifter og formatering i .txt):**
> *«Oppgaven sier "og skrive de beregnede analyseresultatene til filen med tydelige overskrifter." Hvordan skriver jeg tydelige overskrifter? Jeg fant en kilde på nett som sa bruk av likhetstegn mellom overskriftene, men det så ikke helt riktig ut ;P»*

**Svar:**
> I ei tekstfil må teikna stå inni strengen (t.d. `file.write("=== RAPPORT ===\n")`). Bruk understreking med teikn (`===` eller `---`) og linjeskift (`\n`) for å skape luft mellom seksjonane:
> ```text
> RAPPORT FOR SUPPORTHENVENDELSER
> ===============================
> 
> Samla tidsbruk: 120 minutt
> Gjennomsnittleg tidsbruk: 15.5 minutt
> ```

**Prompt 2 (Skriving inni éin with open):**
> *«Er det best å skrive heile rapporten innafor samme with open eg har byrja på, med ny file.write() for kvar gang eg legg noko til?»*

**Svar:**
> Ja, det er **heilt rett og best praksis** å halde all skrivinga samla inni den eine `with open(..., "w", ...)`-blokka for å unngå at fila blir overskrive eller opna unødvendig fleire gonger.

**Prompt 3 (Utskrift av kategorier og Counter.most_common):**
> *«Både highest_category og categories er eg ikkje heilt nøgd med at den printer den i dictformat. Korleis kan eg printe ut berre dei relevante verdiane? Altså noko slik som "kategorien med flest henvendelser er "utstyr" med 5 henvendelser" i stadenfor "{utstyr: 5}"?»*

**Svar:**
> **1. Hente ut toppkategori:**
> ```python
> top_category, top_count = highest_category
> file.write(f"Kategorien med flest henvendelser er '{top_category}' med {top_count} henvendelser.\n")
> ```
> 
> *Viktig om `most_tickets()`:* Standard `max(categories.items())` samanliknar alfabetisk på kategorinamnet. Bruk heller `Counter.most_common(1)[0]`:
> ```python
> def most_tickets(categories):
>     return categories.most_common(1)[0]
> ```
> 
> **2. Skrive ut alle kategoriar med løkke:**
> ```python
> for kategori, antall in categories.items():
>     file.write(f"  - {kategori}: {antall} henvendelser\n")
> ```

**Prompt 4 (Forklaring på most_common(1)[0]):**
> *«Kva representerer (1) og [0] her då?»*

**Svar:**
> - `(1)`: `most_common(1)` returnerer ei liste med det **1** mest vanlege elementet: `[('utstyr', 5)]`.
> - `[0]`: Hentar ut det første elementet frå lista, slik at du sit att med sjølve tuppelet `('utstyr', 5)`.
</details>

<details>
<summary><b>4) Oppgave 4.4: Målrettet try/except og feilretting</b></summary>

**Prompt 1 (Målrettet try/except):**
> *«Kva meiner dei med å bruke "målrettet" try/except? Kvar skal try/except vere?»*

**Svar:**
> Med eit «målretta» unntak meiner ein at du eksplisitt oppgir **kva type feil** koden skal fange opp, i staden for ein tom/brei `except:` som skjuler alle feil:
> 1. **Konverteringsfeil (inne i funksjonen / løkka):** 
>    `int(request["minutes"])` kan kaste `ValueError` dersom verdien er ugyldig tekst.
>    ```python
>    for request in requests:
>        if request["is_resolved"] == "yes":
>            try:
>                total += int(request["minutes"])
>            except (ValueError, TypeError):
>                continue
>    ```
> 2. **Filfeil (der fila vert opna/henta):** 
>    Bruk `try/except FileNotFoundError:` rundt filkall i hovudprogrammet.

**Prompt 2 (Type hints):**
> *«requests: list[dict[str, str | int]]) -> int – Er dette berre eit tulleargument, eller kan argument i ein funksjon sjå slik ut?»*

**Svar:**
> Nei, dette er **type hints** (typeannonseringar):
> - `requests:` Variabelnamnet.
> - `list[dict[str, str | int]]`: Parameteren forventar ei liste (`list`) der kvart element er ei ordbok (`dict`) med streng-nøklar og verdiar av typen streng eller heiltal.
> - `-> int:` Angir at funksjonen returnerer eit heiltall (`int`).

**Prompt 3 (TypeError i except):**
> *«Kva er det TypeError skal fange opp då, siden du foreslår den i samme except?»*

**Svar:**
> - `ValueError` oppstår når typen er streng, men innhaldet ikkje er tal (f.eks. `int("ugyldig")`).
> - `TypeError` oppstår dersom verdien ikkje er ein streng eller eit tal i det heile, for eksempel `int(None)`.
</details>

---

## Oppgave 5

Dokumentasjon/kilder brukt: 
https://docs.python.org/3/library/csv.html








### Dokumentasjon av KI-bruk (Oppgave 5)


<details>
<summary><b>Endringsforslag på "add_dict" etter spørsmål om validering</b></summary>

**Prompt 1 (Validere add_dict):**
> - *"Var det lurt med den add_dict funksjonen?"* 

**Svar:**
> - * Now I'm opening the main program file to understand its overall structure and key functions, so I can identify where to implement or analyze the core logic needed for the task.

**Vurdering av `add_dict`-funksjonen**

Tanken bak funksjonen er **helt super**, spesielt hvis planen er å bruke `csv.DictWriter` til å lagre aktivitetene til CSV-fil! Det å konvertere et objekt til en `dict` er en veldig vanlig og god måte å klargjøre data for lagring eller eksport på.

Likevel er det tre konkrete ting som kan forbedres for å gjøre koden enda mer ryddig og etter beste praksis for objektorientert programmering (OOP):

---

**1. Gjør det til en metode inne i `Activity`-klassen (Anbefalt)**  
I objektorientert programmering er det vanlig at objektet selv «vet» hvordan det skal konvertere sine egne data. 

I stedet for en frittstående funksjon `add_dict(activity)`, er det mer ryddig å legge det som en metode inne i `Activity`-klassen, for eksempel `activity.to_dict()`:

```python
class Activity:
    def __init__(self, title: str, category: str, date: datetime, estimated_minutes: int, status):
        self.title = title
        self.category = category
        self.date = date
        self.estimated_minutes = estimated_minutes
        self.status = status

    def show_info(self):
        '''Prints out the activity attributes with a f-string format'''
        print(f"   -- {self.title} --")
        print(f"* Kategori: {self.category}")
        print(f"* Dato: {self.date}")
        print(f"* Estimert varighet i minutter: {self.estimated_minutes}")
        print(f"* Status: {self.status}")

    def to_dict(self):
        '''Returns activity attributes as a dictionary'''
        return {
            "title": self.title,
            "category": self.category,
            "date": self.date,
            "estimated_minutes": self.estimated_minutes,
            "status": self.status
        }
```

Da kan du i hovedprogrammet enkelt skrive:
```python
my_dict = new_activity.to_dict()
```

---

**2. Navngiving (`to_dict` i stedet for `add_dict`)**  
Navnet `add_dict` gir inntrykk av at funksjonen *legger til* noe i en liste eller database (som `add`). Siden funksjonen faktisk *konverterer/returnerer* objektet som en dictionary, er navn som `to_dict()` eller `as_dict()` standard og mer selvforklarende.

---

**3. Konsekvente nøkkelnavn (liten `d` på `date`)**  
I den nåværende koden har `"Date"` stor forbokstav, mens de andre feltene har små forbokstaver:
```python
# Nåværende:
new_dict = {"title": activity.title, "category": activity.category, "Date": activity.date, ...}

# Anbefalt (små bokstaver overalt):
new_dict = {"title": activity.title, "category": activity.category, "date": activity.date, ...}
```
Det er best å bruke konsekvent lowercase på feltnavn, slik at overskriftene i CSV-filen blir ensartede (f.eks. `title,category,date,estimated_minutes,status`).

---

**Oppsummering**
* **Var idéen lur?** Ja, konseptet er midt i blinken for CSV-skriving.
* **Beste justering:** Flytt den inn i klassen som metoden `def to_dict(self):`, rett `"Date"` til `"date"`, og kall den med `aktivitet.to_dict()`.*


</details>

**Prompt 2:**
"Kvifor får eg denne typerror-feilmeldinga? Eg prøver å gjere det som offisiell dokumentasjon forklarer, så eg skjøner ikkje kva dette er for noko?"

**Svar:**
Update to v3419.7.0 failed

Feilmeldinga (`TypeError`) skuldast at metoden `writer.writerow()` manglar eit påkravd argument.

---

**Kva som forårsakar `TypeError`**

I `oppgave_5_helpers.py` har du skrive følgjande i funksjonen `append_to_file`:

```python
def append_to_file(dict, path):
    with open(path, "a", encoding="utf-8", newline='') as path:
        fieldnames = ["title", "category", "date", "estimated_minutes", "status"]
        writer = csv.DictWriter(path, fieldnames=fieldnames)
        writer.writerow()  # <-- Feilen oppstår her!
```

Når du brukar `csv.DictWriter`, krev `writer.writerow()` at du sender med **dictionaryen** som inneheld verdiane som skal skrivast inn i raden. 

Når parentesen er tom (`writer.writerow()`), gir Python feilen:  
`TypeError: DictWriter.writerow() missing 1 required positional argument: 'rowdict'`

---

**Slik løyser du det**

Du må sende med dictionary-objektet som argument til `writer.writerow(...)`:

```python
def append_to_file(activity_dict, file_path):
    with open(file_path, "a", encoding="utf-8", newline='') as file:
        fieldnames = ["title", "category", "date", "estimated_minutes", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(activity_dict)
```

---

**Nyttige forbetringar i koden**

1. **Variabelnamn overskygger kvarandre (`as file` i staden for `as path`):**
   I både `oppgave_5_program.py` og `oppgave_5_helpers.py` står det:
   ```python
   with open(path, "w", ...) as path:
   ```
   Her heiter filstien `path`, men så gir du også sjølve fil-objektet namnet `path`. Bruk heller `as file` eller `as f` for fil-objektet slik at stien og fila ikkje blandast saman. Unngå også å kalle parametere for `dict`, sidan det overskygger Pythons innebygde `dict`-klasse.

2. **Ulik filsti i hovudprogrammet:**
   I `oppgave_5_program.py` opprettar du headeren i mappa `data/activities.csv` via variabelen `path`:
   ```python
   path = data_folder / "activities.csv"
   ```
   Men når du kallar `append_to_file`, sender du inn strengen `"activities.csv"`:
   ```python
   append_to_file(my_dict, "activities.csv")
   ```
   Dette gjer at dataa hamnar i ei ny fil i rotmappa i staden for under `data/`. Send heller med variabelen `path`:
   ```python
   append_to_file(my_dict, path)
   ```
   
**Subprompt:**
Ok, eg har endra det som du påpeiker. Men, eg får fortsatt: 
"Traceback (most recent call last):
  File "C:\Users\Studier\PycharmProjects\GA\Emne1\ga-emne1-arbeidskrav\oppgave_5_program.py", line 21, in <module>
    append_to_file(my_dict, path)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "C:\Users\Studier\PycharmProjects\GA\Emne1\ga-emne1-arbeidskrav\oppgave_5_helpers.py", line 49, in append_to_file
    with open(file_path, "a", encoding="utf-8", newline='') as file:
         ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: expected str, bytes or os.PathLike object, not TextIOWrapper"
**Svar:**
**Kva som forårsakar denne feilmeldinga**

Feilen skuldast at variabelen `path` i `oppgave_5_program.py` blir overskriven og omgjort frå ein filsti til eit fil-objekt (`TextIOWrapper`).

---

**Forklaring steg for steg**

1. **Først definerer du stien:**
   ```python
   path = data_folder / "activities.csv"  # Her er path eit Path-objekt (en gyldig filsti)
   ```

2. **Så overskriv du variabelen i `with`:**
   ```python
   with open(path, "w", newline='', encoding="utf-8") as path:  # <-- Her overskriv `as path` variabelen!
       fieldnames = ["title", "category", "date", "estimated_minutes", "status"]
       writer = csv.DictWriter(path, fieldnames=fieldnames)
       writer.writeheader()
   ```
   Når du skriv `as path`, set Python variabelen `path` lik det opna fil-objektet (`TextIOWrapper`). Sjølv etter at `with`-blokka er ferdig, peikar `path` framleis på fil-objektet (som no er lukka), og ikkje på filstien lenger.

3. **Du sender fil-objektet inn i hjelpefunksjonen:**
   ```python
   append_to_file(my_dict, path)  # Sender inn TextIOWrapper i staden for filstien
   ```

4. **Krasjet oppstår i hjelpefunksjonen:**
   Inne i `oppgave_5_helpers.py` prøver du å opne fila på nytt:
   ```python
   with open(file_path, "a", encoding="utf-8", newline='') as file:
   ```
   Her forventar `open()` ein streng eller eit `Path`-objekt (ein filsti), men får i staden inn `TextIOWrapper`-objektet du sende med. Då kastar Python feilen:
   `TypeError: expected str, bytes or os.PathLike object, not TextIOWrapper`

---

**Slik løyser du det**

Endre `as path` til `as file` (eller `as f`) i `oppgave_5_program.py` slik at du ikkje overskriv sti-variabelen `path`:

```python
with open(path, "w", newline='', encoding="utf-8") as file:
    fieldnames = ["title", "category", "date", "estimated_minutes", "status"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

append_to_file(my_dict, path)
```

Når du no kallar `append_to_file(my_dict, path)`, er `path` framleis den opphavlege `Path`-stien til fila.


**prompt med subprompts**
`return sorted(activity_list, key=itemgetter(int("estimated_minutes")))`

Kvifor fungerer ikkje dette? 

**svar med subprompts**
**Hvorfor koden feiler**

Det er to hovedgrunner til at linjen `return sorted(activity_list, key=itemgetter(int("estimated_minutes")))` ikke fungerer:

---

**1. `int("estimated_minutes")` kaster en `ValueError`**
Når Python leser uttrykket, kjøres `int("estimated_minutes")` med en gang.   
Her forsøker `int()` å konvertere selve tekststrengen `"estimated_minutes"` (altså bokstavene i ordet) til et heltall. Siden ordet ikke består av siffer, krasjer programmet umiddelbart med en feilmelding:  
`ValueError: invalid literal for int() with base 10: 'estimated_minutes'`

---

**2. `itemgetter` kan ikke transformere data underveis**
`itemgetter("estimated_minutes")` fungerer som en snarvei for å hente ut verdien til en nøkkel, tilsvarende `ordbok["estimated_minutes"]`.   
Den kan derimot **ikke** kjøre funksjoner (som `int()`) på verdien den henter ut. Siden verdiene fra CSV-filen er tekststrenger (`"90"`, `"30"`, `"120"`), ville en ren `itemgetter` sortert tallene alfabetisk som tekst i stedet for numerisk.

---

**Hvordan løse det**

For å gjøre om verdien til et heltall før `sorted()` sammenligner elementene, må du hente ut verdien fra ordboken først, og deretter kalle `int()` på den hentede verdien.

Dette kan gjøres på to måter:

**Alternativ A: Med en `lambda`-funksjon**
En `lambda` tar inn hver ordbok (`x`), slår opp nøkkelen `"estimated_minutes"`, og gjør verdien om til `int`:
```python
def filter_duration(activity_list: list):
    return sorted(activity_list, key=lambda x: int(x["estimated_minutes"]))
```

**Alternativ B: Med en vanlig hjelpefunksjon (`def`)**
Hvis du foretrekker vanlige funksjoner fremfor `lambda`:
```python
def get_duration_as_int(activity: dict) -> int:
    return int(activity["estimated_minutes"])

def filter_duration(activity_list: list):
    return sorted(activity_list, key=get_duration_as_int)
```

Now I'm reviewing the function that sorts activity_list by "estimated_minutes" to understand why the current sorting line fails and how to correctly convert the string values to integers before sorting. I want to clarify the key extraction and conversion logic to fix the sorting behavior.

**Requirements**

**Overview & Goals**
The goal is to sort a list of activity dictionaries loaded from `activities.csv` by either date or duration (`estimated_minutes`) while maintaining each activity dictionary's integrity (keeping all fields together).

**Scope**
- **In Scope:**
  - Sorting the list of dictionaries directly using a custom sorting key.
  - Converting numeric string fields to integers and date string fields to datetime objects for accurate comparison.
  - Allowing flexible sorting by either date or duration.
- **Out of Scope:**
  - Modifying the CSV schema or altering the underlying CSV file structure.
  - Modifying other unrelated helper functions in `oppgave_5_helpers.py`.

**Functional Requirements**
- Retain all dictionary attributes (`title`, `category`, `date`, `estimated_minutes`, `status`) in each record after sorting.
- Sort durations numerically (e.g. 30 < 90 < 120).
- Sort dates chronologically based on parsed date values.

**Technical Design**

**Current Implementation**
In `oppgave_5_helpers.py`, `read_file` reads rows as a list of dictionaries with string values via `csv.DictReader`. Currently, `filter_date_or_duration` creates two separate lists with list comprehensions (`dates` and `durations`), sorting them independently and losing the association with other activity fields.

**Key Decisions**
- **In-place vs New List:** Use `sorted()` with a `key` parameter to return a new sorted list of dictionaries without mutating the original list.
- **Key Extraction & Type Casting:**
  - For duration: cast `int(row["estimated_minutes"])` inside the key function.
  - For date: parse the date string using `datetime.strptime` to guarantee accurate chronological comparison regardless of date separator formats.

**Proposed Changes**
- Update `filter_date_or_duration(activity_list, sort_by)` to sort full dictionaries based on the chosen attribute (`"date"` or `"estimated_minutes"`).
- Pass appropriate key transformations to Python's `sorted()` function.

**File Structure**
- `oppgave_5_helpers.py`: Update `filter_date_or_duration` implementation.
- `oppgave_5_program.py`: Call and display sorted activity lists.

**Testing**

**Validation Approach**
Verify sorting functionality with representative dataset records containing multi-digit numbers and various dates.

**Key Scenarios**
- **Numeric Duration Sorting:** Verify that activities with durations like 30, 90, and 120 minutes sort in numeric order (30, 90, 120) instead of alphabetical order (120, 30, 90).
- **Date Sorting:** Verify that activities with dates across different months and years sort in chronological sequence.
- **Dictionary Integrity:** Verify that each element in the resulting list retains all original keys and values.

**Delivery Steps**

**Step 1: Implement value transformation logic for sorting keys**
Implement helper logic or key functions to extract and convert dictionary values for proper numeric and chronological sorting.

- Define integer conversion logic for `estimated_minutes` to ensure numeric comparison rather than lexicographical string comparison.
- Define datetime parsing logic using `datetime.strptime` to ensure accurate chronological date sorting.
- Handle potential malformed entries or formatting inconsistencies gracefully.

**Step 2: Refactor filter_date_or_duration to sort dictionary list**
Update the sorting function in `oppgave_5_helpers.py` so that full activity dictionaries are sorted and returned.

- Refactor `filter_date_or_duration` to accept criteria (such as sorting by date or duration, and optional sort order).
- Use `sorted()` with the appropriate `key` parameter to sort the list of dictionaries without breaking apart the dictionary records.
- Verify that calling `filter_date_or_duration` in `oppgave_5_program.py` prints the activities in the expected sorted order.

**subprompt**
"Kan du bryte ned og forklare den alternativ a for meg"

**svar**

**Forklaring av Alternativ A**

Koden vi ser på er:

```python
def filter_duration(activity_list: list):
    return sorted(activity_list, key=lambda x: int(x["estimated_minutes"]))
```

La oss bryte denne linjen ned i sine enkeltdeler slik at det blir tydelig nøyaktig hva Python gjør bak kulissene.

---

**1. Hovedkomponentene i uttrykket**

Uttrykket består av tre hoveddeler:

1. `sorted(...)`: Pythons innebygde funksjon for å sortere elementer og returnere en ny liste.
2. `activity_list`: Selve listen som skal sorteres. Hvert element i denne listen er en ordbok (`dict`) som representerer en aktivitet.
3. `key=...`: Parameteret som forteller Python *hvilken verdi* den skal bruke til å sammenligne elementene.

---

**2. Hva er en `lambda`?**

En `lambda` er en liten, anonym funksjon (en funksjon uten et definert navn via `def`) som skrives på én enkelt linje.

Følgende to måter å skrive en funksjon på gjør nøyaktig det samme:

```python
# Vanlig funksjon med def:
def hent_varighet(x):
    return int(x["estimated_minutes"])

# Lambda-funksjon:
lambda x: int(x["estimated_minutes"])
```

Fordelen med `lambda` her er at du slipper å opprette en egen funksjon utenfor linjen når du bare trenger logikken ett enkelt sted.

---

**3. Steg for steg: Hva skjer under kjøring?**

Når `sorted()` kjører på `activity_list`, gjør den følgende for **hvert eneste element** i listen:

1. **`x` representerer det gjeldende elementet:**  
   Siden `activity_list` er en liste med ordbøker, er `x` en ordbok, for eksempel:  
   `x = {"title": "Løpetur", "date": "10.05.2024", "estimated_minutes": "45", "status": "completed"}`

2. **Henter ut verdien:**  
   `x["estimated_minutes"]` slår opp nøkkelen og henter ut tekstverdien `"45"`.

3. **Konverterer til heltall:**  
   `int("45")` konverterer strengen `"45"` til heltallet `45`.

4. **Sammenligning og sortering:**  
   Python bruker tallet `45` som grunnlag for å plassere hele ordboken i riktig rekkefølge i forhold til de andre ordbøkene.

---

**4. Hvorfor er `int(...)` nødvendig her?**

CSV-modulen leser alle verdier som tekststrenger (`str`). 

- **Uten `int()` (tekstsortering):**  
  Tekststrenger sammenlignes alfabetisk tegn for tegn. Da vil `"120"` havne før `"30"` og `"90"` fordi tegnet `'1'` kommer før `'3'` i alfabetet.
- **Med `int()` (tallsortering):**  
  Når verdiene gjøres om til tall (`int`), sammenlignes de matematisk: `30 < 45 < 90 < 120`.

> **Merk:** Selve ordboken og verdiene i den blir ikke permanent endret. `int(...)` brukes kun midlertidig av Python for å vite hvilken rekkefølge ordbøkene skal legges i. Resultatlisten inneholder fortsatt de komplette ordbøkene med alle sine opprinnelige felter intakt.

**subprompt**
"Korleis veit lambda at x er for ordbøkene i lista? Kva er logikken (sidan det vanlegvis i ei løkke vil vere "for row in activity_list")"

**svar**
**Korleis `lambda` mottek ordbøkene frå lista**

For å oppnå maksimal nytte og forståing av korleis dette heng saman, er det mest føremålstenleg å sjå på korleis ansvarsfordelinga mellom `sorted()` og `lambda` fungerer i praksis.

Kort sagt: Det er **`sorted()`-funksjonen** som styrer løkka internt, medan **`lambda`** berre tek imot eitt og eitt element som `sorted()` sender inn.

---

**1. `x` er berre eit valt parameternamn**

Når du skriv:
```python
lambda x: int(x["estimated_minutes"])
```
så er `x` berre eit tilfeldig vald namn på inndata-parameteren. Du kan like gjerne kalle parameteren `row` eller `activity` for å gjere koden meir sjølvforklarande og redusere kognitiv belastning:

```python
lambda row: int(row["estimated_minutes"])
```

Dette tilsvarar nøyaktig ein vanleg funksjon:
```python
def hent_varighet(row):
    return int(row["estimated_minutes"])
```

---

**2. Kva gjer `sorted()` under panseret?**

Det er `sorted()` som veit kva som ligg i `activity_list`. Når du sender inn `key=...`, køyrer `sorted()` ei innebygd, optimalisert løkke over lista di.

Logikken `sorted()` utfører internt kan illustrerast slik:

```python
# Slik fungerer logikken internt i Python (forenkla modell):
midlertidige_par = []

for row in activity_list:
    # Her kallar sorted() nøkkelfunksjonen din med kvar ordbok:
    sorteringsnokkel = nøkkelfunksjon(row)  # row blir sendt inn som 'x'
    midlertidige_par.append((sorteringsnokkel, row))

# Sorterer basert på den utrekna nøkkelen
midlertidige_par.sort()

# Pakkar ut dei originale ordbøkene i rett rekkjefølgje
sortert_liste = [row for sorteringsnokkel, row in midlertidige_par]
```

---

**3. Samanlikning: Vanleg løkke vs. `key`-funksjon**

| Konsept | Korleis elementet vert handtert |
| :--- | :--- |
| **Vanleg `for`-løkke** | Du skriv løkka manuelt: `for row in activity_list:` og vel kva som skal skje med `row`. |
| **`sorted(..., key=...)`** | `sorted()` køyrer løkka for deg i rask C-kode på lågt nivå, og sender kvart `row` rett inn som argument til funksjonen du oppgav som `key`. |

**Oppsummering av nytteverdien**

- `lambda` veit ikkje kva den får inn på førehand; den forventar berre eit objekt som den kan gjere oppslag i.
- `sorted()` veit kva lista inneheld, itererer gjennom kvart element, og mater det inn i funksjonen.
- Dette mønsteret minimerer boilerplate-kode, aukar køyresnøggleiken og sikrar at dataa vert handsama konsistent utan manuelle løkker.
































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


