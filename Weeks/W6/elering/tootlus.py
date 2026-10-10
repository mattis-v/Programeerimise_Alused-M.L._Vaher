"""Hindade sortimine ja kellaajavahemiku järgi otsimine."""
from datetime import datetime, time


def sordi_hinna_jargi(hinnad: dict[datetime, float]) -> dict[datetime, float]:
    """Tagastab sama sõnastiku, järjestatuna odavaimast kallimani.

    sorted() järjestab (aeg, hind) paarid hinna (paari teine element) järgi;
    dict säilitab lisamise järjekorra, seega jääb tulemus sorditud sõnastikuks.
    """
    return dict(sorted(hinnad.items(), key=lambda paar: paar[1]))


def kellaaeg_vahemikus(kell: time, algus: time, lopp: time) -> bool:
    """Kas kellaaeg jääb vahemikku [algus, lopp)? Toetab ka üle kesköö ulatuvat vahemikku (22:00-06:00)."""
    if algus <= lopp:
        return algus <= kell < lopp
    return kell >= algus or kell < lopp


def vahemik(hinnad: dict[datetime, float], algus: time, lopp: time) -> dict[datetime, float]:
    """Tagastab ainult need intervallid, mille kellaaeg jääb antud vahemikku."""
    tulemus = {}
    for aeg, hind in hinnad.items():
        if kellaaeg_vahemikus(aeg.time(), algus, lopp):
            tulemus[aeg] = hind
    return tulemus


def odavaimad_vahemikus(hinnad: dict[datetime, float], algus: time, lopp: time) -> dict[datetime, float]:
    """Kellaajavahemiku hinnad, järjestatuna odavaimast kallimani."""
    return sordi_hinna_jargi(vahemik(hinnad, algus, lopp))
