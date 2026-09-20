from oppgave_4_helpers import *

report_path = file_dir / "support-rapport.txt"


read_check()
valid_tickets = get_valid_tickets()
amount_tickets = valid_ticket_count(valid_tickets)
categories = ticket_per_category(valid_tickets)
total, avg = ticket_time_spent(valid_tickets)
solved, unsolved = tickets_solved_unsolved(valid_tickets)
highest_category = most_tickets(categories)



with open(report_path, "w", encoding="utf-8") as file:
    file.write("= RAPPORT FOR SUPPORTHENVENDELSER =\n")
    file.write("-----------------------------------\n")
    file.write("\n== Antall gyldige henvendelser og antall i hver kategori ==\n")
    file.write(f"\nDet er {amount_tickets} gyldige henvendelser og antall per kategori fordeler seg slik: {categories}\n")
    file.write("\n-------------------------------------\n")
    file.write("\n== Samlet og gjennomsnittlig tidsbruk ==\n")
    file.write(f"\nSamlet tidsbruk for henvendelsene er: {total} minutter.\n")
    file.write(f"Gjennomsnittlig tidsbruk for henvendelsene er: {avg} minutter.\n")
    file.write("\n----------------------------------\n")
    file.write("\n == Antall løste og uløste henvendelser ==\n")
    file.write(f"\n Antall løste henvendelser: {solved}")
    file.write(f"\n Antall uløste henvendelser: {unsolved}")
    file.write(f"test {highest_category}")
    file.write("")
    file.write("")













