def leggi_artisti(nome_file):
    artisti = []
    with open(nome_file, "r", encoding="utf-8") as file:
        for line in file:
            codice, file = line.rstrip().split(";")
            artisti.append({"codice": codice, "file": f"./data/{file}"})
    return artisti


def leggi_brani_artista(artista):
    brani = []
    with open(artista["file"], "r", encoding="utf-8") as file:
        for line in file:
            anno, titolo = line.rstrip().split(";")
            brani.append(
                {"codice": artista["codice"], "anno": int(anno), "brano": titolo}
            )
    return brani


def stampa_per_anni(brani):
    anno = 0

    for brano in brani:
        if brano["anno"] != anno:
            anno = brano["anno"]
            print(f"Anno {anno}:")
        print(f'{brano["brano"]:30s}{brano["codice"]}')


def main():
    artisti = leggi_artisti("./data/artisti.txt")
    brani = []

    for artista in artisti:
        brani_artista = leggi_brani_artista(artista)
        brani.extend(brani_artista)

    brani.sort(key=lambda brano: brano["anno"])

    stampa_per_anni(brani)


if __name__ == "__main__":
    main()
