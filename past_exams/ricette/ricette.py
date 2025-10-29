def leggi_file_ingredienti(nome_file: str) -> tuple[list[dict[str, float]], str]:
    ingredienti: list[dict[str, float]] = []
    procedimento = ""
    path = f"./data/{nome_file}.txt"

    try:
        with open(path, "r") as file:
            line = file.readline()

            while "Procedimento:" not in line and line != "":
                stripped_line = line.strip()

                if stripped_line == "Ingredienti:":
                    pass
                elif stripped_line:
                    if ";" in stripped_line:
                        try:
                            nome, quantita_str = stripped_line.split(";", 1)
                            ingredient = {nome.strip(): (float(quantita_str.strip()))}
                            ingredienti.append(ingredient)
                        except ValueError:
                            print(
                                f"Warning: Impossibile interpretare la quantità come numero decimale: {stripped_line}"
                            )
                        except IndexError:
                            print(
                                f"Warning: Riga ingrediente malformata (valore mancante): {stripped_line}"
                            )
                    else:
                        print(
                            f"Warning: Salto riga ingrediente malformata (nessun punto e virgola): {stripped_line}"
                        )

                line = file.readline()

            while line != "":
                stripped_line = line.strip()

                if stripped_line and stripped_line != "Procedimento:":
                    procedimento += stripped_line + " "

                line = file.readline()

    except FileNotFoundError:
        print(f"Errore: File non trovato in {path}")
        return [], ""
    except Exception as e:
        print(f"Si è verificato un errore imprevisto durante la lettura del file: {e}")
        return [], ""

    return ingredienti, procedimento.strip()


def leggi_file_informazioni() -> list[dict[str, float]]:
    cibi = []
    path = f"./data/cibi.txt"

    try:
        with open(path, "r") as file:
            for line in file:
                campi = line.rstrip().split(";")
                if len(campi) >= 3:
                    try:
                        cibo = {
                            "nome": campi[0].strip(),
                            "costo": float(campi[1]),
                            "calorie": float(campi[2]),
                        }
                        cibi.append(cibo)
                    except ValueError:
                        print(
                            f"Warning: Impossibile interpretare costo o calorie per l'alimento: {line.strip()}"
                        )
                else:
                    print(
                        f"Warning: Salto riga informazioni alimento malformata: {line.strip()}"
                    )
    except FileNotFoundError:
        print(f"Errore: File non trovato in {path}")
    except Exception as e:
        print(f"Si è verificato un errore imprevisto durante la lettura del file informazioni: {e}")

    return cibi


def calcola_costo_calorie(
    elenco_ingredienti: list[dict[str, float]], cibi: list[dict]
) -> tuple[float, float]:
    costo = 0.0
    calorie = 0.0

    for ingrediente in elenco_ingredienti:
        nome_ingrediente, quantita_ingrediente = list(ingrediente.items())[0]

        for food in cibi:
            if nome_ingrediente == food["nome"]:
                costo += (quantita_ingrediente / 1000) * food["costo"]
                calorie += (quantita_ingrediente / 1000) * food["calorie"]
                break

    return costo, calorie


def main() -> None:
    ingredienti, procedimento = leggi_file_ingredienti("polenta_concia")
    cibi = leggi_file_informazioni()
    costo, calorie = calcola_costo_calorie(ingredienti, cibi)

    print("--- Ingredienti ---")
    if ingredienti:
        for item in ingredienti:
            for ingredient, quantity in item.items():
                print(f"{ingredient} - {quantity:.3f} g")
    else:
        print("Nessun ingrediente o errore generico.")

    print("\n--- Procedimento ---")
    if procedimento:
        print(procedimento)
    else:
        print("Nessun procedimento o errore generico.")

    print(f"\nNumero di ingredienti: {len(ingredienti)}")
    print(f"Costo totale della ricetta: {costo:.2f} €")
    print(f"Calorie totali della ricetta: {calorie:.1f} kcal")


if __name__ == "__main__":
    main()