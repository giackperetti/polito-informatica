BOLD = "\033[1m"
RESET = "\033[0m"


def leggi_dati_asta(filepath):
    oggetti = {}
    with open(filepath, "r", encoding="utf-8") as file:
        for riga in file:
            campi = [c.strip() for c in riga.split(",")]
            offerente = campi[0]

            for i in range(1, len(campi), 2):
                oggetto = campi[i]
                offerta = int(campi[i + 1])

                if oggetto not in oggetti:
                    oggetti[oggetto] = {"max": offerta, "offerenti": [offerente]}
                else:
                    record = oggetti[oggetto]
                    if offerta > record["max"]:
                        record["max"] = offerta
                        record["offerenti"] = [offerente]
                    elif offerta == record["max"]:
                        record["offerenti"].append(offerente)

    return oggetti


def risultati_asta(oggetti):
    invenduti = []
    acquistati = {}

    for oggetto, info in oggetti.items():
        max_offerta = info["max"]
        offerenti = info["offerenti"]

        if len(offerenti) > 1:
            invenduti.append(
                {"oggetto": oggetto, "offerta": max_offerta, "offerenti": offerenti}
            )
        else:
            vincitore = offerenti[0]
            acquistati.setdefault(vincitore, []).append(
                {"oggetto": oggetto, "offerta": max_offerta}
            )

    return acquistati, invenduti


def statistica_offerte(acquistati, invenduti):
    for item in invenduti:
        print(
            f"Stessa offerta per {item["oggetto"]} ({item["offerta"]}) da parte di: {", ".join(item["offerenti"])}."
        )

    print()

    massimo_speso = 0
    miglior_offerente = ""

    for offerente in sorted(acquistati):
        lista_acquisti = acquistati[offerente]

        if not lista_acquisti:
            print(f"{offerente}: nessun oggetto aggiudicato")
            continue

        totale = 0
        descrizioni = []

        for oggetto in lista_acquisti:
            descrizioni.append(f'{oggetto["oggetto"]} {oggetto["offerta"]}')
            totale += oggetto["offerta"]

        print(f"{offerente}: {', '.join(descrizioni)}, totale {totale}.")

        if totale > massimo_speso:
            massimo_speso = totale
            miglior_offerente = offerente

    print()
    print(f"L'offerente che ha speso di più è {miglior_offerente}.")


def main() -> None:
    oggetti = leggi_dati_asta("./data/offerte.txt")
    acquistati, invenduti = risultati_asta(oggetti)
    statistica_offerte(acquistati, invenduti)


if __name__ == "__main__":
    main()
