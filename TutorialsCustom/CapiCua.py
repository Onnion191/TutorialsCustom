
#Codi espaguetti

entradaUsuari = input("Entra un enter"); 

if(not isinstance(entradaUsuari,int)):
    print ("No has entrat un enter"); 
    exit();#Fi de l'execucio del programa

#Perque un nombre sigui cap i cua, cal que sigui igual llegit per l'esquerra que per la dreta

#CONSTRUIM EL NOMBRE INVERS

auxiliar = entradaUsuari;
nombreInvers = 0; 

while(auxiliar > 9):    #Quin error hi ha? 
    nombreInvers = nombreInvers*10 + auxiliar%10;
    auxiliar /=10; 

nombreInvers = nombreInvers*10 + auxiliar;

#COMPROVEM CAP I CUA
if(nombreInvers == entradaUsuari):
    print("Es capICua"); 
else:
    print ("No es capICua");
