"""
Hiba objektumok a mentes_py (v02b) alkalmazáshoz.
"""


class Hiba(Exception):
    pass


class H_az_arg_szam_nem_egy(Hiba):
    def __init__(self, p_arg_szam: int) -> None:
        self.arg_szam = p_arg_szam
        self.message = (
            f"Hiba-1:Az indító argumentumok száma '{p_arg_szam}'. Helyes érték: 1."
        )
        super().__init__(self.message)


class H_a_konfig_file_nem_letezik(Hiba):
    def __init__(self, p_ffn: str) -> None:
        self.ffn = p_ffn
        self.message = f"Hiba-2:A '{p_ffn}' konfig file nem létezik."
        super().__init__(self.message)


class H_a_konfig_ft_hibas(Hiba):
    def __init__(self, p_ffn: str, p_ft_valodi: str, p_ft: str) -> None:
        self.ffn = p_ffn
        self.ft_hibas = p_ft_valodi
        self.ft_jo = p_ft
        self.message = f"Hiba-3:A '{p_ffn}' konfig file tipusa hibás: '{p_ft_valodi}'. A helyes: '{p_ft}'."
        super().__init__(self.message)


class H_a_csv_file_nem_letezik(Hiba):
    def __init__(self, p_ffn: str) -> None:
        self.ffn = p_ffn
        self.message = f"Hiba-4:A '{p_ffn}' csv file nem létezik."
        super().__init__(self.message)


class H_a_log_file_hibas(Hiba):
    def __init__(self, p_ffn: str, p_ervenytelen_karakter: str) -> None:
        self.ffn = p_ffn
        self.message = f"Hiba-5:A '{p_ffn}' log file név hibás. Érvénytelen karakter: '{p_ervenytelen_karakter}'."
        super().__init__(self.message)


class H_Egyeb(Hiba):
    def __init__(self, p_message: str) -> None:
        self.message = "Hiba-99:" + p_message
        super().__init__(self.message)


def hibauzenet(p_kivetel: Exception) -> str:
    # huzenet: str = repr(p_kivetel)
    huzenet: str = str(p_kivetel)
    if p_kivetel.__context__ == None:
        return huzenet
    else:
        huzenet = huzenet + " | " + hibauzenet(p_kivetel.__context__)
        return huzenet
