def leggi_file(file_path):
    punteggi = []

    with open(file_path, "r") as file:
        for line in file:
            campi = line.strip().split(";")
            nome = f"{campi[0]} {campi[1]}"
            punti = [int(campo) for campo in campi[2:]]
            punteggi.append({"nome": nome, "punti": punti, "punti_tot": sum(punti)})

    return punteggi


def classifica(punteggi):
    punteggi.sort(key=lambda d: d["punti_tot"], reverse=True)

    print("Classifica Partita:")
    for giocatore in punteggi:
        print(f"{giocatore["nome"]}: {giocatore["punti_tot"]}")


def max_10_0(punteggi):
    max_10 = {"nome": "", "count": -1}
    max_0 = {"nome": "", "count": -1}

    for giocatore in punteggi:
        conto_10 = 0
        conto_0 = 0
        for punto in giocatore["punti"]:
            if punto == 10:
                conto_10 += 1
            elif punto == 0:
                conto_0 += 1

        if conto_10 > max_10["count"]:
            max_10["nome"] = giocatore["nome"]
            max_10["count"] = conto_10

        if conto_0 > max_0["count"]:
            max_0["nome"] = giocatore["nome"]
            max_0["count"] = conto_0

    print(f"\n{max_10['nome']} ha abbattuto tutti i birilli {max_10['count']} volta/e")
    print(f"{max_0['nome']} ha mancato tutti i birilli {max_0['count']} volta/e")


def main():
    punteggi = leggi_file("./data/bowling.txt")
    classifica(punteggi)
    max_10_0(punteggi)


if __name__ == "__main__":
    main()
