"""Hindade salvestamine faili ja failist tagasi lugemine.

Faili rida: "2026-10-07 00:15;2.88"  ->  aeg ja hind eraldatud semikooloniga.
"""
from datetime import datetime

VORMING = "%Y-%m-%d %H:%M"


def salvesta(hinnad: dict[datetime, float], failinimi: str) -> None:
    """Kirjutab iga intervalli eraldi reale: aeg;hind."""
    with open(failinimi, "w") as f:
        for aeg, hind in hinnad.items():
            f.write(f"{aeg:{VORMING}};{hind}\n")


def loe(failinimi: str) -> dict[datetime, float]:
    """Loeb faili ja teisendab tekstist tagasi õigeteks tüüpideks (datetime, float)."""
    hinnad = {}
    with open(failinimi) as f:
        for rida in f:
            aeg, hind = rida.strip().split(";")
            hinnad[datetime.strptime(aeg, VORMING)] = float(hind)
    return hinnad
