import random


BOLD = "\033[1m"
ITALIC = "\033[3m"
RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
WHITE = "\033[37m"
MAGENTA = "\033[35m"


def get_valore_carta(original_card):
    if original_card > 10:
        return 10
    return original_card


def get_carta_da_visualizzare(original_card):
    if original_card == 1:
        return "A"
    elif original_card == 11:
        return "J"
    elif original_card == 12:
        return "Q"
    elif original_card == 13:
        return "K"
    else:
        return str(original_card)


def distribuisci_carta(carte_giocatore):
    carta = random.randint(1, 13)
    carte_giocatore.append(carta)


def formatta_mano(carte):
    return "[" + ", ".join(get_carta_da_visualizzare(card) for card in carte) + "]"


def calcola_valore_mano(carte):
    valore = 0
    aces = 0

    for carta in carte:
        if carta == 1:
            aces += 1
            valore += 11
        else:
            valore += get_valore_carta(carta)

    while valore > 21 and aces > 0:
        valore -= 10
        aces -= 1

    return valore


def ha_sballato(carte_giocatore):
    return calcola_valore_mano(carte_giocatore) > 21


def ha_vinto(carte_tavolo, carte_giocatore):
    giocatore_sballa = ha_sballato(carte_giocatore)
    banco_sballa = ha_sballato(carte_tavolo)

    if giocatore_sballa:
        return False
    elif banco_sballa:
        return True
    else:
        return calcola_valore_mano(carte_giocatore) > calcola_valore_mano(carte_tavolo)


def gioca():
    carte_tavolo = []
    carte_giocatore = []
    sta = False
    for i in range(2):
        distribuisci_carta(carte_tavolo)
        distribuisci_carta(carte_giocatore)

    print(
        f"{ITALIC}{CYAN}Il banco ha {RESET}{BOLD}{WHITE}"
        f"{get_carta_da_visualizzare(carte_tavolo[0])}{RESET}"
        f"{ITALIC}{CYAN} e ha una carta nascosta{RESET}"
    )
    print(
        f"{ITALIC}La tua mano: {RESET}{BOLD}{WHITE}{formatta_mano(carte_giocatore)} = "
        f"{calcola_valore_mano(carte_giocatore)}{RESET}"
    )

    if calcola_valore_mano(carte_tavolo) == 21:
        print(f"{BOLD}{RED}Il banco ha fatto Blackjack!{RESET}")
        return
    elif ha_sballato(carte_giocatore):
        print(f"{BOLD}{RED}Hai sballato!{RESET}")
        return

    while (
        (not ha_sballato(carte_giocatore))
        and (not sta)
        and (calcola_valore_mano(carte_giocatore) != 21)
    ):
        scelta = input(
            f"{ITALIC}{YELLOW}Vuoi stare (s) o chiedere (c) [s/c]: {RESET}"
        ).strip()

        match (scelta):
            case "s":
                print(f"{ITALIC}Stai!{RESET}")
                sta = True

                print(
                    f"{ITALIC}{CYAN}Il banco gira la sua seconda carta: "
                    f"{RESET}{BOLD}{WHITE}{get_carta_da_visualizzare(carte_tavolo[1])}{RESET}"
                )
                print(
                    f"{ITALIC}{CYAN}La mano del banco è: {RESET}"
                    f"{BOLD}{WHITE}{formatta_mano(carte_tavolo)}{RESET}{ITALIC}{CYAN} = "
                    f"{RESET}{BOLD}{WHITE}{calcola_valore_mano(carte_tavolo)}{RESET}"
                )

                while calcola_valore_mano(carte_tavolo) < 17:
                    distribuisci_carta(carte_tavolo)
                    print(
                        f"{ITALIC}{CYAN}Il banco ha meno di 17 e ha pescato: "
                        f"{RESET}{BOLD}{WHITE}{get_carta_da_visualizzare(carte_tavolo[-1])}{RESET}"
                    )
                    print(
                        f"{ITALIC}{CYAN}Mano del banco: {RESET}"
                        f"{BOLD}{WHITE}{formatta_mano(carte_tavolo)}{RESET}{ITALIC}{CYAN} = "
                        f"{RESET}{BOLD}{WHITE}{calcola_valore_mano(carte_tavolo)}{RESET}"
                    )
            case "c":
                distribuisci_carta(carte_giocatore)
                print(
                    f"{ITALIC}La tua nuova carta è: {RESET}"
                    f"{BOLD}{WHITE}{get_carta_da_visualizzare(carte_giocatore[-1])}{RESET}"
                )
                print(
                    f"{ITALIC}La tua mano ora è: {RESET}{BOLD}{WHITE}"
                    f"{formatta_mano(carte_giocatore)} = {calcola_valore_mano(carte_giocatore)}{RESET}"
                )
            case _:
                print(
                    f"{ITALIC}{YELLOW}Inserisci una delle due opzioni: " f"s/c{RESET}"
                )

    if ha_sballato(carte_giocatore):
        print(f"{BOLD}{RED}Hai sballato! Il banco vince!{RESET}")
    elif ha_sballato(carte_tavolo):
        print(f"{BOLD}{GREEN}Il banco ha sballato! Vinci tu!{RESET}")
        print(
            f"{ITALIC}{WHITE}(Tu: {calcola_valore_mano(carte_giocatore)} "
            f"vs Banco: {calcola_valore_mano(carte_tavolo)}){RESET}"
        )
    elif ha_vinto(carte_tavolo, carte_giocatore):
        if calcola_valore_mano(carte_giocatore) == 21 and len(carte_giocatore) == 2:
            print(f"{BOLD}{GREEN}🎉 BLACKJACK! VINCI TU! 🎉{RESET}")
        else:
            print(f"{BOLD}{GREEN}Vinci tu!{RESET}")
        print(
            f"{ITALIC}{WHITE}(Tu: {calcola_valore_mano(carte_giocatore)} "
            f"vs Banco: {calcola_valore_mano(carte_tavolo)}){RESET}"
        )
    else:
        print(f"{BOLD}{RED}Il banco vince!{RESET}")
        print(
            f"{ITALIC}{WHITE}(Tu: {calcola_valore_mano(carte_giocatore)} "
            f"vs Banco: {calcola_valore_mano(carte_tavolo)}){RESET}"
        )


def main() -> None:
    print(f"{BOLD}{MAGENTA}---- BLACKJACK ----{RESET}")
    gioca()


if __name__ == "__main__":
    main()
