
print ("This program evaluates your input, if it's a number it returns if it's pair");

entradaUsuari = input("Enter a number \n >>> ");

if(isinstance(entradaUsuari,int)):

    if(entradaUsuari % 2): # 0 = false
        print ("has entrat un enter imparell")
    else: # 1 = true
        print("Has entrta un enter parell")
else: 
    print("No has entrat un enter");
        
    

