import matplotlib.pyplot as plt
import random


# Crea una lista per memorizzare i nomi delle squadre
campionato = []
# Chiedi i nomi delle squadre
for i in range(20):
    nome_squadra = input(f"Inserisci il nome della squadra {i+1}: ")
    campionato.append(nome_squadra)
    

def simulazione_campionato():
    
    # Crea un dizionario per memorizzare i punti delle squadre
    punti = {squadra: 0 for squadra in campionato}

    for i in range(380): #20 squadre, ognuna gioca 38 partite
            
        squadra_casa,squadra_trasferta = random.sample(campionato,2)

        # Simula un risultato casuale: vittoria, pareggio o sconfitta
        risultato = random.choice(["vittoria1", "pareggio", "vittoria2"])
        
        # Vittoria squadra 1
        if risultato == "vittoria1":
            punti[squadra_casa] += 3

            # Pareggio tra le due squadre   
        elif risultato == "pareggio":
            punti[squadra_casa] += 1
            punti[squadra_trasferta] += 1

        # Vittoria squadra 2
        elif risultato == "vittoria2":
            punti[squadra_trasferta] += 3
    return punti

def visualizzazione_dell_andamento(punti):
    # Ordina le squadre in base ai punti
    classifica_finale = sorted(punti.items(), key=lambda x: x[1], reverse=True)


    # Grafica della classifica finale
    squadre = [squadra[0] for squadra in classifica_finale]
    punti = [squadra[1] for squadra  in classifica_finale]

    plt.figure(figsize=(10, 6))
    plt.barh(squadre, punti, color='skyblue')
    plt.xlabel('Punti')
    plt.title('Classifica finale del campionato')
    plt.gca().invert_yaxis()  # Inverti l'asse y per avere il primo in alto
    plt.show()

punti_stagione = simulazione_campionato()
visualizzazione_dell_andamento(punti_stagione)