import csv
from pathlib import Path
from collections import Counter

print(f"Current directory: {Path.cwd()}")

file_dir = Path("data")
file_path = file_dir / "supporthenvendelser.csv"

# Oppgave 4.1
def read_check():
    with open(file_path, "r", encoding="utf-8") as file:
        content = csv.DictReader(file)
        for row in content:
            if "" in row.values():
                print(f"Problem på rad: Det ser ut til at denne raden mangler en eller flere gyldige verdier.")
            elif int(row['id']) < 1:
                print(f"Problem på rad: Id er ikke et positivt heltall.")
            elif not row['minutes'].isdigit() or int(row['minutes']) < 0:
                print(f"Problem på rad: Minutter er ikke et heltall på null eller mer.")
            elif row['is_resolved'] != "yes" and row['is_resolved'] != "no":
                print(f"Problem på rad: Ugyldig status på om henvendelsen er løst")
            else:
                print(row)


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

def valid_ticket_count():

    with open(file_path, "r", encoding="utf-8") as file:
        content = csv.DictReader(file)
        counter = 0
        for row in content:
            if "" in row.values():
                continue
            elif int(row['id']) < 1:
                continue
            elif not row['minutes'].isdigit() or int(row['minutes']) < 0:
                continue
            elif row['is_resolved'] != "yes" and row['is_resolved'] != "no":
                continue
            else:
                counter += 1
        return counter


def ticket_per_category():

    with open(file_path, "r", encoding="utf-8") as file:
        content = csv.DictReader(file)
        categories = []
        for row in content:
            if "" in row.values():
                continue
            elif int(row['id']) < 1:
                continue
            elif not row['minutes'].isdigit() or int(row['minutes']) < 0:
                continue
            elif row['is_resolved'] != "yes" and row['is_resolved'] != "no":
                continue
            else:
                for k,v in row.items():
                    if k == "category":
                        categories.append(v)
        return Counter(categories)


# -------

def ticket_time_spent():
    with open(file_path, "r", encoding="utf-8") as file:
        content = csv.DictReader(file)
        total_minutes = 0
        counter = 0
        for row in content:
            if "" in row.values():
                continue
            elif int(row['id']) < 1:
                continue
            elif not row['minutes'].isdigit() or int(row['minutes']) < 0:
                continue
            elif row['is_resolved'] != "yes" and row['is_resolved'] != "no":
                continue
            else:
                counter += 1
                total_minutes += int(row['minutes'])

        # prevent division by 0 and returners optimized result
        if counter == 0:
            return (0, 0.0)

        return total_minutes, round(total_minutes / counter, 1)


print(ticket_time_spent())

def tickets_solved_unsolved():

    with open(file_path, "r", encoding="utf-8") as file:
        content = csv.DictReader(file)
        solved = 0
        unsolved = 0
        for row in content:
            if "" in row.values():
                continue
            elif int(row['id']) < 1:
                continue
            elif not row['minutes'].isdigit() or int(row['minutes']) < 0:
                continue
            elif row['is_resolved'] != "yes" and row['is_resolved'] != "no":
                continue
            else:
                if row["is_resolved"] == "yes":
                    solved += 1
                else:
                    unsolved += 1
        return solved, unsolved

print(tickets_solved_unsolved())


def most_tickets(categories):
    return max(categories.items())

print(ticket_per_category())
print(most_tickets(ticket_per_category()))





