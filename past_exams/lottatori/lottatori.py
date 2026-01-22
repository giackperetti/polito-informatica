import csv
from random import randint


def leggi_squadra(filepath):
    squadra = {}
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for riga in reader:
            if not riga:
                continue

            nome = riga["nome univoco"].strip()
            punti_vita = int(riga[" punti vita"].strip())
            attacchi = [
                float(riga[" potenza attacco 1"].strip()),
                float(riga[" potenza attacco 2"].strip()),
                float(riga[" potenza attacco 3"].strip()),
            ]

            squadra[nome] = {
                "punti_vita": punti_vita,
                "attacchi": attacchi,
            }
    return dict(sorted(squadra.items(), key=lambda x: x[1]["punti_vita"], reverse=True))


def visualizza_squadra(squadra):
    for nome, info in squadra.items():
        punti_vita = info["punti_vita"]
        attacco1 = info["attacchi"][0]
        attacco2 = info["attacchi"][1]
        attacco3 = info["attacchi"][2]

        print(
            f"{nome}: Punti Vita {punti_vita}, Attacco 1: {attacco1}, Attacco 2: {attacco2}, Attacco 3: {attacco3}"
        )


def scegli_attacco(dati_lottatore):
    indice_attacco = randint(0, 2)
    return indice_attacco, dati_lottatore["attacchi"][indice_attacco]


def simula_combattimento(squadra):
    lottatori = input("Inserire il nome dei combattenti separati da ';': ").split(";")
    if len(lottatori) != 2:
        print("Devi inserire esattamente 2 lottatori")
        return

    try:
        nome_lottatore_1 = lottatori[0].strip()
        dati_lottatore_1 = squadra[nome_lottatore_1]
        nome_lottatore_2 = lottatori[1].strip()
        dati_lottatore_2 = squadra[nome_lottatore_2]
    except KeyError:
        print("1+ lottatori inseriti non sono validi")
        return

    while dati_lottatore_1["punti_vita"] > 0 and dati_lottatore_2["punti_vita"] > 0:
        mossa_lottatore_1, potenza_lottatore_1 = scegli_attacco(dati_lottatore_1)
        print(f"{nome_lottatore_1} attacca con mossa {mossa_lottatore_1}")
        dati_lottatore_2["punti_vita"] -= potenza_lottatore_1

        if dati_lottatore_2["punti_vita"] <= 0:
            break

        mossa_lottatore_2, potenza_lottatore_2 = scegli_attacco(dati_lottatore_2)
        print(f"{nome_lottatore_2} attacca con mossa {mossa_lottatore_2}")
        dati_lottatore_1["punti_vita"] -= potenza_lottatore_2

    if dati_lottatore_1["punti_vita"] > dati_lottatore_2["punti_vita"]:
        print(f"Vince {nome_lottatore_1}")
    else:
        print(f"Vince {nome_lottatore_2}")


def main() -> None:
    squadra = leggi_squadra("./data/squadra.csv")
    visualizza_squadra(squadra)
    print()
    simula_combattimento(squadra)


if __name__ == "__main__":
    main()
