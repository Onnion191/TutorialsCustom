#Llista Mante ordre + Repetits + flexible

#INICI PROGRAMA
llistaDeLaCompra = ["Doritos ", "Vodka", "Ron", "Cocacola", "Llima"]; #Aixo es una llista. 

print("la teva llsita es: ")
for producte in llistaDeLaCompra: 
    print("\t"+producte);

#INTERACCIO DE L'USUARI

while( raw_input("Has de comprar una cosa mes? S/N \n >>>") == "S"): 
   llistaDeLaCompra.append( raw_input("Que et fa falta? \n >>> ") );
  

#MOSTRA RESULTATS
print("Aquesta es la teva llista de la compra: ")

for producte in llistaDeLaCompra: 
    print("\t"+producte);


#2a INTERACCIO USUARI
while(len(llistaDeLaCompra) and raw_input(  "No hi ha " + llistaDeLaCompra[len(llistaDeLaCompra) -1 ] + " El vols treure de la llista? S/N \n >>>"  )   ==    "S"):
    llistaDeLaCompra.pop();

    #MOSTRA RESULTATS
    for producte in llistaDeLaCompra: 
        print("\t"+producte);

if(not len(llistaDeLaCompra)):
    print("La llista esta buida");