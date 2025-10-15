def read_ingredient_files(nome_file: str) -> tuple[list[dict[str, float]], str]:
    ingredients: list[dict[str, float]] = []
    procedure = ""
    file_path = f"./data/{nome_file}.txt"

    try:
        with open(file_path, "r") as file:
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
                            ingredients.append(ingredient)
                        except ValueError:
                            print(
                                f"Warning: Could not parse quantity as float: {stripped_line}"
                            )
                        except IndexError:
                            print(
                                f"Warning: Malformed ingredient line (missing value): {stripped_line}"
                            )
                    else:
                        print(
                            f"Warning: Skipping malformed ingredient line (no semicolon): {stripped_line}"
                        )

                line = file.readline()

            while line != "":
                stripped_line = line.strip()

                if stripped_line and stripped_line != "Procedimento:":
                    procedure += stripped_line + " "

                line = file.readline()

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return [], ""
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return [], ""

    return ingredients, procedure.strip()


def read_information_file() -> list[dict[str, float]]:
    foods = []
    file_path = f"./data/cibi.txt"

    try:
        with open(file_path, "r") as file:
            for line in file:
                campi = line.rstrip().split(";")
                if len(campi) >= 3:
                    try:
                        cibo = {
                            "nome": campi[0].strip(),
                            "costo": float(campi[1]),
                            "calorie": float(campi[2]),
                        }
                        foods.append(cibo)
                    except ValueError:
                        print(
                            f"Warning: Could not parse cost or calories for food: {line.strip()}"
                        )
                else:
                    print(
                        f"Warning: Skipping malformed food information line: {line.strip()}"
                    )
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred while reading the information file: {e}")

    return foods


def calculate_price_calories(
    ingredients_list: list[dict[str, float]], foods: list[dict]
) -> tuple[float, float]:
    cost = 0.0
    calories = 0.0

    for ingredient_item_dict in ingredients_list:
        ingredient_name, ingredient_quantity = list(ingredient_item_dict.items())[0]

        for food in foods:
            if ingredient_name == food["nome"]:
                cost += (ingredient_quantity / 1000) * food["costo"]
                calories += (ingredient_quantity / 1000) * food["calorie"]
                break

    return cost, calories


def main() -> None:
    ingredients, procedure = read_ingredient_files("polenta_concia")
    foods = read_information_file()
    cost, calories = calculate_price_calories(ingredients, foods)

    print("--- Ingredients ---")
    if ingredients:
        for item in ingredients:
            for ingredient, quantity in item.items():
                print(f"{ingredient} - {quantity:.3f} g")
    else:
        print("No ingredients found or an error occurred.")

    print("\n--- Procedure ---")
    if procedure:
        print(procedure)
    else:
        print("No procedure found or an error occurred.")

    print(f"\nNumero di ingredienti: {len(ingredients)}")
    print(f"Total recipe cost: {cost:.2f} €")
    print(f"Total recipe calories: {calories:.1f} kcal")


if __name__ == "__main__":
    main()
