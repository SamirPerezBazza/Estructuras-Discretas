test="abbbcabcbbbcb" #Cadena de prueba
sa={}#Diccionario, el primer elemento es la subcadena que se
# particiona y su argumento será su sucesor.

#k es la longitud de las subcadenas, ejemplo "hola" con k=2 la particionaria en "ho" y "la"
def encontrar_sucesores(test,k):
    for i in range(len(test)-k):
        pareja=test[i:i+k]
        if i+k+1<=len(test):
            if pareja in sa.keys():
                sa[pareja]=sa[pareja]+","+test[i+k:i+k+1]
            else:
                sa[pareja]=test[i+k:i+k+1]


encontrar_sucesores(test,3)
print(sa)
