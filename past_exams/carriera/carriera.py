import csv
import math
from datetime import datetime


def leggi_file(path_immatricolazione, path_laurea):
    immatricolati = {}
    laureati = {}

    with open(path_immatricolazione, mode="r") as file_immatricolazione:
        reader = csv.DictReader(file_immatricolazione)
        for riga in reader:
            matricola = int(riga["matricola"])

            data_immatricolazione = datetime.strptime(
                riga["data_immatricolazione"], "%Y-%m-%d"
            ).date()

            immatricolati[matricola] = {
                "nome_cognome": riga["nome"] + " " + riga["cognome"],
                "data_immatricolazione": data_immatricolazione,
            }

    with open(path_laurea, mode="r") as file_laurea:
        reader = csv.DictReader(file_laurea)
        for riga in reader:
            matricola = int(riga["matricola"])

            data_laurea = datetime.strptime(riga["data_laurea"], "%Y-%m-%d").date()

            laureati[matricola] = {
                "nome_cognome": riga["nome"] + " " + riga["cognome"],
                "data_laurea": data_laurea,
            }

    return immatricolati, laureati


def valida_dati(immatricolati, laureati):
    studenti_validi = {}

    for matricola, info in laureati.items():
        if matricola not in immatricolati:
            print(f"Manca la data di immatricolazione di {info["nome_cognome"]}")
            continue

        if info["data_laurea"] < immatricolati[matricola]["data_immatricolazione"]:
            print(
                f"Le date di immatricolazione/laurea di {info["nome_cognome"]} non sono compatibili"
            )
            continue

        studenti_validi[matricola] = {
            "nome_cognome": info["nome_cognome"],
            "data_immatricolazione": immatricolati[matricola]["data_immatricolazione"],
            "data_laurea": info["data_laurea"],
        }

    return studenti_validi


def statistiche_studenti(studenti):
    print("Lista studenti e anni di carriera universitaria:")
    for matricola, info in studenti.items():
        differenza_giorni = (info["data_laurea"] - info["data_immatricolazione"]).days
        anni_carriera = math.trunc(differenza_giorni / 365.25 * 100) / 100
        info["anni_carriera"] = anni_carriera

        print(f"{info["nome_cognome"]}: {anni_carriera:.2f} anni")

    studenti_ordinati = sorted(studenti.values(), key=lambda x: x["anni_carriera"])

    print("\nI 3 studenti più veloci a laurearsi:")
    for info in studenti_ordinati[:3]:
        print(f"{info["nome_cognome"]}: {info["anni_carriera"]:.2f} anni")

    print("\nI 3 studenti più lenti a laurearsi:")
    for info in studenti_ordinati[-3:][::-1]:
        print(f"{info["nome_cognome"]}: {info["anni_carriera"]:.2f} anni")


def main() -> None:
    dati_immatricolati, dati_laureati = leggi_file(
        "./data/immatricolazione.txt", "./data/laurea.txt"
    )

    studenti_validi = valida_dati(dati_immatricolati, dati_laureati)
    print()

    statistiche_studenti(studenti_validi)


if __name__ == "__main__":
    main()
