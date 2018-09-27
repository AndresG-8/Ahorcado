frase = "esto es una frase"
frase2 = "____ __ ___ _____"

print(frase)
print(frase2)

#tomo las dos caddenas y las paso a listas
#comparo en que posicion de la cadena1 es igual a la letra obtenida
#luego reemplazo en esa posicion la cadena2 con la letra que llega
#y nuevamente retorno el string 
#para retornar el string toca ir letra a letra y añadiendo a la cadena2
#lo de la lista

lista1 = list(frase)
lista2 = list(frase2)
letra="a"

print(lista1[10])
for i in range(len(lista1)):
	#si hay letra igual a la ingresada
	if (lista1[i] == letra):
		print("entra al si con i=",i)
		#que la reemplace en la posicion correspondiente
		lista2.insert(i, lista1[i])


print(lista1)
print(lista2)

print("ahora reemplazar la frase con la lista", frase2)
frase2=""
for i in lista2:
	frase2=frase2+i

print(frase2)

#for i in range(len(frase)):
#	print(frase2[i])

# frase = frase.replace("_", "e")

# print(frase)