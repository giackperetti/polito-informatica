RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
WHITE = "\033[37m"
GREY = "\033[90m"
MAGENTA = "\033[35m"


def riempi_grid(grid):
    with open("./dati/sudoku.dat", "r", encoding="utf-8") as file:
        for i, linea in enumerate(file):
            linea = linea.strip()
            for j, char in enumerate(linea):
                if char != ".":
                    grid[i][j] = int(char)


def is_valido(grid, row, col, val):
    if val in grid[row]:
        return False

    if val in [grid[i][col] for i in range(9)]:
        return False

    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if grid[i][j] == val:
                return False

    if grid[row][col] != 0:
        return False

    return True


def is_completo(grid):
    for row in grid:
        if 0 in row:
            return False
    return True


def stampa_sudoku(grid):

    print(f"{CYAN}{BOLD}   1 2 3 | 4 5 6 | 7 8 9{RESET}")

    for i in range(9):
        if i % 3 == 0 and i != 0:
            print(f"   {CYAN}------+-------+------{RESET}")

        row_str = f"{MAGENTA}{BOLD}{i + 1}){RESET} "
        for j in range(9):
            val = grid[i][j] if grid[i][j] != 0 else f"{GREY}.{RESET}"
            row_str += str(val)

            if (j + 1) % 3 == 0 and j != 8:
                row_str += f" {CYAN}|{RESET} "
            elif j != 8:
                row_str += " "

        print(row_str)
    print()


def main() -> None:
    grid = [[0] * 9 for _ in range(9)]
    riempi_grid(grid)

    print(f"{RED}{BOLD}BENVENUTO A SUDOKU!{RESET}")

    while not is_completo(grid):
        stampa_sudoku(grid)
        mossa = input(
            f"{YELLOW}{BOLD}Inserisci la tua mossa (riga, colonna, valore):{RESET} "
        )

        parts = mossa.strip().split(",")
        if len(parts) != 3 or not all(part.strip().isdigit() for part in parts):
            print(f"{RED}{BOLD}Formato non valido!{RESET}\n")
            continue

        row, col, val = map(int, parts)
        if not (1 <= row <= 9 and 1 <= col <= 9 and 1 <= val <= 9):
            print(f"{RED}{BOLD}Valori fuori intervallo (1-9)!{RESET}\n")
            continue

        row, col = row - 1, col - 1

        if is_valido(grid, row, col, val):
            grid[row][col] = val
            print(f"{GREEN}{BOLD}Mossa valida!{RESET}\n")
        else:
            print(f"{RED}{BOLD}Mossa non valida!{RESET}\n")

    stampa_sudoku(grid)
    print(f"{GREEN}{BOLD}CONGRATULAZIONI! HAI VINTO!{RESET}")


if __name__ == "__main__":
    main()
