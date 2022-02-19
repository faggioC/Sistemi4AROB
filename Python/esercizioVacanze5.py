nomeFile = input("Inserisci il nome del file: ")
prin, comm = 0, 0
f = open(nomeFile, "r")

righe = f.readlines()

print(f"Numero di righe del file: {len(righe)}")

for riga in righe:
    if "printf" in riga:
        prin += 1
    elif "//" in riga:
        comm += 1

print(f"Numero di prinf presenti: {prin}")

print(f"Numero di commenti presenti: {comm}")

f.close()
