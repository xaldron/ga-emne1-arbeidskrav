from pathlib import Path

data_folder = Path(__file__).parent / "data"
path = data_folder / "activities.csv"
print(path.exists())

from oppgave_5_helpers import *



with open(path, "w", newline='', encoding="utf-8") as file:
    fieldnames = ["title", "category", "date", "estimated_minutes", "status"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

my_test = Activity("Testing", "Coding", "23.09.2026", 15, "planned")
my_dict = my_test.to_dict()
append_to_file(my_dict, path)


print(my_test)




