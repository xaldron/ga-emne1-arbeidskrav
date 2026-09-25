from pathlib import Path
from oppgave_5_helpers import *
import sys

if __name__ == '__main__':
    try:

        data_folder = Path(__file__).parent / "data"
        path = data_folder / "activities.csv"
        print(path.exists())

        my_list = read_file(path)


        with open(path, "w", newline='', encoding="utf-8") as file:
            fieldnames = ["title", "category", "date", "estimated_minutes", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(my_list)
















    except Exception as error:
        print(f"En uventet feil oppstod {error}")
        sys.exit(1)







'''new_test = register_activity()
        test_dict = new_test.to_dict()
        append_to_file(test_dict, path)
        print(read_file(path))'''