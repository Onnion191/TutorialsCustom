#Funcions
def EntradaUsuari():
    x = input("Entra un enter \n >>> "); 
    return x

def EsEnter(variable):
   return  isinstance(variable,int);

def ConstruirInvers(numero): 
    auxiliar = numero; #Fem una copia perque hem de manipular la variable
    nombreInvers = 0; #Inicialitzem el nombre invers

    while(auxiliar > 9): #Quin error hi ha? 
        nombreInvers = nombreInvers*10 + auxiliar%10;
        auxiliar /=10; 


    nombreInvers = nombreInvers*10 + auxiliar;

    return nombreInvers;
        

#PROGRAMA
userInput = EntradaUsuari();

if(EsEnter(userInput)): #Comprovem que sigui un enter
    invers = ConstruirInvers(userInput);
    if(invers == userInput):
        print("Es capICua"); 
    else:
        print ("No es capICua");

else: 
    print("No has entrat un enter");

