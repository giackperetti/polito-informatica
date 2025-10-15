anni = 0
conto = 10_000

while conto < 20_000:
    conto *= 1.05
    anni += 1

print(f"Dopo {anni} anni hai sul conto {conto:.2f}€")