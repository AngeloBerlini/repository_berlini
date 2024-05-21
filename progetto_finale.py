import random
import matplotlib.pyplot as plt


#chiede all'utente il numero di squadre 
numero_di_squadre = int(input("Inserisci il numero di squadre del campionato: "))

#lista delle squadre
lista_squadre = []

#chiede il nome delle squadre e lo aggiunge alla lista
for i in range (numero_di_squadre):
    nome_squadra = input(f"Enter the name of team {i+1}: ")    
    lista_squadre.append(nome_squadra)

#mette a schermo il nome delle squadre
print("Le squadre sono: ")
for squadra in lista_squadre:
    print(squadra)

#simulazione campionato
punti = [0] * numero_di_squadre
for i in range(numero_di_squadre - 1):
    for j in range(i + 1, numero_di_squadre):
        risultato = random.choice([0, 1, 2])

        if risultato == 0:
            # Pareggio
            punti[i] += 1
            punti[j] += 1

        elif risultato == 1:
            # Vittoria della squadra i
            punti[i] += 3

        else:
            # Vittoria della squadra j
            punti[j] += 3
#classifica finale
classifica = sorted(zip(lista_squadre, punti), key=lambda x: x[1], reverse=True)


plt.bar([i for i in range(numero_di_squadre)], [x[1] for x in classifica], tick_label=[x[0] for x in classifica])
plt.title("Classifica finale")
plt.xlabel("Squadre")
plt.ylabel("Punti")
plt.show()




