def leggi_file(filepath_skaters, filepath_skateparks):
    skaters = {}
    skateparks = {}
    with (
        open(filepath_skaters, "r") as file_skaters,
        open(filepath_skateparks, "r") as file_skateparks,
    ):
        for riga in file_skateparks:
            citta, nome_p, difficolta = riga.strip().split(";")
            skateparks[citta] = {"nome": nome_p, "difficolta": int(difficolta)}
        for riga in file_skaters:
            nome, citta, punti_str = riga.strip().split(";")
            if citta in skateparks:
                punti = [int(el) for el in punti_str.split(",")]
                punteggio_medio = sum(punti) / len(punti) if punti else 0.0
                diff = skateparks[citta]["difficolta"]
                skaters[nome] = {
                    "citta": citta,
                    "punteggio_medio": punteggio_medio,
                    "indice_sfida": punteggio_medio * diff,
                }

    return (
        dict(sorted(skaters.items(), key=lambda x: x[1]["indice_sfida"], reverse=True)),
        skateparks,
    )


def ranking(skaters, skateparks):
    print("Ranking Skateboarders:")
    i = 1
    for nome, info in skaters.items():
        print(
            f"{i}. {nome} - Indice di Sfida: {info['indice_sfida']:.2f} - Punteggio medio: {info['punteggio_medio']:.2f}"
        )
        print(
            f"    {info['citta']} - {skateparks[info['citta']]['nome']} (Difficoltà: {skateparks[info['citta']]['difficolta']})"
        )
        i += 1


def main() -> None:
    skaters, skateparks = leggi_file(
        "./data/skateboardersLong.txt", "./data/skateparksLong.txt"
    )
    ranking(skaters, skateparks)


if __name__ == "__main__":
    main()
