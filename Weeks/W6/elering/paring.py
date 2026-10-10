"""Eleringi päev-ette (day-ahead) elektrihinna päring.

API dokumentatsioon: https://dashboard.elering.ee/assets/swagger-ui/index.html
Vastus tuleb 15-minutiliste intervallidena: {'timestamp': unix-aeg, 'price': EUR/MWh}.
"""
from datetime import date, datetime, time

import requests

API = "https://dashboard.elering.ee/api/nps/price"


def paeva_hinnad(paev: date) -> dict[datetime, float]:
    """Tagastab ühe päeva hinnad sõnastikuna {kohalik kellaaeg: hind EUR/MWh}.

    API ootab algus- ja lõpuaega koos ajavööndiga (ISO 8601), lõpp on kaasa arvatud,
    seega küsime 00:00:00 kuni 23:59:59. Vastuse unix-aeg teisendatakse kohalikuks ajaks.
    """
    algus = datetime.combine(paev, time.min).astimezone()
    lopp = datetime.combine(paev, time.max).astimezone()
    vastus = requests.get(API, params={"start": algus.isoformat(), "end": lopp.isoformat()})
    vastus.raise_for_status()

    hinnad = {}
    for kirje in vastus.json()["data"]["ee"]:
        aeg = datetime.fromtimestamp(kirje["timestamp"])
        hinnad[aeg] = kirje["price"]
    return hinnad