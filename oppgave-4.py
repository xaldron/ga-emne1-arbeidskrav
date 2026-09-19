import csv
from pathlib import Path
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

