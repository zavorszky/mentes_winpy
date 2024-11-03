"""
Parancsori argumentumok beolvasása.
"""

import sys


def main(*p_argv) -> None:
    # A p_argv egy "tuple", amiben egy elem van, egy "list".
    # A "list"-ben van a Python modul név: p_argv[0]
    # és a parancssori argumentumok: p_argv[1], p_argv[2],...
    # A "list"-et a "sys" Python modul szolgáltatja: sys.argv

    print(p_argv)
    
    i = -1
    v_argumentumok = p_argv[0]
    for elem in v_argumentumok:
        # for elem in p_argv[0]:
        i = i + 1
        print(i, elem)

    print("***")

    i = -1
    for elem in p_argv[0]:
        i = i + 1
        print(i, elem)


main(sys.argv)
