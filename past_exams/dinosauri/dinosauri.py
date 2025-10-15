FILE_NAME = "./data/mazzo.txt"
NUM_CARTE = 30
PUNTEGGI = {"Rosso": 5, "Verde": 3, "Giallo": 1}
BOLD = "\033[1m"
RESET = "\033[0m"


def leggi_mazzo(file_name):
    mazzo = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            if line not in PUNTEGGI:
                print(f"Carta {line} non valida (viene ignorata)")
            else:
                mazzo.append(line)

    if len(mazzo) != NUM_CARTE:
        print(f"Il numero di carte {len(mazzo)} non corrisponde a {NUM_CARTE}")
        return []

    return mazzo


def distribuisci_carte(mazzo):
    giocatore1 = []
    giocatore2 = []
    for i in range(0, len(mazzo), 2):
        giocatore1.append(mazzo[i])
        giocatore2.append(mazzo[i + 1])
    return (giocatore1, giocatore2)


def simula_partita(giocatore1, giocatore2):
    punti1 = punti2 = 0
    tavolo = 0
    conto_mani = 1
    while (len(giocatore1) > 0) and (len(giocatore2) > 0):
        c1 = giocatore1.pop(0)
        c2 = giocatore2.pop(0)
        print(f"{BOLD}Mano n. {conto_mani}{RESET}:")
        print(
            f"\t{BOLD}Carta giocatore 1{RESET}: {c1}\n\t{BOLD}Carta giocatore 2{RESET}: {c2}"
        )
        tavolo = tavolo + PUNTEGGI[c1] + PUNTEGGI[c2]
        if c1 == c2:
            print("\tPareggio")
        elif PUNTEGGI[c1] > PUNTEGGI[c2]:
            print(f"\t{BOLD}Risultato{RESET}: Vince la mano iocatore 1")
            punti1 = punti1 + tavolo
            tavolo = 0
        else:
            print(f"\t{BOLD}Risultato{RESET}: Vince la mano giocatore 2")
            punti2 = punti2 + tavolo
            tavolo = 0
        print(f"\t{BOLD}Punteggio giocatore 1{RESET}: {punti1}")
        print(f"\t{BOLD}Punteggio giocatore 2{RESET}: {punti2}\n")

        conto_mani += 1
    return (punti1, punti2)


def main():
    mazzo = leggi_mazzo(FILE_NAME)
    (giocatore1, giocatore2) = distribuisci_carte(mazzo)
    (punti1, punti2) = simula_partita(giocatore1, giocatore2)
    if punti1 > punti2:
        print(f"Ha vinto il Giocatore 1 con {punti1} punti")
    elif punti2 > punti1:
        print(f"Ha vinto il Giocatore 2 con {punti2} punti")
    else:
        print(f"I giocatori hanno pareggiato con {punti1} punti ciascuno")


if __name__ == "__main__":
    main()
