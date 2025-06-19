import sqlite3
from datetime import datetime
from models import Masina, LocParcare
import os

class Parcare:
    def exporta_status_pe_desktop(self):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "parcare_status.txt")
        with open(desktop_path, "w") as f:
            for loc, obiect in self.locuri.items():
                if obiect.este_liber():
                    f.write(f"Loc {loc}: Liber\n")
                else:
                    durata = datetime.now() - obiect.masina.timestamp
                    ore = max(1, int(durata.total_seconds() // 3600))
                    taxa = ore * 5
                    f.write(
                        f"Loc {loc}: {obiect.masina.nr_inmatriculare} (de la {obiect.masina.timestamp}, taxa curenta: {taxa} Lei)\n")
        print(f"\nFișierul `parcare_status.txt` a fost salvat pe Desktop.")

    def __init__(self, nr_locuri=100):
        self.nr_locuri = nr_locuri
        self.locuri = {i: LocParcare(i) for i in range(1, nr_locuri+1)}
        self.db_init()
        self.incarca_din_baza()

    def db_init(self):
        self.conn = sqlite3.connect("parcare.db")
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS masini (nr TEXT PRIMARY KEY, timestamp TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS locuri (loc INTEGER PRIMARY KEY, nr TEXT)")
        self.conn.commit()

    def incarca_din_baza(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT loc, nr FROM locuri")
        for loc, nr in cursor.fetchall():
            cursor.execute("SELECT timestamp FROM masini WHERE nr = ?", (nr,))
            rezultat = cursor.fetchone()
            if rezultat:
                masina = Masina(nr, datetime.strptime(rezultat[0], "%Y-%m-%d %H:%M:%S"))
                self.locuri[loc].masina = masina

    def salveaza_in_baza(self):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM locuri")
        cursor.execute("DELETE FROM masini")
        for loc, obiect in self.locuri.items():
            if not obiect.este_liber():
                nr = obiect.masina.nr_inmatriculare
                ts = obiect.masina.timestamp.strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute("INSERT INTO masini (nr, timestamp) VALUES (?, ?)", (nr, ts))
                cursor.execute("INSERT INTO locuri (loc, nr) VALUES (?, ?)", (loc, nr))
        self.conn.commit()

    def parcare_masina(self, nr_inmatriculare, loc):
        if self.locuri[loc].este_liber():
            self.locuri[loc].masina = Masina(nr_inmatriculare)
            self.salveaza_in_baza()
            print(f"Masina {nr_inmatriculare} a fost parcata la locul {loc}. Taxa: 5 Lei.")
        else:
            print("Locul selectat este deja ocupat.")

    def plecare_masina(self, nr_inmatriculare):
        for loc, obiect in self.locuri.items():
            if not obiect.este_liber() and obiect.masina.nr_inmatriculare == nr_inmatriculare:
                durata = datetime.now() - obiect.masina.timestamp
                ore = max(1, int(durata.total_seconds() // 3600))
                taxa = ore * 5
                self.locuri[loc].masina = None
                self.salveaza_in_baza()
                print(f"Masina {nr_inmatriculare} a plecat. Durata: {durata}, Taxa: {taxa} Lei.")
                return
        print("Masina nu a fost gasita in parcare.")

    def status(self):
        for loc, obiect in self.locuri.items():
            if obiect.este_liber():
                print(f"Loc {loc}: Liber")
            else:
                durata = datetime.now() - obiect.masina.timestamp
                ore = max(1, int(durata.total_seconds() // 3600))
                taxa = ore * 5
                print(f"Loc {loc}: {obiect.masina.nr_inmatriculare} (de la {obiect.masina.timestamp}, taxa curenta: {taxa} Lei)")