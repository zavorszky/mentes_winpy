try:
    import context
except ModuleNotFoundError:
    import test.context
from main import __version__
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
print ("main.py version:", __version__)