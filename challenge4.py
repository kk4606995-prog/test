#Oppdrag

#Skriv ut gangetabellen opp til 10-gangen
#Hvis tallet du skriver ut er delelig med 7, 
#skriv ut en * bak tallet
#Last opp fila di med ditt navn i filnavnet

#Lykke til.

#%%
tabell_1 = 1
tabell_2 = 1
while tabell_1 <= 10:
        while tabell_2 <= 10:
            print(tabell_1 * tabell_2, end = " ")
            if (tabell_1 * tabell_2) % 7 == 0:
                print("*", end = " ")
            tabell_2 += 1
        print()
        tabell_1 += 1
        tabell_2 = 1
# %%
