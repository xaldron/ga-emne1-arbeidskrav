# Oppgave 1.1 - Beregn tidsbruk
def calculate_time():

    gather_data = True

    while gather_data:
        try:
            study_sessions = int(input('Hvor mange studieøkter har du deltatt i til nå? '))
            minutes_per_sessions = int(input('Hvor mange minutter varer hver økt? '))
        except:
            print('Beklager. Jeg forstår ikke svarene dine. Prøv igjen og svar kun med hele tall (høyere enn "0").')
            continue
        else:
            gather_data = False

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

        try:
            start_value = int(input('Vennligst tast inn en startverdi: (bare heltall)'))
            stop_value = int(input('Vennligst tast inn en stoppverdi: (bare heltall)'))
        except:
            print('Beklager, jeg forstår ikke svarene dine. Prøv igjen (kun heltall).')
            continue

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

        try:
            choice = int(input('Vennligst tast 1-4 for å velge: '))
        except:
            print('\nBeklager, jeg forstår ikke valget ditt. Vennlist prøv igjen') # Starting with new line to create space between menu and error
            continue

        if choice not in range(1, 5):
            print('\nJeg godtar kun valg mellom 1 og 4') # Starting with new line to create space between menu and error
            continue
        elif choice == 1:
            calculate_time()
        elif choice == 2:
            analyze_text()
        elif choice == 3:
            analyze_numbers()
        else:
            print('\nTakk for at du brukte dette programmet. Programmet avsluttes. ') # New line to create space between menu and this message
            menu_on = False
choose_program()