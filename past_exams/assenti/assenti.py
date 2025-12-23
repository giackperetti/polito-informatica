import os


def leggi_prenotazioni(filepath):
    prenotati = {}
    with open(filepath, encoding="utf-8") as file:
        for riga in file:
            campi = riga.strip().split("\t")
            prenotati[campi[0]] = " ".join(campi[1:])
    return prenotati


def leggi_consegne(filepath):
    consegne = set()
    with open(filepath, encoding="utf-8") as file:
        for riga in file:
            campi = riga.strip().split("_")
            matricola = campi[2].removeprefix("S")
            consegne.add(matricola)
    return consegne


def main() -> None:
    ordini = ["primo", "secondo", "terzo", "quarto", "quinto"]
    assenti_per_appello = []
    i = 1

    while True:
        prenotazioni_path = f"./data/prenotazioni/prenotati_appello{i}.txt"
        consegne_path = f"./data/consegne/consegne_appello{i}.txt"
        if not os.path.exists(prenotazioni_path):
            break

        prenotati = leggi_prenotazioni(prenotazioni_path)
        consegne = leggi_consegne(consegne_path)

        assenti = set(prenotati) - consegne
        assenti_per_appello.append(assenti)

        label = ordini[i - 1] if i <= len(ordini) else f"{i}°"
        print(f"Assenti al {label} appello:")
        print(
            "\n".join(
                [
                    f"{matricola} {prenotati[matricola]}"
                    for matricola in sorted(assenti, key=lambda x: prenotati[x])
                ]
            )
        )
        print(f"In totale ci sono: {len(assenti)}\n")
        i += 1

    if assenti_per_appello:
        mai_presenti = set.intersection(*assenti_per_appello)
        print("Matricole degli studenti che non si sono mai presentati a un appello:")
        print("\n".join([matricola for matricola in sorted(mai_presenti)]))


if __name__ == "__main__":
    main()
