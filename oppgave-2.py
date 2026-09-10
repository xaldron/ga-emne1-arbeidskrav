
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


def display_sessions():
    if study_sessions == []:
        print('Beklager. Det finnes ingen studieøkter registrert ennå.')
    else:
        for dicts in study_sessions:
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
        elif new_search.lower() not in study_sessions.split().lower():
            print("Beklager. Ingen treff som samsvarte med søket ditt.")
            search_on = False
        else:
            for dicts in study_sessions:
                if new_search.lower() == dicts["status"].lower():
                    print(dicts)


search_topic()


# sort_duration()
    # If no result, print clear message

# display_duration_completed()
    # If no result, print clear message

# close_program()

#menu_on: pass
 #study_sessions.append(register_session())
 #print(study_sessions[5])
# Clear error message if non-valid menu choice