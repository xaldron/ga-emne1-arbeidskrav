
study_sessions = [{"topic": "Operators",
                   "duration_minutes": 30,
                   "status": "completed"},
                  {"topic": "Conditionals",
                   "duration_minutes": 30,
                   "status": "completed"},
                  {"topic": "Loops",
                   "duration_minutes": 45,
                   "status": "completed"},
                  {"topic": "functions",
                   "duration_minutes": 60,
                   "status": "planned"},
                  {"topic": "Oop",
                   "duration_minutes": 60,
                   "status": "planned"}]


def register_session():
    add_dict = {}
    gather_data = True

    while gather_data:
        add_dict["topic"] = input('Vennligst oppgi tema for studieøkten: ')
        if add_dict["topic"] == "" or add_dict["topic"].isspace():
            print('Beklager. Jeg forstår ikke svaret ditt. Vennligst prøv igjen.')
            continue

        add_dict["duration_minutes"] = input('Vennligst oppgi varighet for økten i minutter: (kun heltall)')
        if not add_dict["duration_minutes"].isdigit():
            print('Bruk kun heltall, takk.')
            continue
        else:
            add_dict["duration_minutes"] = int(add_dict["duration_minutes"])

        add_dict["status"] = input('Vennligst oppgi status "planlagt"/"fullført": ')
        if add_dict["status"].lower() == 'planlagt':
            add_dict["status"] = "planned"
        elif add_dict["status"].lower() == 'fullført':
            add_dict["status"] = "completed"
        else:
            print('Vennligst tast inn "planlagt" eller "fullført" i svaret ditt.')
            continue

        gather_data = False

    return add_dict


def display_sessions(dict_list):
    if dict_list == []:
        print('Beklager. Det finnes ingen studieøkter registrert ennå.')
    else:
        for dicts in dict_list:
            print("")
            for k,v in dicts.items():
                print(k.capitalize()+':',v)


def display_completed():
    completed_sessions = [s for s in study_sessions if s["status"] == "completed"]

    if not completed_sessions:
        print("Ingen fullførte studieøkter funnet.")

    for session in completed_sessions:
        print("")
        for k, v in session.items():
            print(k.capitalize() + ":", v)


def search_topic():

    search_on = True
    while search_on:

        new_search = input("Vennligst tast inn et søkeord: ")

        if new_search.isspace() or new_search == "":
            print("Beklager, jeg forstår ikke søket ditt. Prøv igjen.")
            continue
        else:
            search_result = [s for s in study_sessions if new_search.lower() in s["topic"].lower()]

        if len(search_result) == 0:
            print("Beklager. Ingen treff som samsvarte med søket ditt.")
        else:
            for search in search_result:
                print('\nSearch results:') # Starting with new line to create space between this print and previous ones
                for k, v in search.items():
                    print(k.capitalize() + ":", v)

        search_on = False


def sort_duration():
    from operator import itemgetter

    print('Sorterer... ')
    print('Sortering vellyket! Bruk menyvalg 2 for å se oppdatert liste over dine studieøkter, sortert etter varighet.')

    return sorted(study_sessions, reverse=True, key = itemgetter('duration_minutes'))


def display_duration_completed():
    counter = 0
    for d in study_sessions:
        if d["status"] == "completed":
            counter += d["duration_minutes"]

    if len(study_sessions) == 0:
        print('Beklager, det ser ut til at du ikke fullført noen studieøkter ennå.')
    else:
        print(f'Samlet varighet for fullførte økter: {counter}')
        print(f'Gjennomsnittlig varighet for fullførte økter: {counter / len(study_sessions):.0f}')


def choose_program():
    menu_on = True

    while menu_on:
        print('\n') # To create space between every new menu display
        print('Vennligst velg program fra menyen ved å taste inn nummererte valg 1-3 eller avslutt med "4": ')
        print('1. Registrer en studieøkt')
        print('2. Vis alle studieøkter')
        print('3. Vis kun fullførte studieøkter')
        print('4. Søk etter tema')
        print('5. Sorter øktene etter varighet (fra lengst til kortest)')
        print('6. Vis samlet og gjennomsnittlig varighet for fullførte økter')
        print('7. Avslutt')


        try:
            choice = int(input('Vennligst tast 1-7 for å velge: '))
        except:
            print('\nBeklager, jeg forstår ikke valget ditt. Vennlist prøv igjen') # Starting with new line to create space between menu and error
            continue

        if choice not in range(1, 8):
            print('\nJeg godtar kun valg mellom 1 og 7') # Starting with new line to create space between menu and error
            continue
        elif choice == 1:
            study_sessions.append(register_session())
        elif choice == 2:
            display_sessions(study_sessions)
        elif choice == 3:
            display_completed()
        elif choice == 4:
            search_topic()
        elif choice == 5:
            study_sessions = sort_duration()
        elif choice == 6:
            display_duration_completed()
        else:
            print('\nTakk for at du brukte dette programmet. Programmet avsluttes. ') # New line to create space between menu and this message
            menu_on = False
choose_program()
