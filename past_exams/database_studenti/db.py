import csv


def leggi_studenti(filepath):
    studenti = []
    with open(filepath, "r") as file:
        reader = csv.DictReader(file)
        for riga in reader:
            studenti.append({
                "ID": int(riga["ID"]),
                "cognome_studente": riga["cognome_studente"],
                "grado": riga["grado"],
                "GPA": float(riga["GPA"]),
            })
    return studenti


def leggi_criteri(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()
        id_ricerca = [int(x) for x in lines[0].strip().split(",")]
        cognome_ricerca = lines[1].strip()
        livello_ricerca = lines[2].strip()
    return {
        "IDs": id_ricerca,
        "cognome": cognome_ricerca,
        "grado": livello_ricerca,
    }


def statistiche(studenti, criteri):
    print("Studenti trovati per ID:")
    [print(studente) for studente in studenti if studente["ID"] in criteri["IDs"]]

    print("\nStudenti trovati per cognome:")
    [print(s) for s in studenti if s["cognome_studente"] == criteri["cognome"]]

    GPAs = [s["GPA"] for s in studenti if s["grado"] == criteri["grado"]]
    print(f"\nMedia del GPA per il grado {criteri['grado']}: {sum(GPAs) / len(GPAs):.2f}")


def main() -> None:
    studenti = leggi_studenti("./data/studenti.csv")
    criteri = leggi_criteri("./data/criteria.txt")
    statistiche(studenti, criteri)


if __name__ == "__main__":
    main()