from evidencezasilek import EvidenceZasilek
from datetime import datetime

evidence = EvidenceZasilek()

evidence.registruj_zasilku(1, "Jan Novak", "Petr Svoboda", "Praha 1, Namesti Republiky 1", datetime(2024, 6, 1))
evidence.zasilka_prevzata(1, datetime(2024, 6, 2), "Zásilka převzata kurýrem.")
evidence.zasilka_na_ceste(1, datetime(2024, 6, 3), "Zásilka je na cestě k příjemci.")
evidence.zasilka_dorucena(1, datetime(2024, 6, 4), "Zásilka doručena příjemci.")

evidence.registruj_zasilku(2, "Eva Kralova", "Martin Dvorak", "Brno, Masarykova 10", datetime(2024, 6, 5))
evidence.zasilka_prevzata(2, datetime(2024, 6, 6), "Zásilka převzata kurýrem.")
evidence.zasilka_vracena(2, datetime(2024, 6, 7), "Zásilka vrácena odesílateli z důvodu nedostupnosti příjemce.")

print("Info o zasilce 1:")
print(evidence.zasilka_info(1))

print("Info o zasilce 2:")
print(evidence.zasilka_info(2))

print("Historie zasilky 1:")
print(evidence.historie_zasilky(1))

print("Historie zasilky 2:")
print(evidence.historie_zasilky(2))
