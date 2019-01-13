#Exemple d'escriptura d'un fitxer

#Obrir el fitxer: 
filename = "FileWrite.txt"; 

#Si el fitxer no existeix es crea sol. 

file = open(filename,"w"); # w = write |a = append | r = read | r+ = read and write (Dangerous)

text = raw_input("Enter the text you want to write \n >>> "); 

file.write(text+"\n");
file.close();
