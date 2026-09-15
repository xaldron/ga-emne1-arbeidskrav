from datetime import datetime, date, time, timedelta

test_date = input('Vennligst oppgi en dato (dd.mm.åååå): ')

def add_date(new_date):
    '''take in a date with dd.mm.yyyy format and return the date'''
    try:
        return date.strptime(new_date, "%d.%m.%Y")
    except:
        print('Beklager, det ser ut til at du har oppgitt en ugyldig dato. Vennligst prøv igjen (dd.mm.åååå)')




my_time = time(13, 00)

def start_end(start_time, minutes):
    '''Take in start time and minutes and returns endtime'''
    try:
        return timedelta.time.strptime(start_time, "%h:%m") == time(minutes)
    except:
        print('Beklager, det ser ut til at du har oppgitt et ugyldig tidspunkt. Vennligst prøv igjen (tt:mm)')

print(start_end(my_time, 60))

def days_between():
    '''Take inn two dates and return (positive) days between them'''
    pass

def list_of_dates_sorted():
    '''Take in a list of datoes and return a chronologically sorted list'''
    pass


