from datetime import  date, datetime, timedelta



def add_date(new_date):
    '''take in a date with dd.mm.yyyy format and return the date'''
    try:
        print("\n")
        return datetime.strptime(new_date, "%d.%m.%Y").date()
    except ValueError:
        print('Beklager, det ser ut til at du har oppgitt en ugyldig dato. Vennligst bruk riktig format (dd.mm.åååå)\n')


def start_end(start_time, duration_in_minutes):
    '''Take in start time and minutes and returns endtime'''
    new_time = datetime.combine(date.today(), start_time) + timedelta(minutes=duration_in_minutes)
    return new_time.strftime("%H:%M:%S")


def days_between(date_1, date_2):
    '''Take inn two dates and return (positive) days between them'''
    return abs((date_1 - date_2).days)


def list_of_dates_sorted(date_list):
    '''Take in a list of datoes and return a chronologically sorted list'''
    return sorted(date_list)


planner_on = True

study_dates = []

while planner_on:
    print()
    print("Vennligst velg fra menyen hva du vil gjøre:")
    print("1: Legg til en dato for undervisning")
    print("2: Vis en kronologisk sortert liste over undervisningsdatoer")
    print("3: Beregn sluttid for en økt")
    print("4: Vis antall dager mellom to økter")
    print("5: Avslutt programmet")
    print()


    try:
        choice = int(input('Vennligst tast 1-5 for å velge: '))
        print()
    except:
        print(
            '\nBeklager, jeg forstår ikke valget ditt. Vennlist prøv igjen')  # Starting with new line to create space between menu and error
        continue

    if choice not in range(1, 6):
        print('\nJeg godtar kun valg mellom 1 og 5')  # Starting with new line to create space between menu and error
        continue

    elif choice == 1:
        new_date = None
        while not new_date:
            new_date = add_date(input('Vennligst oppgi en dato (dd.mm.åååå): '))
        study_dates.append(new_date)
        print(f"Dato {new_date.strftime("%d.%m.%Y")} er lagt til.\n")

    elif choice == 2:
        study_dates = list_of_dates_sorted(study_dates)
        print("Undervisningsdatoer lagt i planleggeren: \n")
        for e in study_dates:
            print(e.strftime("%d.%m.%Y"))
        print()

    elif choice == 3:
        # 1. Gather and validate start time
        start_time = None
        while start_time is None:
            time_input = input("Vennligst oppgi et klokkeslett for når forelesningen starter (TT:MM): ")
            try:
                # Convert string to datetime, and extract time-object
                start_time = datetime.strptime(time_input, "%H:%M").time()
            except ValueError:
                print("Beklager, ugyldig klokkeslett eller format. Vennligst bruk TT:MM (f.eks. 10:15 eller 14:00).\n")

        # 2. Extract and validate duration
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


    elif choice == 4:
        one_date = None
        while not one_date:
            one_date = add_date(input('Vennligst oppgi en dato (dd.mm.åååå): '))

        another_date = None
        while not another_date:
            another_date = add_date(input('Vennligst oppgi enda en dato (dd.mm.åååå): '))

        print(f"Dager mellom disse to datoene er: {days_between(one_date, another_date)}\n")

    else:
        print(
            '\nTakk for at du brukte dette programmet. Programmet avsluttes. ')  # New line to create space between menu and this message
        planner_on = False
