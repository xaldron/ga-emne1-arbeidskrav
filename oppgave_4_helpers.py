from collections import Counter
import csv
from pathlib import Path


file_dir = Path("data")
file_path = file_dir / "supporthenvendelser.csv"


# Oppgave 4.1
def read_check():
    with open(file_path, "r", encoding="utf-8") as file:
        content = csv.DictReader(file)
        for row in content:
            if "" in row.values():
                print(f"Problem på rad: Det ser ut til at denne raden mangler en eller flere gyldige verdier. Raden tas ikke med i rapporten.")
            elif int(row['id']) < 1:
                print(f"Problem på rad: Id er ikke et positivt heltall. Raden tas ikke med i rapporten.")
            elif not row['minutes'].isdigit() or int(row['minutes']) < 0:
                print(f"Problem på rad: Minutter er ikke et heltall på null eller mer. Raden tas ikke med i rapporten.")
            elif row['is_resolved'] != "yes" and row['is_resolved'] != "no":
                print(f"Problem på rad: Ugyldig status på om henvendelsen er løst. Raden tas ikke med i rapporten.")
            else:
                print(row)
    print()
    print("Skriver rapport med utvalgte resultater...\nSe egen fil 'support-rapport.txt'")


# Oppgave 4.2
# Function to return only valid tickets to be used in all other functions
def get_valid_tickets():
    valid_rows = []
    with open(file_path, "r", encoding="utf-8") as file:
        content = csv.DictReader(file)
        for row in content:
            if "" in row.values():
                continue
            elif int(row['id']) < 1:
                continue
            elif not row['minutes'].isdigit() or int(row['minutes']) < 0:
                continue
            elif row['is_resolved'] not in ("yes", "no"):
                continue
            else:
                valid_rows.append(row)
    return valid_rows


def valid_ticket_count(tickets):
    return len(tickets)


def ticket_per_category(tickets):
    categories = [row["category"] for row in tickets]
    return Counter(categories)


def ticket_time_spent(tickets):
    if not tickets:
        return (0, 0.0)

    total_minutes = sum(int(row["minutes"]) for row in tickets)
    avg_minutes = round(total_minutes / len(tickets), 1)
    return total_minutes, avg_minutes


def tickets_solved_unsolved(tickets):
    solved = sum(1 for row in tickets if row["is_resolved"] == "yes")
    unsolved = len(tickets) - solved
    return solved, unsolved


def most_tickets(categories):
    return categories.most_common(1)[0]

def unsolved_tickets_sorted(tickets):
    unsolved_tickets = [(row["minutes"], row["id"]) for row in tickets if row["is_resolved"] == "no"]
    return sorted(unsolved_tickets, reverse=True)


# Oppgave 4.4
def sum_resolved_minutes(requests: list[dict[str, str | int]] > int):
    total = 0
    for request in requests:
        if request["is_resolved"] == "yes":
            try:
                total += int(request["minutes"])
            except (ValueError, TypeError):
                print("Wops. Her ser det ut til eksisterer en ugyldig eller ikke eksisterende verdi!")
                continue
    return total