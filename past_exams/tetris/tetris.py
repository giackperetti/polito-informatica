BOLD = "\033[1m"
RESET = "\033[0m"


def leggi_mosse(path):
    mosse = []
    with open(path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    i = 0
    while i < len(lines):
        if lines[i]:
            row, col = map(int, lines[i].split(","))

            tetramino = []
            for j in range(1, 5):
                tetramino.append(lines[i + j])

            mosse.append({"row": row, "col": col, "tetramino": tetramino})
            i += 5
        else:
            i += 1

    return mosse


def crea_board(righe=6, colonne=8):
    return [[" " for _ in range(colonne)] for _ in range(righe)]


def piazza_tetramino(board, row, col, tetramino):
    rows = len(board)
    cols = len(board[0])

    for i in range(4):
        for j in range(4):
            if tetramino[i][j] == "1":
                board_row = row + (3 - i)
                board_col = col + j

                if board_row >= rows:
                    return False

                if board_col < cols and board_row >= 0:
                    board[board_row][board_col] = "x"

    return True


def pulisci_righe(board) -> int:
    righe_rimosse = 0
    colonne = len(board[0])

    i = 0
    while i < len(board):
        if all(elem == "x" for elem in board[i]):
            board.pop(i)
            righe_rimosse += 1
        else:
            i += 1

    while len(board) < 6:
        board.append([" " for _ in range(colonne)])

    return righe_rimosse


def stampa_board(board):
    for row in reversed(board):
        print("|" + "".join(row) + "|")
    print("-" * 10)
    print()


def tetris(path):
    mosse = leggi_mosse(path)
    board = crea_board()  # (0,0) è l'angolo in basso a sinistra
    punteggio = 0

    for i, mossa in enumerate(mosse):
        piazzato = piazza_tetramino(
            board, mossa["row"], mossa["col"], mossa["tetramino"]
        )

        if not piazzato:
            print(f"Mossa: {i+1}, Punteggio: {punteggio}")
            stampa_board(board)
            print("Mi dispiace, hai perso")
            return

        righe_rimosse = pulisci_righe(board)
        punteggio += righe_rimosse * 10

        print(f"Mossa: {i+1}, Punteggio: {punteggio}")
        stampa_board(board)

    print("Congratulazioni, hai vinto!")


def main() -> None:
    paths = ["./data/tetraminoes.txt", "./data/tetraminoes2.txt"]

    for path in paths:
        print(f"{BOLD}Partita del file: {path}{RESET}")
        tetris(path)
        print()


if __name__ == "__main__":
    main()
