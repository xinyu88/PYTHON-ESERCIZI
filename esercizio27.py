#entrata cesello autostradale 

print("inserire 0 per terminare")
tempo = 0  #1 giorno
listaveicoli = []

while True : 
    veicoli = int(input("inserire numero veicoli di oggi"))
    if veicoli == 0 : 
        break
    else :
        tempo += 1 
        listaveicoli.append(veicoli)
        

totale = sum(listaveicoli) #calcolo totale veicoli
print("sono passati", totale,"veicoli in", tempo) 

