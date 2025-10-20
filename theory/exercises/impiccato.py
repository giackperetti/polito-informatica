BOLD = "\033[1m"
RESET = "\033[0m"

PAROLA_SEGRETA = "python"
parola_guess = "_" * len(PAROLA_SEGRETA)
errori = 0

print(f"{BOLD}Parola da indovinare:{BOLD} {''.join(parola_guess)}")

while errori < 6 and "_" in parola_guess:
    guess = input(f"{BOLD}Inserisci una lettera per scoprire se e' contenuta nella parola:{RESET} ").lower()
    if guess in PAROLA_SEGRETA:
        for i in range(len(PAROLA_SEGRETA)):
            if PAROLA_SEGRETA[i] == guess:
                parola_guess = parola_guess[:i] + guess + parola_guess[i+1:]
        if "_" in parola_guess:
            print(f"{BOLD}Parola da indovinare:{RESET} {''.join(parola_guess)}")
    else:
        errori += 1
        print(f"Errori: {errori}/6")

if "".join(parola_guess) == PAROLA_SEGRETA:
    print(f"{BOLD}Hai indovinato, la parola era:{RESET} {PAROLA_SEGRETA}!")
else:
    print(f"{BOLD}Hai fatto troppi errori{RESET}")
