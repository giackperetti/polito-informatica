import csv
from collections import defaultdict


def leggi_file(filepath):
    spesa_clienti = defaultdict(lambda: {"ordini": 0, "spesa_totale": 0.0})
    prodotti = defaultdict(int)

    with open(filepath, "r") as file:
        reader = csv.DictReader(file)
        for riga in reader:
            if not riga:
                continue

            prodotto = riga["Prodotto"].strip()
            qta = int(riga["Quantità"].strip())
            prezzo = float(riga["Prezzo unitario"].strip())
            cliente = riga["Cliente"].strip()

            spesa = prezzo * qta

            spesa_clienti[cliente]["ordini"] += 1
            spesa_clienti[cliente]["spesa_totale"] += spesa

            prodotti[prodotto] += qta

    return spesa_clienti, prodotti


def elenco_ordini_clienti(spesa_clienti):
    print("Numero di ordini di ciascun cliente:")
    for nome, info in sorted(spesa_clienti.items()):
        print(f"- {nome}: {info["ordini"]}")


def cliente_spesa_max(spesa_clienti):
    nome, info = max(spesa_clienti.items(), key=lambda x: x[1]["spesa_totale"])
    print("Cliente con la spesa totale maggiore:")
    print(f"- {nome}, con un totale di {info['spesa_totale']:.2f} euro.")


def prodotto_unita_min(prodotti):
    prodotto, qta = min(prodotti.items(), key=lambda x: x[1])
    print("Prodotto meno venduto:")
    print(f"- {prodotto}, con {qta} unità vendute.")


def main() -> None:
    try:
        spesa_clienti, prodotti = leggi_file("./data/ordini.csv")
    except FileNotFoundError:
        print("File non trovato!")
        return

    elenco_ordini_clienti(spesa_clienti)
    cliente_spesa_max(spesa_clienti)
    prodotto_unita_min(prodotti)


if __name__ == "__main__":
    main()
