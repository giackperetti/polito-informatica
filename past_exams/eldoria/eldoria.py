import csv


def leggi_dati(path_creature, path_incantesimi):
    creature = []
    with open(path_creature, "r", encoding="utf-8") as file_creature:
        reader = csv.DictReader(
            file_creature, fieldnames=["id_creatura", "nome", "tipo", "potenza"]
        )
        for row in reader:
            row["id_creatura"] = int(row["id_creatura"])
            row["potenza"] = int(row["potenza"])
            creature.append(row)

    creature.sort(key=lambda c: (c["tipo"], c["nome"]))

    incantesimi = []
    with open(path_incantesimi, "r", encoding="utf-8") as file_incantesimi:
        reader = csv.DictReader(
            file_incantesimi,
            fieldnames=["id_incantesimo", "nome", "tipo", "id_creatura", "potenza"],
        )
        for row in reader:
            if row["tipo"] in ["attacco", "difesa"]:
                row["id_incantesimo"] = int(row["id_incantesimo"])
                row["id_creatura"] = int(row["id_creatura"])
                row["potenza"] = int(row["potenza"])
                incantesimi.append(row)

    incantesimi.sort(key=lambda i: (-i["potenza"], i["nome"]))

    return creature, incantesimi


def analisi_creature(dati_creature, dati_incantesimi):
    for creatura in dati_creature:
        print(
            f"{creatura['nome']} ({creatura['tipo']}, potenza = {creatura['potenza']}):"
        )
        for tipo in ["attacco", "difesa"]:
            print(f"  {tipo.capitalize()}:")
            incantesimi = [
                i
                for i in dati_incantesimi
                if i["id_creatura"] == creatura["id_creatura"] and i["tipo"] == tipo
            ]
            if incantesimi:
                for incantesimo in incantesimi:
                    print(f"    {incantesimo['nome']}: {incantesimo['potenza']}")
            else:
                print("    Nessun incantesimo")


def main() -> None:
    dati_creature, dati_incantesimi = leggi_dati(
        "./data/creature.csv", "./data/incantesimi.csv"
    )

    analisi_creature(dati_creature, dati_incantesimi)


if __name__ == "__main__":
    main()
