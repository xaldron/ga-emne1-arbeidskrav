from datetime import datetime
#Planning to use csv writer to save activities to file
import csv
from collections import Counter

# Class
# --------------------------------------------------------------

class Activity:
    def __init__(self, title: str, category: str, date, estimated_minutes: int, status: str):
        self.title = title
        self.category = category
        self.date = date
        self.estimated_minutes = estimated_minutes
        self.status = status


    def __str__(self) -> str:
        return (f"  == {self.title} ==\n"
                f"* Kategori: {self.category}\n"
                f"* Dato: {self.date}\n"
                f"* Estimert varighet i minutter: {self.estimated_minutes}\n"
                f"* Status: {self.status}")


    def to_dict(self):
        '''Returns activity attributes as a dictionary'''
        return {
            "title": self.title,
            "category": self.category,
            "date": self.date,
            "estimated_minutes": self.estimated_minutes,
            "status": self.status
        }


# Functions
# --------------------------------------------------------------

# Register activity
def register_activity():
    '''Gather information about an activity and return a instance of the Activity class'''
    title = input("Navn på aktivitet: ")
    category = input("Kategori: ")
    date = None
    while not date:
        date = add_date(input('Vennligst oppgi en dato (dd.mm.åååå): '))
        continue
    estimated_minutes = None
    while not estimated_minutes:
        try:
            estimated_minutes = int(input("Oppgi vargihet i minutter (kun heltall): "))
        except ValueError, TypeError:
            print("Error: Det ser ut til at du har oppgitt en ugyldig verdi. Oppgi kun varighet i hele antall minutter")
            continue
    status = ""
    while status == "":
        status = input("Er du ferdig med aktiviteten? Oppgi 'Ja' eller 'Nei': ")
        if status.lower() == "ja":
            status = "completed"
        elif status.lower() == "nei":
            status = "planned"
        else:
            print("Beklager, jeg forstår ikke svaret ditt. Svar kun 'Ja' eller 'Nei' ")
            status = ""
            continue
    activity = Activity(title, category, date, estimated_minutes, status)
    return activity


# Re-used from task 3
def add_date(new_date):
    '''take in a date with dd.mm.yyyy format and return the date'''
    try:
        print("\n")
        return datetime.strptime(new_date, "%d.%m.%Y").date()
    except ValueError:
        print('Beklager, det ser ut til at du har oppgitt en ugyldig dato. Vennligst bruk riktig format (dd.mm.åååå)')


# Add dictionary to csv file
def append_to_file(activity_dict, file_path):
    '''Takes in a dictionary and a file path and appends dictionary to that file'''
    try:
        with open(file_path, "a", encoding="utf-8", newline='') as file:
            fieldnames = ["title", "category", "date", "estimated_minutes", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(activity_dict)
    except FileNotFoundError, FileExistsError, PermissionError:
        print("Error: Det ser ut som filen ikke eksisterer, eller at du ikke har tilgang til den.")

def read_file(file_path):

    rows = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = csv.DictReader(file)
            for row in content:
                rows.append(row)
            return rows
    except FileNotFoundError, FileExistsError, PermissionError:
        print("Error: Det ser ut som filen ikke eksisterer, eller at du ikke har tilgang til den..")

def search_title_or_category(activity_list: list) -> None:

    search = input('Søk etter tittel eller kategori: ')

    for row in activity_list:
        if search.lower() in str(row.values()).lower():
            print(f"  == {row["title"]} ==\n"
                f"* Kategori: {row["category"]}\n"
                f"* Dato: {row["date"]}\n"
                f"* Estimert varighet i minutter: {row["estimated_minutes"]}\n"
                f"* Status: {row["status"]}")
            print()
        else:
            continue

def filter_status(activity_list: list, status: str) -> None:


    for row in activity_list:
        if status.lower() == row["status"]:
            print(f"  == {row["title"]} ==\n"
                f"* Kategori: {row["category"]}\n"
                f"* Dato: {row["date"]}\n"
                f"* Estimert varighet i minutter: {row["estimated_minutes"]}\n"
                f"* Status: {row["status"]}")
            print()





