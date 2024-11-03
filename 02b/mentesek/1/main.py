import sys
import os
import configparser
import re
import mod_kozos_dolgok as koz
import mod_hibak as hib


def main(*p_argv) -> None:
    print(f"{koz.PRG_NEV} (v{koz.PRG_VERZ})")
    print("Indítási argumentumok:")
    for i, elem in enumerate(p_argv[0]):
        print(f"\t {i}. {elem}")

    try:
        print("Argumentum(ok) ellenőrzése:")
        n: int = len(p_argv[0]) - 1
        if n != 1:
            raise hib.H_az_arg_szam_nem_egy(n)

        v_konfig_ffn: str = p_argv[0][1]
        print(f"\tA konfig file neve: '{v_konfig_ffn}'")

        print("A konfig file beolvasása:")
        if not os.path.exists(v_konfig_ffn):
            raise hib.H_a_konfig_file_nem_letezik(v_konfig_ffn)

        cp = configparser.ConfigParser()
        cp.read(v_konfig_ffn)

        v_konfig_ft_valodi: str = cp.get("alap", "ft")
        print(f"\tA konfig file tipusa: '{v_konfig_ft_valodi}'")
        if not v_konfig_ft_valodi == koz.KONFIG_FT:
            raise hib.H_a_konfig_ft_hibas(
                v_konfig_ffn, v_konfig_ft_valodi, koz.KONFIG_FT
            )

        v_csv_ffn: str = cp.get("csv", "ffn")
        print(f"\tA csv file neve: '{v_csv_ffn}'")
        if not os.path.exists(v_csv_ffn):
            raise hib.H_a_csv_file_nem_letezik(v_csv_ffn)
        
        v_log_ffn: str = cp.get("log", "ffn")
        print(f"\tA log file neve: '{v_log_ffn}'")
        match=re.search(koz.ERVENYTELEN_NTFS_KARAKTEREK, v_log_ffn)
        if match:
            raise hib.H_a_log_file_hibas(v_log_ffn, match[0])

        print("\nMentés kész.")
    except (
        hib.H_az_arg_szam_nem_egy,
        hib.H_a_konfig_file_nem_letezik,
        hib.H_a_konfig_ft_hibas,
        hib.H_a_csv_file_nem_letezik,
        hib.H_a_log_file_hibas,
    ) as e:
        print("\t" + hib.hibauzenet(e))
    except Exception as e:
        print(e)


# main()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

if __name__ == "__main__":
    main(sys.argv)
