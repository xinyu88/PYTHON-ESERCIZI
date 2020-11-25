
#giornata ballottaggio tra due candidati. 
print("ecco i due candidati, Sofia e Alice " )
voto1 =int(input("inserisci il voto del primo candidato cioè di sofia "))
voto2 =int(input("inserisci il voto del secondo candidato candidato cioè di alice"))

somma = voto1 + voto2
print("i voti totali sono", somma)

#calcolo percentuale 
print("ora calcoliamo la percentuale dei candidati")
P1 = (int(voto1/ somma * 100))
P2 = (int(voto2/ somma * 100))
print("il voto di sofia è di ", P1, "%") 
print("il voto di alice è di ", P2, "%") 

#calcolo vincitore
print("allora ...il vincitore è")

if P1 > P2 : 
    print("sofia")
else : 
    print("alice")

