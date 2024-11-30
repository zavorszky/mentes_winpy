"""
main.py
A mentes_winpy mentést végző program indító/fő programja.
Figyelem!
  A következő csomagoknak a 'pythonpat' környezeti változóban
  szerepelniün kell, hogy a Python interpreter megtalálja őket:
  z9hiba
  z9konfig
  z9log
"""

__version__ = "2.0"

__all__ = []

__author__ = "zavorszky@yahoo.com"


import sys
import logging
import z9hiba.mod_hiba as hib
import z9konfig.mod_konfig as konf
import z9log.mod_log as log
import mod_kozos_dolgok as koz

# Konstansok
# ----------
PRG_NEV: str = "mentes_winpy"
PRG_VERZ: str = "02b"

KONFIG_FT_ERVENYES: str = "mentes_winpy"

KONFIG_LOG_FFN_KULCS1: str = "log"
KONFIG_LOG_FFN_KULCS2: str = "ffn"


# A main modul hiba osztályai
# ---------------------------
class MainHiba_az_arg_szam_nem_egy(IndexError):
    def __init__(self, p_arg_szam: int) -> None:
        self.arg_szam = p_arg_szam
        self.message = (
            f"Hiba:Az indító argumentumok száma '{p_arg_szam}'. Helyes érték: 1."
        )
        super().__init__(self.message)


class MainHiba_nem_sikerult_a_log_fn_kiolvasasa(Exception):
    def __init__(self, p_kulcs1: str, p_kulcs2: str) -> None:
        self.kulcs1 = p_kulcs1
        self.kulcs2 = p_kulcs2
        self.message = f"Hiba:A konfig állományból nem sikerült kiolvasni a log file nevét. Kulcs1='{p_kulcs1}', kulcs2='{p_kulcs2}'."
        super().__init__(self.message)


# Főprogram
# ---------
def main(*p_argv) -> None:
    print(f"{PRG_NEV} (v{PRG_VERZ})")
    print("Indítási argumentumok:")
    for i, elem in enumerate(p_argv[0]):
        if i > 0:
            print(f"\t {i}. {elem}")

    try:
        print("Argumentum(ok) ellenőrzése...")
        n: int = len(p_argv[0]) - 1
        if n != 1:
            raise MainHiba_az_arg_szam_nem_egy(n)

        v_konfig_ffn: str = p_argv[0][1]
        print(f"\tA konfig file neve: '{v_konfig_ffn}'")

        print("A konfig file beolvasása...")

        konf_kezelo = konf.KonfigRegDBKezelo(v_konfig_ffn, KONFIG_FT_ERVENYES)
        v_logging_config_ffn: str = konf_kezelo.cp.get(
            section=KONFIG_LOG_FFN_KULCS1, option=KONFIG_LOG_FFN_KULCS2
        )

        koz.logger = logging.getLogger("mentes_winpy")

        log.logging_setup(p_logging_config_ffn=v_logging_config_ffn)

        koz.logger.info("*** Naplózás elindult...")

        # Ide jön a mentés

        koz.logger.info("*** Naplózás befejeződött.")
        print("A mentés kész.")
    except (
        MainHiba_az_arg_szam_nem_egy,
        konf.KonfigHiba_a_konfig_file_nem_letezik,
        konf.KonfigHiba_a_konfig_file_olvasasa_sikertelen,
        konf.KonfigHiba_a_konfig_ft_hibas,
        log.Mod_logHiba_konfig_arg_beallitas,
    ) as e:
        print("\t", hib.hibauzenet(e))
    except Exception as e:
        print(hib.hibauzenet(e))


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

if __name__ == "__main__":
    main(sys.argv)
