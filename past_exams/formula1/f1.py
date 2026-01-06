import csv
from collections import defaultdict


def process_f1_statistics(filepath):
    giri_veloci = defaultdict(int)
    ritirati = defaultdict(int)

    with open(filepath, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for riga in reader:
            if riga["Set Fastest Lap"] == "Yes":
                giri_veloci[riga["Driver"]] += 1

            if riga["Time/Retired"] == "DNF":
                ritirati[riga["Team"]] += 1

    return dict(giri_veloci), dict(ritirati)


def main():
    dati_giri_veloci, dati_ritirati = process_f1_statistics("./data/Formula1_2024season_raceResults.csv")

    if not dati_giri_veloci or not dati_ritirati:
        return

    top_driver = max(dati_giri_veloci, key=dati_giri_veloci.get)
    max_laps = dati_giri_veloci[top_driver]

    top_team = max(dati_ritirati, key=dati_ritirati.get)
    max_retirements = dati_ritirati[top_team]

    print(f"Il maggior numero di giri veloci è {max_laps}, ottenuto da: {top_driver}")
    print()
    print(f"Il maggior numero di ritiri è {max_retirements}, ottenuto da: {top_team}")


if __name__ == "__main__":
    main()
