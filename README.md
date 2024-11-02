# Mentés

## Feladat

Adott egy PC egy belső Winchesterrel és egy külsővel.\
A külsőn személyes adatok is vannak és vannak nem személyes adatok is.\
A fenti két típusú adatokat meteni szeretném.

Az érzékeny adatokat egy PenDrive-ra,\
a fontos de nem érzékenyek egy részét szintén PenDrive-ra,\
másik részét Google Drive-ra szeretném menteni.

## Megoldás

Valamilyen szkript nyelven szeretném megoldani a problémát. Először Node.Js-re gondoltam,
de a W3School kurzusa előbb végetért, mint hogy a nekem fontos részhez értem volna. Fizetni a folytatásért pedig nem akartam.

A Python lett a következő választás. Azért is erre gondoltam, mert a rá épülő Django-t is meg szeretném ismerni.

(Amíg a Python szkripthez nem tudok eleget, az egyszerű Win10 Cmd Script-et használok.)

|verzió   | Leírása |
|:-------:|:--------|
| 02a     | #Python #log_file #zipfile (Python module) #csv |
| 02b     | #Python #log_file #7z.exe #csv|

## v 02a

* Stabil verzió: nincs
* Script nyelv: Win CMD/PowerShell, Python
* Tömörítés: zipfile (Python module)
* A (mentendő és a cél könvytár) pároknak a tárolás a **mentestabla.cvs** file-ban.
* Logozás 
    - Script üzenetek írása a képernyőre.
    - A futásról mapló/log file készül, file-onként mutatja\
    a mentés sikerességét, és a végén egy összegzést.
    - A logozásra külön modul készült: z9log_mod.py.\
    Ha módosítani akarjuk a logozást, akkor a "**z9log.cfg**" (encode=utf-8) file-t kell használni.\
    Info
      * [python &raquo; logging.config — Logging configuration &raquo; Configuration file format](https://docs.python.org/3/library/logging.config.html)

## v 02b

* Script nyelv: Win CMD/PowerShell, Python
* Tömörítés: 7z.exe
* A (mentendő és a cél könvytár) pároknak a tárolás a **mentestabla.cvs** file-ban.
* Hívás\
  &gt;python mainmentes log_file csv_táblázat


# Github

Link: [mentes_verziok](https://github.com/zavorszky/mentes_verziok)

# Szerző

Závorszky István\
zavorszky@yahoo.com
