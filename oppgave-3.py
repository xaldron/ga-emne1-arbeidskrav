import datetime

def add_date():
    '''take in a date with dd.mm.yyyy format and return the date'''
    get_date = True
    while get_date:
        try:
            date_string = input('Vennligst oppgi en dato (dd.mm.åååå): ')
            user_date = datetime.date.strptime(date_string, "%d.%m.%Y")
        except:
            print('Beklager, det ser ut til at du har oppgitt en ugyldig dato. Vennligst prøv igjen (dd.mm.åååå')
            continue
        get_date = False
    return user_date

def start_end():
    '''Take in start time and minutes and returns endtime'''
    pass

def days_between():
    '''Take inn two dates and return (positive) days between them'''
    pass

def list_of_dates_sorted():
    '''Take in a list of datoes and return a chronologically sorted list'''
    pass


