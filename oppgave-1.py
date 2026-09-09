# Oppgave 1.1 - Beregn tidsbruk
def calculate_time():
    gather_data = True
    while gather_data:

        study_sessions = input('Hvor mange studieøkter har du deltatt i til nå? ')
        if not study_sessions.isdigit() or study_sessions == "0":
            print('Beklager. Jeg forstår ikke svaret ditt. Prøv igjen og svar kun med hele tall (høyere enn "0").')
            continue

        minutes_per_sessions = input('Hvor mange minutter varer hver økt? ')
        if not minutes_per_sessions.isdigit() or minutes_per_sessions == "0":
            print('Beklager. Jeg forstår ikke svaret ditt. Prøv igjen og svar kun med hele tall (høyere enn "0").')
            continue

        gather_data = False

    study_sessions = int(study_sessions)
    minutes_per_sessions = int(minutes_per_sessions)

    minutes = study_sessions * minutes_per_sessions
    hours = minutes // 60
    minutes_left = minutes % 60


    print(f'Antall studieøkter: {study_sessions}')
    print(f'Minutter per økt: {minutes_per_sessions}')
    print(f'Samlet tidsbruk: {hours} timer og {minutes_left} minutter')


# Oppgave 1.2 - Analyser tekst
def analyze_text():
    my_text = ""
    while my_text == "" or my_text.isspace():
        my_text = input('Vennligst skriv inn en tekst: ')

    print(f'Denne teksten har {len(my_text)} tegn med mellomrom, og {len(my_text) - my_text.count(" ")} tegn uten.')
    print(f'Denne teksten blir "{my_text[::-1]}" baklengs.')
    print(f'Denne teksten blir "{my_text.lower()}" med bare små bokstaver.')

    if "python" in my_text.lower():
        print('Denne teksten har "Python" i seg.')


# Oppgave 1.3 - Analyser tallintervall
def analyze_numbers():

    gather_values = True
    total = 0

    while gather_values:

        start_value = input('Vennligst tast inn en startverdi: (bare heltall)')
        stop_value = input('Vennligst tast inn en stoppverdi: (bare heltall)')

        if not start_value.isdigit() or not stop_value.isdigit():
            print('Beklager, jeg forstår ikke. Prøv igjen (kun heltall)')
            continue

        start_value = int(start_value)
        stop_value = int(stop_value)

        if stop_value < start_value:
            print('Beklager, men stoppverdien kan ikke være lavere enn startverdien! Prøv på nytt')
            continue
        else:
            gather_values = False


    for n in range(start_value, stop_value+1):
        total += n

        if n % 2 == 0 and n % 3 == 0:
            print(f'{n} er et partall og kan deles på 3 uten rest.')
        elif n % 3 == 0:
            print(f'{n} kan deles på 3 uten rest.')
        elif n % 2 == 0:
            print(f'{n} er et partall.')

    print(f'Summen av alle tall fra {start_value} til og med {stop_value} = {total}')

# Oppgave 1.4 - Lag en meny
def choose_program():
    menu_on = True

    while menu_on:
        print('\n') # To create space between every new menu display
        print('Vennligst velg program fra menyen ved å taste inn nummererte valg 1-3 eller avslutt med "4": ')
        print('1. Beregn tidsbruk')
        print('2. Analyser tekst')
        print('3. Analyser Tallintervall')
        print('4. Avslutt')

        choice = input('Vennligst tast 1-4 for å velge: ')
        if not choice.isdigit():
            print('\nBeklager, jeg forstår ikke svaret ditt. Vennlist prøv igjen') # Starting with new line to create space between menu and error
        elif int(choice) not in range(1, 5):
            print('\nJeg godtar kun valg mellom 1 og 4') # Starting with new line to create space between menu and error

        elif choice == "1":
            calculate_time()
        elif choice == "2":
            analyze_text()
        elif choice == "3":
            analyze_numbers()
        else:
            print('\nTakk for at du brukte dette programmet. Programmet avsluttes. ') # To create space between menu and this message
            menu_on = False
choose_program()






