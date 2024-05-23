import random
import matplotlib.pyplot as plt

# Chiedi il numero di squadre
num_squadre = int(input("Inserisci il numero di squadre: "))

# Crea una lista per memorizzare i nomi delle squadre
nomi_squadre = []

# Chiedi i nomi delle squadre
for i in range(num_squadre):
    nome_squadra = input(f"Inserisci il nome della squadra {i+1}: ")
    nomi_squadre.append(nome_squadra)

# Crea un dizionario per memorizzare i punti delle squadre
punti_squadre = {nome: 0 for nome in nomi_squadre}

# Simula le partite del campionato
for i in range(len(nomi_squadre)):
    for j in range(i + 1, len(nomi_squadre)):
        squadra1 = nomi_squadre[i]
        squadra2 = nomi_squadre[j]
        
        # Simula un risultato casuale: vittoria, pareggio o sconfitta
        risultato = random.choice(["vittoria1", "pareggio", "vittoria2"])
        
        if risultato == "vittoria1":
            punti_squadre[squadra1] += 3
        elif risultato == "pareggio":
            punti_squadre[squadra1] += 1
            punti_squadre[squadra2] += 1
        elif risultato == "vittoria2":
            punti_squadre[squadra2] += 3

# Ordina le squadre in base ai punti
classifica_finale = sorted(punti_squadre.items(), key=lambda x: x[1], reverse=True)

# Stampa la classifica finale
print("\nClassifica finale:")
for i, (squadra, punti) in enumerate(classifica_finale):
    print(f"{i+1}. {squadra} - {punti} punti")

# Grafica della classifica finale
squadre = [squadra for squadra, punti in classifica_finale]
punti = [punti for squadra, punti in classifica_finale]

plt.figure(figsize=(10, 6))
plt.barh(squadre, punti, color='skyblue')
plt.xlabel('Punti')
plt.title('Classifica finale del campionato')
plt.gca().invert_yaxis()  # Inverti l'asse y per avere il primo in alto
plt.show()
