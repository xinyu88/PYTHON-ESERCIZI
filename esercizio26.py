#MEDIA STIPENDI
contatore = 0

print("inserire -1  per  termina ")
s = []

while True : #ciclo while termina quando l'utente inserisce -1
    stipendio = int(input("inserisci i stipendi dei dipendenti"))
    if stipendio == -1:
        break  

    else: 
        contatore += 1
        s.append(stipendio)
        somma = sum(s)
        
        
media = somma / contatore 
print ("la media degli stipendi dei dipendenti è", media)  
