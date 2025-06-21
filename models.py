from datetime import datetime

class Masina:
    def __init__(self, nr_inmatriculare, timestamp=None):
        # Reprezintă o mașină parcată
        # Salvează numărul de înmatriculare și timpul parcării (implicit timpul curent)
        self.nr_inmatriculare = nr_inmatriculare
        self.timestamp = timestamp or datetime.now()

class LocParcare:
    def __init__(self, numar, masina=None):
        # Reprezintă un loc de parcare, cu număr și mașină asociată (dacă există)
        self.numar = numar
        self.masina = masina

    def este_liber(self):
        # Returnează True dacă locul nu are mașină asociată (este liber)
        return self.masina is None
