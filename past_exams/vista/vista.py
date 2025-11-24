def leggi_mappa(mappa):
    with open("./dati/mappa.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                riga = [int(char) for char in line]
                mappa.append(riga)


def sommatoria_differenze(mappa, i, j, quadranti_adiacenti):
    somma = 0
    for elem in quadranti_adiacenti:
        somma += mappa[i][j] - elem

    return somma


def calcola_vista(mappa):
    viste = []
    for i, riga in enumerate(mappa):
        for j, elem in enumerate(riga):
            quadranti_adiacenti = []
            for delta_i in [-1, 0, 1]:
                for delta_j in [-1, 0, 1]:
                    new_i, new_j = i + delta_i, j + delta_j
                    if delta_i == 0 and delta_j == 0:
                       pass 
                    elif 0 <= new_i < len(mappa) and 0 <= new_j < len(mappa[new_i]):
                        quadranti_adiacenti.append(mappa[new_i][new_j])
                    else:
                        quadranti_adiacenti.append(0)
        
            viste.append({"i": i, "j": j, "vista": sommatoria_differenze(mappa, i, j, quadranti_adiacenti)})
            
    return viste

def stampa_viste(viste):
    viste = sorted(viste, key=lambda x: x["vista"], reverse=True)
    for i, elem in enumerate(viste):
        print(f"{i+1} ({elem["i"]}, {elem["j"]}): Valore = {elem["vista"]}")


def main() -> None:
    mappa = []
    leggi_mappa(mappa)
    viste = calcola_vista(mappa)
    stampa_viste(viste)


if __name__ == "__main__":
    main()
