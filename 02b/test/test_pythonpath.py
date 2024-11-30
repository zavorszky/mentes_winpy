import sys

# import python_packages.z9konfig.mod_z9konfig as mk # -- Nem OK
import z9konfig.mod_z9konfig as mk # --OK
# import mod_z9konfig # -- Nem OK
for elem in sys.path:
    print(elem)
print("mod_konfig verzió:",mk.__version__)
print("OK")

