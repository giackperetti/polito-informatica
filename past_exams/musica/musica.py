import csv


def leggi_file(filepath):
    brani = {}
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for riga in reader:
            compositore = riga["composer"]
            titolo = riga["composition"]
            movimento = riga["movement"]
            formazione_musicale = riga["ensemble"]
            numero_catalogo = riga["catalog_name"]
            durata = int(riga["seconds"])

            if compositore not in brani:
                brani[compositore] = {}

            if numero_catalogo not in brani[compositore]:
                brani[compositore][numero_catalogo] = {
                    "titolo": titolo,
                    "formazione": formazione_musicale,
                    "movimenti": [],
                }

            brani[compositore][numero_catalogo]["movimenti"].append(
                {"nome": movimento, "durata": durata}
            )

    return brani


def interroga_compositore(compositore, catalogo):
    if compositore in catalogo:
        print(f"Opere di {compositore}")
        for id, info in catalogo[compositore].items():
            durata_totale = sum(m["durata"] for m in info["movimenti"])
            n_movimenti = len(info["movimenti"])
            durata_media = durata_totale / n_movimenti if n_movimenti > 0 else 0

            print(f"- {id}: {info["titolo"]}, {durata_totale:.2f} secondi")
            print(f"    {n_movimenti} movimenti, in media {durata_media:.2f} secondi")
    else:
        print(f"Opere di {compositore}")
        print("Compositore non presente in catalogo")

    print()


def interroga_formazione(formazione, catalogo):
    trovato = False
    print(f"Opere con formazione musicale: {formazione}")
    for compositore, opere in catalogo.items():
        for id, info in opere.items():
            if info["formazione"] == formazione:
                print(f"- {compositore}, opera {id}")
                trovato = True
    if not trovato:
        print("Formazione musicale non presente")

    print()


def elabora_richieste(richieste_path, catalogo):
    with open(richieste_path, "r", encoding="utf-8") as file:
        for riga in file:
            riga = riga.strip()
            if not riga:
                continue

            parti = riga.split(":")
            comando = parti[0]
            valore = parti[1]

            if comando == "c":
                interroga_compositore(valore, catalogo)
            elif comando == "s":
                interroga_formazione(valore, catalogo)


def main() -> None:
    catalogo = leggi_file("./data/musicnet.csv")
    elabora_richieste("./data/richieste.txt", catalogo)


if __name__ == "__main__":
    main()
