#concorso pubblico due candidati 
nome = []
print("inserisci i nomi dei due candidati")
a = input()
nome.append(a)
b = input()
nome.append(b)

nome.sort()
print("ecco l'elenco dei nomi dei candidati in ordine alfabetico")
print(nome)

#ora  il punteggio 
voto = []

print("ora inserisci i voti dei due candidati")

votoa = input("il voto di" + a )
voto.append(votoa)
print(votoa)

votob = input("il voto di" + b)
voto.append(votob)
print(votob)

lista = [a, b]
#print(lista)
#ora riordino i candidati secondo i punteggi decrescente 

print ("ecco i candidati secondo i punteggi in ordine decrescente")

if votoa > votob :
    lista.reverse() # se il voto di a è maggiore di b allora darà B, A
    print(lista)
else :
    print(lista) #se il voto di a è minore di b allora darà A,B