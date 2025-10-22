import math


def read_file(file_name):
    file_path = f"./data/{file_name}.txt"

    with open(file_path, "r") as f:
        a, b = map(float, f.readline().strip().split(" "))

        n_values = []
        for line in f:
            n_values.append(int(line.strip()))

    return a, b, n_values


def tartaglia(N: int) -> list[list[int]]:
    triangle = []
    for n in range(N + 1):
        current_row = []
        for k in range(n + 1):
            current_row.append(math.comb(n, k))
        triangle.append(current_row)
    return triangle


def format_term(coeff: float, x_power: int, y_power: int) -> str:
    x_part = f"x^{x_power}" if x_power > 1 else "x" if x_power == 1 else ""
    y_part = f"y^{y_power}" if y_power > 1 else "y" if y_power == 1 else ""

    if x_part and y_part:
        return f"{coeff} {x_part} {y_part}"
    elif x_part:
        return f"{coeff} {x_part}"
    elif y_part:
        return f"{coeff} {y_part}"
    else:
        return f"{coeff}"


def main() -> None:
    a, b, n_list = read_file("potenze")

    print(f"Potenze del binomio ({a}x + {b}y)^N")

    for n in n_list:
        print(f"N = {n}")
        coeffs = tartaglia(n)[n]

        terms = []
        for k in range(n + 1):
            term_coeff = coeffs[k] * (a ** (n - k)) * (b**k)
            x_power = n - k
            y_power = k

            term = format_term(term_coeff, x_power, y_power)
            if term.strip().startswith("-"):
                terms.append(f"({term})")
            else:
                terms.append(term)

        print(" + ".join(terms) + " ")


if __name__ == "__main__":
    main()
