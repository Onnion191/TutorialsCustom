
# Definir la funcio llegirFitxer que llegeixi el fitxer que li passem com a parametre
# i retorni una llista amb les linies que el componen.

def LlegirFitxer( nomFitxer ):
    if(not isinstance(s, basestring)): #Comprovem que sigui una string (no es obligatori)
        return;

    fitxer = open(nomFitxer,"r");#Intentem obrir el fitxer
    contingut = fitxer.readlines(); #Llegim les linies
    return contingut; #Retornem el valor

# versio compacte de la funcio anterior.
def LlegirFitxerCompacte( nomFitxer ):
    if (not isinstance(s, basestring)):  # Comprovem que sigui una string (no es obligatori)
        return;
    return open(nomFitxer,"r").readlines();


# Definir la funcio obteColumna que donada una llista que conte cadenes amb n
# valors numerics, i donat un valor entre 0 i n-1 que representa la posicio, retorni
# una llista amb tots els valors (convertits a float) que ocupen la posicio
# demanada.

def ObteColumna(llista, index):
    novaLlista = []; # Creem una nova llista buida
    # llista = [ 60 80 150, 15 2.3 17, 30 0.2 0.3]
    for element in llista: #Agafem el valor/s que hi ha entre "comes"
        #exemple: 60 80 150  // 15 2.3 17// 30 0.2 0.3 (AL LLORO!! AIXO ES TEXT)
        valors_interns = element.split();

        if(index < len(valors_interns)):#Comprovem que no intentem buscar una posicio mes gran de la que tenim
            novaLlista.append( float(valors_interns[index]) ); # HEM DE FER UN CAST PER PODER TENIR EL NUMERO

    return novaLlista;



# Definir valMin que busca el minim d'una llista
def valMin(llista):
    valMin = float("inf");
    for element in llista:
        if(element < valMin):
            valMin = element;

    return valMin;

def valMinCompacte(llista):
    return min(llista);

# Definii funcio posicio maxima de la llista
def posMax(llista):
    valor_maxim = - float("inf");
    for element in llista:
        if(element > valor_maxim):
            valor_maxim = element;

    #valor_maxim = max(llista);
    posicio = llista.index(valor_maxim);
    return posicio;

def posMaxCompacte(llista):
    return llista.index(max(llista));

# Definir la funcio selecNoZero que donades dues llistes retorni una llista amb els
# valors de la primera que a la mateixa posicio de la segona hi ha un valor
# diferent de zero.

def selectNoZero(llistaA , llistaB):
    llistaC = [];
    #Mirem quina es la llista mes petita.
    indexPetit = len(llistaA);
    if(len(llistaB) < indexPetit):
        indexPetit = len(llistaB);

    for i in range(0,indexPetit,1):
        if(llistaB[i]): # 0 = false
            llistaC.append(llistaA[i]);

    return llistaC;

def selectNoZeroCompacte(llistaA , llistaB):
    llistaC = [];
    indexPetit = len(llistaA) if len(llistaA) < len(llistaB) else len(llistaB);
    for i in range(0,indexPetit):
        if(llistaB[i]):
            llistaC.append(llistaA[i]);
    return llistaC;



list = ["60 0.2 150" , "20 15 0.8" , "0.1 0.2 0.3"];
list2 = ObteColumna(list,1);
print list2;
print posMax(list2);

print valMin(list2);



