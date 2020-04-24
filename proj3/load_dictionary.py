"""Modul tworzy liste ze slow ze slownika tekstowego"""
import sys

def load(file):
    """Otworz plik tekstowy i zwroc liste ciagow tekstowych z uzyciem malych liter."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as error:
        print("{}\nError opening {}. Terminating program".format(error, file), file=sys.stderr)
        sys.exit(1)
