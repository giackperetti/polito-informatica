import csv


def leggi_utenti(filename):
    utenti = []
    with open(f"./data/{filename}", "r") as file:
        reader = csv.DictReader(file, delimiter=";")
        for riga in reader:
            if not riga:
                continue
            utenti.append({"id_utente": int(riga["id_utente"]), "nome": riga["nome"]})

    return utenti

def leggi_follows(filename):
    follows = set()
    with open(f"./data/{filename}", "r") as file:
        reader = csv.DictReader(file, delimiter=";")
        for riga in reader:
            if not riga:
                continue
            follows.add((int(riga["id_follower"]), int(riga["id_followed"])))

    return follows

def numero_utenti(utenti):
    print(f"Numero totale di utenti: {len(utenti)}")


def numero_relazioni_follow(follows):
    print(f"Numero totale di relazioni di follow: {len(follows)}")


def follower_followed_utente(follows, utente):
    follower = 0
    followed = 0
    for relationship in follows:
        if utente["id_utente"] == relationship[0]:
            followed += 1
        if utente["id_utente"] == relationship[1]:
            follower += 1

    return follower, followed


def stampa_tabella_follower_followed(follows, utenti):
    print("id  nome    follower followed")
    for utente in utenti:
        follower, followed = follower_followed_utente(follows, utente)
        print(f"{utente['id_utente']:<3} {utente['nome']:<7} {follower:>1} {followed:>7}")


def relazioni_reciproche(follows):
    reciproche = []
    for relationship in follows:
        opposite = (relationship[1], relationship[0])
        
        if opposite in list(follows):
            follows.remove(relationship)
            follows.remove(opposite)
            reciproche.append(relationship)
        
    return reciproche


def stampa_relazioni_reciproche(follows):
    reciproche = relazioni_reciproche(follows)

    print(f"Numero totale di coppie reciproche: {len(reciproche)}")
    print(f"Coppie: {', '.join([str(rel) for rel in reciproche])}")


def main():
    utenti = leggi_utenti("utenti.csv")
    follows = leggi_follows("follow.csv")

    numero_utenti(utenti)
    numero_relazioni_follow(follows)
    stampa_tabella_follower_followed(follows, utenti)
    stampa_relazioni_reciproche(list(follows))


main()