from datetime import datetime
#Planning to use csv writer to save activities to file
import csv

# Class
# -------------------------

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



# Functions
# -----------------------

# Re-used from task 3
def add_date(new_date):
    '''take in a date with dd.mm.yyyy format and return the date'''
    try:
        print("\n")
        return datetime.strptime(new_date, "%d.%m.%Y").date()
    except ValueError:
        print('Beklager, det ser ut til at du har oppgitt en ugyldig dato. Vennligst bruk riktig format (dd.mm.åååå)\n')


# Add Activity object to a dictionary. To be used to write into csv file
def add_dict(activity):
    '''Add all Activity object attributes to a dictionary, with corresponding key names'''
    new_dict = {"title": activity.title, "category": activity.category, "Date": activity.date, "estimated_minutes": activity.estimated_minutes, "status": activity.status}
    return new_dict
