from datetime import datetime

class Masina:
    def __init__(self, nr_inmatriculare, timestamp=None):
        self.nr_inmatriculare = nr_inmatriculare
        self.timestamp = timestamp or datetime.now()

class LocParcare:
    def __init__(self, numar, masina=None):
        self.numar = numar
        self.masina = masina

    def este_liber(self):
        return self.masina is None