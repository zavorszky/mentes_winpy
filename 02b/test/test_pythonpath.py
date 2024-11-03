import sys

# import python_packages.z9konfig.mod_konfig as mk # -- Nem OK
import z9konfig.mod_konfig as mk # --OK
# import mod_konfig # -- Nem OK
for elem in sys.path:
    print(elem)
print("mod_konfig verzió:",mk.mod_verzio())
print("OK")

