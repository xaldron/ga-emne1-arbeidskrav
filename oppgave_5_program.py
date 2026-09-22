from oppgave_5_helpers import *

new_activity = Activity("Testing", "Studier", "2026-09-22", 15, "planned")

new_activity.show_info()

my_dict = add_dict(new_activity)
print(my_dict)
