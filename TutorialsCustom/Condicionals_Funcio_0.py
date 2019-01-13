print ("This program evaluates your input, if it's a number it returns if it's pair");
#FUNCIONS
#Funcio per entrar un enter de l'usuari
def EntradaUsuari(): 
    entradaUsuari = input("Enter a number \n >>> ");
    return entradaUsuari;

#Funcio que evalua si el nombre es parell
def EsParell(Enter): 
    if(not isinstance(Enter,int)):#Si no ha enviat un enter, acabem l'execucio de la funcio
        print("No puc evaluar si es parell, perque no hi ha cap enter");
        return False
    return not (Enter %2);   
#FI FUNCIONS


#PROGRAMA
x = EntradaUsuari(); 

if(EsParell(x)): 
    print("Has entrat un parell"); 
else: 
    print("Has entrat un sanar");

#FI PROGRAMA
        
    


