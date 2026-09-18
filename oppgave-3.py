from datetime import  date, datetime, time, timedelta

#test_date = input('Vennligst oppgi en dato (dd.mm.åååå): ')

def add_date(new_date):
    '''take in a date with dd.mm.yyyy format and return the date'''
    try:
        return date.strptime(new_date, "%d.%m.%Y")
    except:
        print('Beklager, det ser ut til at du har oppgitt en ugyldig dato. Vennligst prøv igjen (dd.mm.åååå)')




my_time = time(13, 00)

def start_end(start_time, duration_in_minutes):
    '''Take in start time and minutes and returns endtime'''
    new_time = datetime.combine(date.today(), start_time) + timedelta(minutes=duration_in_minutes)
    return new_time.strftime("%H:%M:%S")




one_date = date(1998, 6, 26)
another_date = date(1990, 12, 18)

def days_between(date_1, date_2):
    '''Take inn two dates and return (positive) days between them'''
    return abs((date_1 - date_2).days)


def list_of_dates_sorted():
    '''Take in a list of datoes and return a chronologically sorted list'''
    pass


