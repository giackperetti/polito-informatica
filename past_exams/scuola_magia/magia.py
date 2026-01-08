import csv


def leggi_risultati(filepath):
    risultati = []
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for riga in reader:
                nome_cognome = riga["nome"] + " " + riga["cognome"]
                casata = riga["casata"]
                materia = riga["materia"]
                punti = int(riga["punti"])
                risultati.append(
                    {
                        "nome_cognome": nome_cognome,
                        "casata": casata,
                        "materia": materia,
                        "punti": punti,
                    }
                )
    except FileNotFoundError:
        print("Impossibile aprire il file.")
        exit(1)

    return risultati


def calcola_medie(risultati, chiave):
    gruppi = {}
    for record in risultati:
        k = record[chiave]
        if k not in gruppi:
            gruppi[k] = {"totale": 0, "conteggio": 0}
        gruppi[k]["totale"] += record["punti"]
        gruppi[k]["conteggio"] += 1
    for info in gruppi.values():
        info["media"] = info["totale"] / info["conteggio"]
    return gruppi


def media_per_casata(risultati):
    return calcola_medie(risultati, "casata")


def studente_media_max(risultati):
    studenti = calcola_medie(risultati, "nome_cognome")
    nome = max(studenti, key=lambda x: studenti[x]["media"])
    return {"nome_cognome": nome, "media": studenti[nome]["media"]}


def materia_facile_difficile(risultati):
    materie = calcola_medie(risultati, "materia")

    materia_max = max(materie, key=lambda x: materie[x]["media"])
    materia_min = min(materie, key=lambda x: materie[x]["media"])

    return (
        {"materia": materia_max, "media": materie[materia_max]["media"]},
        {"materia": materia_min, "media": materie[materia_min]["media"]},
    )


def statistiche(media_casate, studente_max, materia_facile, materia_difficile):
    print("Media dei punti per casata:")
    for casata in sorted(media_casate.keys()):
        media = media_casate[casata]["media"]
        print(f"- {casata}: {media:.2f}")

    print(
        f"\nStudente con la media più alta: {studente_max["nome_cognome"]} ({studente_max["media"]:.2f})"
    )

    print(
        f"\nMateria più facile: {materia_facile["materia"]} ({materia_facile["media"]:.2f})"
    )

    print(
        f"\nMateria più difficile: {materia_difficile["materia"]} ({materia_difficile["media"]:.2f})"
    )


def main() -> None:
    risultati = leggi_risultati("./data/risultati.csv")
    media_casate = media_per_casata(risultati)
    studente_max = studente_media_max(risultati)
    materia_facile, materia_difficile = materia_facile_difficile(risultati)
    statistiche(media_casate, studente_max, materia_facile, materia_difficile)


if __name__ == "__main__":
    main()
