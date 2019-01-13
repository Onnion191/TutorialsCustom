#Dictionary #Parella de valors + No repetits + semiFlexible (no es poden eliminar propietats basiques) 

cotxe_props = {"Portes" : 4 , "Marca" : "Ford"} #Propietats basiques

cotxe_props["Cavalls"] = input("Quants cavalls vols que tingui \n >>> "); #Afegim propietats
cotxe_props["Color"] = raw_input("Quin color vols el cotxe? \n >>> "); #Afegim propietats
cotxe_props["GPS"] = raw_input("Vols que tingui GPS? S/N \n >>> ") == "S"; #Afegim propietats


print("El teu cotxe es el seguent: ") #Mostrem els resultats
for x in cotxe_props.keys(): 
    print (x + " : ", cotxe_props[x]); 


#Deixem que l'usuari posi el que vulgi al cotxe
while(raw_input("Vols afegir alguna cosa mes? S/N \n >>> ") == "S"):
    prop = raw_input("Que vols afegir? \n >>> "); 
    cotxe_props[prop] = raw_input("Com ho vols? \n >>>");

#Mostrem el cotxe final
for x in cotxe_props.keys(): 
    print (x + " : ", cotxe_props[x]); 