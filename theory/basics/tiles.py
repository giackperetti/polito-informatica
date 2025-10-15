## Posizionare le piastrelle a scacchiera (quasi)
# 1. prima e ultima devono essere nere

# Input:
# - larghezza stanza (cm)
# - larghezza di ogni piastrella (cm)

# Output:
# - numero di piastrelle necessarie
# - il vuoto alle estremità della riga

import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

room_width = int(input("Inserisci la larghezza della stanza (cm): "))
tile_width = int(input("Inserisci la larghezza della piastrella (cm): "))

raw_tiles_number = room_width // tile_width
# logging.debug(f"Numero di piastrelle [a prescindere dal requisito (nero, ..., nero)]: {raw_tiles_number}")

tile_number = (
    (raw_tiles_number - 1)
    if (raw_tiles_number % 2 == 0 and raw_tiles_number > 0)
    else raw_tiles_number
)

print(f"Numero di piastrelle corretto (prima e ultima nere): {tile_number}")

used_space = tile_number * tile_width
side_gap_total = room_width - used_space
side_gap_each = side_gap_total / 2
# logging.debug(f"Gap totale da distribuire: {side_gap_total} cm")

print(f"Gap a ciascun lato: {side_gap_each}cm")

# ## SOLUZIONE BENSO
# lStanza = int(input("Inserisci la larghezza della stanza (cm): "))
# lPiastrella = int(input("Inserisci la larghezza della piastrella (cm): "))

# # print(f"stanza: {lStanza}, piastrella: {lPiastrella}")

# nPiastrelle = lStanza // lPiastrella

# if nPiastrelle % 2 == 0:
#     nPiastrelle -= 1

# lRimanente = lStanza - (nPiastrelle * lPiastrella)

# print(f"Numero piastrelle: {nPiastrelle}")
# print(f"Spazio vuoto su ogni lato: {lRimanente / 2}")