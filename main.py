from parking_lot import Parcare

def meniu():
    parcarea = Parcare()

    while True:
        print("\n--- Meniu Parcare ---")
        print("1. Parcare masina")
        print("2. Plecare masina")
        print("3. Status parcare")
        print("4. Iesire")
        print("5. Exportă status parcare în fișier text")

        opt = input("Alege o optiune: ")
        if opt == "1":
            nr = input("Numar inmatriculare: ")
            loc = int(input("Loc dorit: "))
            parcarea.parcare_masina(nr, loc)
        elif opt == "2":
            nr = input("Numar inmatriculare: ")
            parcarea.plecare_masina(nr)
        elif opt == "3":
            parcarea.status()
        elif opt == "4":
            break
        elif opt == "5":
            parcarea.exporta_status_pe_desktop()
        else:
            print("Optiune invalida.")

if __name__ == "__main__":
    meniu()