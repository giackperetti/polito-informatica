import csv
import datetime
from collections import defaultdict


def leggi_dati_aziende(filepath_aziende, filepath_storico):
    dati = {}
    with open(filepath_aziende, "r", encoding="utf-8") as file_aziende:
        reader = csv.DictReader(file_aziende)
        for row in reader:
            dati[row["Symbol"]] = {"settore": row["Sector"], "storico": []}

    with open(filepath_storico, "r", encoding="utf-8") as file_storico:
        reader = csv.DictReader(file_storico)
        for row in reader:
            simbolo = row["Symbol"]
            if simbolo in dati:
                dati[simbolo]["storico"].append(
                    {
                        "data": datetime.datetime.strptime(
                            row["Date"], "%m/%d/%Y"
                        ).date(),
                        "close": float(row["Close"]),
                    }
                )

    return dati


def rendimento_azienda(azienda):
    primo_giorno = azienda["storico"][0]
    ultimo_giorno = azienda["storico"][-1]
    chiusura_primo_giorno = primo_giorno["close"]
    chiusura_ultimo_giorno = ultimo_giorno["close"]

    rendimento = 100 * (
        (chiusura_ultimo_giorno - chiusura_primo_giorno) / (chiusura_primo_giorno)
    )

    return rendimento


def rendimento_medio_settori(dati_aziende):
    settori = defaultdict(list)
    for azienda in dati_aziende.values():
        if azienda["storico"]:
            settori[azienda["settore"]].append(rendimento_azienda(azienda))

    return [
        {"settore": settore, "rendimento": round(sum(rendimenti) / len(rendimenti), 2)}
        for settore, rendimenti in settori.items()
    ]


def main() -> None:
    dati_aziende = leggi_dati_aziende(
        "./data/sp500_companies.csv", "./data/sp500_historical.csv"
    )

    rendimenti_settori = rendimento_medio_settori(dati_aziende)

    for settore in rendimenti_settori:
        print(f"Sector: {settore["settore"]}, Average return: {settore["rendimento"]}%")


if __name__ == "__main__":
    main()
