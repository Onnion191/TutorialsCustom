#Funcio llegir Fitxer:
def llegirFitxer(NomFitxer): 
    fitxer = open(NomFitxer,"r"); # Obrim el fitxer
    contingut = fitxer.readlines(); # Llegim el contingut i ens retorna una llista
    fitxer.close(); # Tanquem el fitxer
    return contingut; # retornem el contingut del fitxer

#Funcio escriure Fitxer: Nom fitxer = nom del fitxer a escriure // text = text per escriure al fitxer.
def escriureFitxer(NomFitxer, text): 
    fitxer = open(NomFitxer,"a"); #obrim el fitxer
    fitxer.write(text); #Escrivim el text
    fitxer.close(); #Tanquem el fitxer

#Funcio eliminarCapcalera 
 # donada una llista, elimina la primera posicio
 # exemple: [ ABC , CDF , GFT ] --> [ CDF , GFT ]
def eliminarCapcalera(llista): 
    llista.pop(0); #elimina la primera posicio 
    return llista; 

# Funcio dividirText: 
# Divideix el text en grups de n elements. 
# text = text que vols dividir
# num_grups = de quants elements vols que siguin els grups
def dividirText(text, elementsDinsGrup, afeirRestants = False): 

    grupsPossibles = len(text)//elementsDinsGrup; #Calculem quants grups podem fer sencers
    llista = []
    for i in range (0,grupsPossibles): 
        nouGrup = text[ elementsDinsGrup*i : elementsDinsGrup*i+elementsDinsGrup ]; 
        llista.append(nouGrup); #L'afegim

    if(afeirRestants):
        elementsQuefalten = len(text) - grupsPossibles*elementsDinsGrup; #Ha quedat algun element sense agrupar? 
        if(elementsQuefalten > 0):
            llista.append(text[len(text)-elementsQuefalten : len(text)])
        
    return llista; 

# Funcio generarDiccionariADN_AMINO 
# Crea el diccionari que relaciona el fitxer 2 amb el 3. 
def generarDiccionariADN_AMINO (llistaADN, llistaAmino):
    diccionari = {}; 
    min = len(llistaADN); 
    if(len(llistaADN) > len(llistaAmino)): #Aixo nomes es de control
         min = len(llistaAmino);

    for i in range(0,min):  
        diccionari[ llistaADN[i] ] = llistaAmino[i]; #Afegim el nou element

    return diccionari;



#Entrat un text en format [ A UAT CDF GFG ] forma {A= [ UAT CDF GFG ] }
# i ho afegeix al diccionari
def llegirAminoICodo(text, diccionari): 
   llista = text.split(); #Separem per parts
   clau = llista.pop(0); #Treiem la primera 

   dic = diccionari; #Generem un nou diccionari actualitzat
   dic[clau] = llista; #Ens guardem els valors
   return dic; #Tornem el nou diccionari

#Funcio generarDiccionariCodo
# li enviem el contingut del fitxer 1
def generarDiccionariCodo(text): 
    diccionari={} #Creem un nou diccionari
    for i in text: #Per cada [A AID AOD AAS] fem una nova entrada la diccionari
            diccionari = llegirAminoICodo(i,diccionari);#Actualitzem el diccionari

    return diccionari;


#Funcio generarDiccionariPercentatge
# Li entrem la llista de claus del diccionari AMINO_ADN ja que alla tenim tots els codols
# Creem el nou diccionari amb el valor 0 de % perque encara no hem calculat res
def generarDiccionariPercentatge(llista_claus):
    diccionari={}; 
    for i in llista_claus: 
        diccionari[i] = 0;
    return diccionari;


# Funcio omplirDiccionariPercentatge
# Donada una la llista d'adn ja separada en grups de 3, anem mirant quants cops surten els codols
# NOTA: SUMEM ELS COPS QUE SURTEN, ENCARA NO CALCULEM ELS %
def omplirDiccionariPercentatge(diccionari, DNA): 

    for codo in DNA: #Per cada codo
        if codo in diccionari: #Si el codo existeix al diccionari (En prinicpi per forsa ha d'exisitir pero millor comprovar)
            diccionari[codo] +=1; #Afegim que l'hem trobat un cop mes

    return diccionari;

# Funcio CalcularIMostrarPercentatges
# Com ja sabem quants cops ha sortit cada codo, i quines son les regles de traduccio codo - amino 
# podem calcular el bias de cada amino
def CalcularIMostrarPercentatges(diccionari_perc, diccionari_Codons): 
    #Variables per poder mostrar per pantalla de forma bonica
    AminoActual = None; 
    CodoActual = None;
    percent = None; 

    llistaAmino = diccionari_Codons.keys();
    for Amino in llistaAmino: #Recordem que aquest diccionari esta en format { A = [TTA ASE DSF EWS] , B = [OEW PWE] }
        sumTotal = 0;
        for codo in diccionari_Codons[Amino]: #Per cada codo que forma l'aminoacid [TTA ASE DSF EWS] 
            sumTotal += diccionari_perc[codo]; #Quants codons hi ha en total

        #Mostrem per pantalla       
        print(Amino+":"); 
        for codo in diccionari_Codons[Amino]: 
            TextAMostrar = "\t"+codo+":\t"+str(diccionari_perc[codo]*100 / sumTotal)+"%";
            print(TextAMostrar); 



#Programa Principal: 

#LLegim els fitxers
ADN = llegirFitxer("FitxerADN.txt"); 
AMINO = llegirFitxer("FitxerAmino.txt"); 
CODONS = llegirFitxer("FitxerCodons.txt");
#treiem la capalera
ADN = eliminarCapcalera(ADN); 
AMINO = eliminarCapcalera(AMINO);
#Dividim el text
llistaADN = dividirText(ADN[0],3); 
llistaAMINO = dividirText(AMINO[0],1);
#Creem el diccionari
diccionari_ADN_AMINO = generarDiccionariADN_AMINO(llistaADN,llistaAMINO);#Generem el diccionari

#Fem el diccionari de codons [ A USS ASD SOD ]
diccionari_CODONS = generarDiccionariCodo(CODONS)

#=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
#DISCLAIMER: HO ESTIC FENT SENSE L'ENUNCIAT A DAVANT, A PARTIR D'AQUI POT SER QUE S'HAGI DE MODIFICAR UNA MICA
#=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*

#Fem el tercer diccionari per calcular el bias PD
diccionari_PERCENTATGE = generarDiccionariPercentatge(diccionari_ADN_AMINO.keys());
#Omplim el diccionari de %
diccionari_PERCENTATGE = omplirDiccionariPercentatge(diccionari_PERCENTATGE,llistaADN);

#=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
#   INICI ZONA COMPROVACIO == AQUESTES INSTRUCCIONS S'HAN D'ESBORRAR AL FINAL JA QUE NOMES SON PER VEURE QUE ESTEM FENT LES COSES BÉ
#   Print perque veieu com son els diccionaris fets fins el moment
print (diccionari_ADN_AMINO); 
print(diccionari_CODONS);
print (diccionari_PERCENTATGE);#Perque veieu que ha calculat. 
#   FI ZONA COMPROVACIO A PARTIR D'AQUI JA NO S'HA D'ESBORRAR RES MES
#=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*


CalcularIMostrarPercentatges(diccionari_PERCENTATGE,diccionari_CODONS); 


