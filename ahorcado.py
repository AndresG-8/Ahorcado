import figuras as fig
import re as regex

class Ahorcado(object):
	"""docstring for Ahorcado"""
	"""Esta version tiene la palabra prefeiniida, por ende esta seria la primera version"""
	#frase_re = ""
	
	def __init__(self):
		super(Ahorcado).__init__()

	#establece como variable de clase la frase que se le envia
	def setFrase(self, frase):
		self.frase = frase

	#devuelve la frase, la cual esta almacenada como variable de clase
	def getFrase(self):
		return self.frase
	
	#a la frase le quita los espacios laterales y la pone toda en mayuscula
	def sanitizar(self, frase):
		limpiar = frase.strip()
		limpiar = limpiar.upper()
		return limpiar
	
	#contar la cantidad real de letras
	def cant_letras(self, frase):
		#una lista nueva que guarde cada letra
		letras = []
		#recorra la frase letra a letra
		for i in frase:
			#si la letra ya esta en el array nuevo o si es un espacio, que siga
			if(i in letras or i == " "):
				#print("repetida",i)
				pass
			#si no esta en letras que lo guarde
			else:
				#print(frase.count(i))  --esto cuenta la cantidad de letras que hayan en la frase
				#se agrega la letra al array
				letras.append(i)
	 	#retorna la cantidad de letras diferentes en el array
		return len(letras)

	#reemplazo inicial de letras por guiones bajos
	def letras_x_guiones(self, frase):
		#reemplaza cada letra por un guion bajo
		self.frase_re = regex.sub("[A-Za-z]","_", frase)
		return self.frase_re

	#reemplazo de guin por letra ingresa 
	def reemplazo_letra(self, letra):
		lista1 = list(self.frase)
		lista2 = list(self.frase_re)
		#bandera local para verificar si esta o no
		bandera=False
		#Busque en la frase letra a letra
		for i in range(len(lista1)):
			#si hay letra igual a la ingresada
			if (lista1[i] == letra):
				#que la reemplace en la posicion correspondiente
				lista2.insert(i, lista1[i])
				bandera=True

		self.frase_re=""
		for i in lista2:
			self.frase_re=self.frase_re+i
		return bandera

#el programa inicia por acá
if __name__=="__main__":
	#crea el objeto
	ahorcado = Ahorcado()
	#establece la frase
	ahorcado.setFrase("Adivina adivinador")
	#verifica que la frase tenga caracteres validos (letras y espacios unicamente)
	if (regex.search("^[a-zA-Z ]+$", ahorcado.getFrase())):
		#Sanitizar: quitar espacios laterales y poner en mayusculas y establecerla nuevamente
		ahorcado.setFrase(ahorcado.sanitizar(ahorcado.getFrase()))
		#Contar la cantidad de caracteres
		print("Cantidad de caracteres:", len(ahorcado.getFrase()))
		#contar la cantidad real de letras 
		print("Cantidad de letras:", ahorcado.cant_letras(ahorcado.getFrase()))
		#reemplazar las letras por guiones y los espacios dejarlos igual
		print("estado:", ahorcado.letras_x_guiones(ahorcado.getFrase()))
		

		#ingresar una letra 
		letra = input("Ingrese una letra (o frase completa):")
		#quita los espacion y la pone en mayuscula
		letra = ahorcado.sanitizar(letra)
		#verifica que sea una sola letra 
		if ( regex.search("^[a-zA-Z]$",letra) ):
			#ahora se busca la letra que ingresó si esta o no en la frase y la reemplaza
			if (ahorcado.reemplazo_letra(letra)):
				print(ahorcado.frase_re)
				#GANA Y SE DEJA EL MUÑECO TAL CUAL
			else:
				#PIERDE UN PUNTO
				print("PIERDE UN PUNTO, LETRA NO COINCIDE")
		#sino es una letra sino la frase completa
		elif(letra == ahorcado.getFrase()):
			print("Haz ganado, frase completada WINNER")
			#GANA Y SE ACABA LA RONDA, NUEVA FRASE
		#sino es un acierto, pierde un punto y muestra ahorcado un nivel mas
		else:
			#PIERDE UN PUNTO
			print("Debe ingresar un letra o la frase completa respetando espacios:", letra)

			
	#else de la frase con caracteres validos
	else:
		print(ahorcado.getFrase(), "no es una frase valida.")
	

#deberia guardar en una lista las letras que el usuario ya ha ingresado
#para asi darle la opcion de que ingrese otra que no sea esa misma
#a modo recordatorio