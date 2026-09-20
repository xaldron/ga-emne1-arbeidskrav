# Oppgave 4.3

from oppgave_4_helpers import *

report_path = file_dir / "support-rapport.txt"


read_check()
valid_tickets = get_valid_tickets()
amount_tickets = valid_ticket_count(valid_tickets)
categories = ticket_per_category(valid_tickets)
total, avg = ticket_time_spent(valid_tickets)
solved, unsolved = tickets_solved_unsolved(valid_tickets)
top_category, top_count = most_tickets(categories)
unsolved_sorted = unsolved_tickets_sorted(valid_tickets)



with open(report_path, "w", encoding="utf-8") as file:
    file.write("= RAPPORT FOR SUPPORTHENVENDELSER =\n")
    file.write("-----------------------------------\n")
    file.write("\n== Antall gyldige henvendelser og antall i hver kategori ==\n")
    file.write(f"\nDet er totalt {amount_tickets} gyldige henvendelser.\n")
    file.write("\nFordeling per kategori: \n")
    for c, n in categories.items():
        file.write(f"  * {c}: {n} henvendelser\n")
    file.write("\n-------------------------------------\n")
    file.write("\n== Samlet og gjennomsnittlig tidsbruk ==\n")
    file.write(f"\nSamlet tidsbruk for henvendelsene er: {total} minutter.\n")
    file.write(f"Gjennomsnittlig tidsbruk per henvendelsene er: {avg} minutter.\n")
    file.write("\n----------------------------------\n")
    file.write("\n == Antall løste og uløste henvendelser ==\n")
    file.write(f"\n Antall løste henvendelser: {solved}")
    file.write(f"\n Antall uløste henvendelser: {unsolved}")
    file.write(f"\n---------------------------------\n")
    file.write("\n== Kategorien med flest henvendelser ==\n")
    file.write(f"\n Kategori '{top_category}' har {top_count} henvendelser og er dermed kategorien med flest henvendelser.\n")
    file.write("\n------------------------------------\n")
    file.write("\n == Uløste henvendelser per mest tidkrevende == \n")
    file.write("\nFordeling per id og tidsbruk: \n")
    for m, i in unsolved_sorted:
        file.write(f"  * Henvendelse med ID nummer {i}: Antall minutter brukt: {m} \n")
    file.write("\n------------------------------------\n")

# Oppgave 4.4

print("\n")
print("Resultat av oppgave 4.4: ")
try:
    result = sum_resolved_minutes(valid_tickets)
    print(f"- Totalt løste minutt: {result}")
except FileNotFoundError:
    print("Feil: Fant ikke CSV-fila for supporthenvendelser.")












