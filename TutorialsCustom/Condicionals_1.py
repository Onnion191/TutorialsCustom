#Semafor
def EstatSemafor(estat): 
    if(estat == 0): 
        return "Verd"; 
    elif (estat == 1): 
        return "Taronja"; 
    else:
        return "Vermell";

#Inicialitzem l'estat amb un nombre "aleatori"
estat = input("Entra un nombre aleatori \n >>> ") % 3;

#Un conductor arriba a un semafor, que ha de fer? 
print("El semafor es de color: "+EstatSemafor(estat));
print("El conductor haura de: ");

#Processem (if, elif, else)
if(EstatSemafor(estat) == "Verd"):
    print("Seguir"); 
elif(EstatSemafor(estat) == "Taronja"): 
    print("Frenar"); 
else: 
    print("Parar");
