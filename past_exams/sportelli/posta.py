def leggi_sportelli(filepath):
    sportelli = {}
    with open(filepath, "r") as file:
        for riga in file:
            riga = riga.strip()
            if not riga:
                continue
            campi = riga.split(",")
            id_sportello = int(campi[0])
            sportelli[id_sportello] = {
                "tasks": campi[1:-1],
                "chiusura": int(campi[-1]),
                "libero": 0,
            }
    return dict(sorted(sportelli.items()))


def leggi_clienti(filepath):
    clienti = []
    with open(filepath, "r") as file:
        for riga in file:
            riga = riga.strip()
            if not riga:
                continue
            campi = riga.split(",")
            clienti.append(
                {
                    "nome": campi[0],
                    "task": campi[1],
                    "tempo": int(campi[2]),
                    "arrivo": int(campi[3]),
                }
            )
    return clienti


def assegna_cliente(sportelli, cliente):
    for id_sportello, info in sportelli.items():
        fine_task = cliente["arrivo"] + cliente["tempo"]

        # Lo sportello non ofrre la task -> skip
        if cliente["task"] not in info["tasks"]:
            continue
        # Lo sportello è occupato all'arrivo del cliente -> skip
        if info["libero"] > cliente["arrivo"]:
            continue
        # Lo sportello chiuderebbe prima della fine del servizio al cliente -> skip
        if fine_task > info["chiusura"]:
            continue

        info["libero"] = fine_task
        return id_sportello, info["libero"]

    return None, None


def main() -> None:
    sportelli = leggi_sportelli("./data/sportelli.txt")
    clienti = leggi_clienti("./data/clienti.txt")

    for cliente in clienti:
        id_sportello, uscita = assegna_cliente(sportelli, cliente)
        if id_sportello:
            print(
                f"{cliente['nome']}. Arrivo: {cliente['arrivo']}. Uscita: {uscita}. Sportello: {id_sportello}"
            )
        else:
            print(
                f"{cliente['nome']} non può essere servito/a. Tutti gli sportelli occupati o chiusi."
            )


if __name__ == "__main__":
    main()
