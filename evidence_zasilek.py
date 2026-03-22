from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class StavZasilky(str, Enum):
    REGISTROVANA = "registrovana"
    ODESLANA = "odeslana"
    DORUCENA = "dorucena"
    NA_CESTE = "na_ceste"
    VRACENA = "vracena"
    ZTRACENA = "ztracena"
    PREVZATA = "prevzata"


@dataclass
class ZaznamHistorie:
    stav: StavZasilky
    datum: datetime
    poznamka: Optional[str] = None

@dataclass
class Zasilka:
    id: int
    odesilatel: str
    prijemce: str
    adresa_prijemce: str
    datum_odeslani: datetime
    stav: StavZasilky = StavZasilky.REGISTROVANA
    historie: list[ZaznamHistorie] = field(default_factory=lambda: [])

class EvidenceZasilek:
    def __init__(self):
        self._zasilky: dict[int, Zasilka] = {}

    def _ziskej_zasilku(self, id: int) -> Zasilka:
        if id not in self._zasilky:
            raise ValueError(f"Zásilka s ID {id} neexistuje.")
        return self._zasilky[id]
    
    def _zmen_stav(self, zasilka: Zasilka, novy_stav: StavZasilky, datum: datetime, poznamka: Optional[str] = None):
        if zasilka.stav in {StavZasilky.DORUCENA, StavZasilky.VRACENA, StavZasilky.ZTRACENA}:
            raise ValueError(f"Zásilka je již ukončena.")
        zasilka.stav = novy_stav
        zasilka.historie.append(ZaznamHistorie(stav=novy_stav, datum=datum, poznamka=poznamka))
    
    def registruj_zasilku(self, id: int, odesilatel: str, prijemce: str, adresa_prijemce: str, datum_odeslani: datetime):
        if id in self._zasilky:
            raise ValueError(f"Zásilka s ID {id} již existuje.")
        datum = datum_odeslani or datetime.now()

        self._zasilky[id] = Zasilka(id=id, odesilatel=odesilatel, prijemce=prijemce, adresa_prijemce=adresa_prijemce, datum_odeslani=datum)
    
    def zasilka_prevzata(self, id: int, datum: datetime, poznamka: Optional[str] = None) -> None:
        self._zmen_stav(self._zasilky[id], StavZasilky.PREVZATA, datum, poznamka)

    def zasilka_na_ceste(self, id: int, datum: datetime, poznamka: Optional[str] = None) -> None:
        self._zmen_stav(self._zasilky[id], StavZasilky.NA_CESTE, datum, poznamka)

    def zasilka_dorucena(self, id: int, datum: datetime, poznamka: Optional[str] = None) -> None:
        self._zmen_stav(self._zasilky[id], StavZasilky.DORUCENA, datum, poznamka)

    def zasilka_vracena(self, id: int, datum: datetime, poznamka: Optional[str] = None) -> None:
        self._zmen_stav(self._zasilky[id], StavZasilky.VRACENA, datum, poznamka)

    def zasilka_ztracena(self, id: int, datum: datetime, poznamka: Optional[str] = None) -> None:
        self._zmen_stav(self._zasilky[id], StavZasilky.ZTRACENA, datum, poznamka)

    def historie_zasilky(self, id: int) -> list[ZaznamHistorie]:
        return self._ziskej_zasilku(id).historie
    
    def zasilka_info(self, id: int) -> Zasilka:
        return self._ziskej_zasilku(id)
