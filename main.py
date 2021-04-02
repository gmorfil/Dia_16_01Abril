#ingresar textos aplicando write
armorfil= open('ejemplo.txt', 'w+')
armorfil.write("hola mundo \n")
armorfil.write("no me dejes ir. \n")
armorfil.write("entre mas peligro mejor. ")
armorfil.close()

# devuelvo el texto en una lista aplicando readlines
armorfil=open("ejemplo.txt", "r")
texto=armorfil.read()
li_armorfil=armorfil.readlines()
armorfil.close()
print(li_armorfil)
print(texto)

#devuelvo el texto en una lista y imprimo algunos valores de la lista
armorfil=open("ejemplo.txt","r")
li_armorfil=armorfil.readlines()
armorfil.close()
print(li_armorfil)

print(li_armorfil[-3])
print(li_armorfil[0:-1])

# se coloca el puntero en la posicion 8 y se imprime de ahi hacia atras
armorfil=open("ejemplo.txt","r")
print(armorfil.read(8))
 
#se situa en la posicion 45 y imprime de ahi en adelante el texto
armorfil=open("ejemplo.txt","r")
armorfil.seek(45)
print(armorfil.read())

# ingreseo una linea de texto despuesde la posicion 5
armorfil=open("ejemplo.txt","r+")
ingmorfil=armorfil.readlines();
ingmorfil[0]="correo loco \n"
armorfil.seek(5)
armorfil.writelines(ingmorfil)
armorfil.close()
