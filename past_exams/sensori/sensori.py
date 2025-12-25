from collections import defaultdict
from statistics import mean


def leggi_sensori(filepath):
    sensori = {}
    with open(filepath) as file:
        for riga in file:
            codice, luogo, tipo = riga.strip().split()

            sensori[codice] = {
                "luogo": luogo,
                "tipo": tipo,
                "path_misurazioni": f"./data/sensori/{codice}.csv",
            }

    return sensori


def leggi_misurazioni_sensori(sensori):
    for codice in list(sensori.keys()):
        info = sensori[codice]
        misurazioni = []
        try:
            with open(info["path_misurazioni"]) as file:
                file.readline()
                for riga in file:
                    misurazione = riga.strip().split(",")[2]
                    misurazioni.append(float(misurazione))
        except FileNotFoundError:
            print(f"File non trovato per il sensore: {codice}\n")
            sensori.pop(codice)
            continue

        max_misurazione = max(misurazioni)
        avg_misurazioni = sum(misurazioni) / len(misurazioni)

        info["max_misurazione"] = max_misurazione
        info["avg_misurazioni"] = avg_misurazioni


def statistiche_sensori(sensori):
    valori_per_tipo = defaultdict(list)

    for codice, info in sensori.items():
        print(
            f"{codice}: {info['luogo']} - {info['tipo']} - Media: {info['avg_misurazioni']}"
        )
        valori_per_tipo[info["tipo"]].append(info["avg_misurazioni"])

    id_max = max(sensori, key=lambda k: sensori[k]["max_misurazione"])
    info_max = sensori[id_max]

    medie_per_tipo = {
        tipo: mean(misurazioni) for tipo, misurazioni in valori_per_tipo.items()
    }
    tipo_migliore = max(medie_per_tipo, key=medie_per_tipo.get)

    print(
        f"\nSensore con massima lettura: {id_max} a {info_max['luogo']} - "
        f"{info_max['tipo']} - Valore massimo: {info_max['max_misurazione']}"
    )

    print(
        f"Tipo di sensore con media globale più alta: {tipo_migliore} - "
        f"Media: {medie_per_tipo[tipo_migliore]:.2f}"
    )


def main() -> None:
    sensori = leggi_sensori("./data/sensori.txt")
    leggi_misurazioni_sensori(sensori)
    statistiche_sensori(sensori)


if __name__ == "__main__":
    main()
