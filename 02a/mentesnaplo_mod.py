"""
File
    mentesnaplo_mod.py
Feladat
    A mentés applikáció napló kezelése.
    A naplóban a bejegyzések sorszámozva vannak. Ehhez a 'z9package.z9seq_mod'
    csomagot használjuk. Az aktuális sorszámot a 'mentes_sorszam.cfg' file-ban
    tároljul.
    A napló file nevét paraméterként kapja a 'naplozas_init()' függvény. A naplózás
    beállításait a 'z9log.cfg' tartalmazza ha létezik. Ha nem létezik, akkor
    default beállítások lépnek életbe.
Fejlesztő
    zavorszky@yahoo.com
Létrehozás
    2024.05.xx
"""

import menteshiba_mod as mhm
import z9packages.z9seq.z9seq_mod as sm
import z9packages.z9log.z9log_mod as lm


def naplozas_init(p_logfile_nev: str) -> lm.Naplo:
    """
    Felkészülés a naplózásra:
    1) sorszám szakítás
    2) naplózási paraméterek beállítása
    """
    SEQ_NEV = "mentes_sorszam.cfg"
    # PRGLOGFILE_NEV =

    # Sorszám a naplózáshoz
    # ---------------------

    try:
        ssz = sm.Sorszam(p_file_nev=SEQ_NEV)
    except Exception as e:
        raise mhm.H_Sorszam_KonfigOlvasasa(SEQ_NEV) from e

    sorszam: int = ssz.kovetkezo()

    try:
        ssz.valtozasMentes()
    except Exception as e:
        raise mhm.H_Sorszam_KonfigIrasa(SEQ_NEV) from e

    # A napló előkészítése
    # --------------------

    try:
        naplo = lm.Naplo(
            p_logger_name=__name__,
            p_logfile_name=p_logfile_nev,
            p_sorszam=sorszam,
        )
    except Exception as e:
        raise mhm.H_Naplozas_Elokeszites(
            p_logger_name=__name__, p_file_nev=p_logfile_nev, p_sorszam=sorszam
        ) from e
    return naplo
