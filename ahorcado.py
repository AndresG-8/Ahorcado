import figuras as fig
import diccionario as diccionario
import re as regex
import random

class Ahorcado(object):
	"""docstring for Ahorcado"""
	"""
	Es un juego básico de adivinanzas en el cual dado ciertas caracteristicas el programa determina las
	posibilidades que hay para adivinar la frase.
	Esta es la primera version que se hace y tiene lo siguiente:
	*un solo usuario puede jugar, la idea es hacerlo multiusuario
	*toma las figuras del archivo "figuras.py"
	*toma las frase del archivo diccionario.py
	*el usuario deberá adivinar la frase elegida aleatoriamente
	*el sistema determina la cantidad de intentos según cantidad de letras individuales en la frase
	TODO: 
	*crear el multiusuario para juego enlinea,
	*recoleccion de frases o palabras
	*guardar estadisticas del juego
	*validar que no sean frases muy extensas, de menos de 50 caracteres, su mucho
	*en vez de una lista en el diccionario un diccionario (en python {"llave":"valor"}), y en valor
	iria una breve descripcion introductoria de lo que se va a adivinar
	"""
	
	def __init__(self):
		super(Ahorcado).__init__()

	#establece como variable de clase la frase que se le envia
	def setFrase(self, frase):
		"""Establece la frase que será usada"""
		self.frase = frase

	#devuelve la frase, la cual esta almacenada como variable de clase
	def getFrase(self):
		"""Retorna la frase que fue establecida por setFrase"""
		return self.frase
	
	#a la frase o letra le quita los espacios laterales y la pone en mayuscula(s) - retorna frase o letra
	def sanitizar(self, frase):
		"""Limpia espacios laterales y pone en mayusculas la frase o letra, retorna la frase o letra"""
		limpiar = frase.strip()
		limpiar = limpiar.upper()
		return limpiar
	
	#contar la cantidad real de letras - retorna numero
	def cant_letras(self, frase):
		"""Cuenta la cantidad real de letras diferentes en la frase, retorna esa cantidad"""
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

	#reemplazo inicial de letras por guiones bajos - retorna frase en _ y espacios
	def letras_x_guiones(self, frase):
		"""Remplazo inicial de letras por guiones bajos, retorna frase en _ y espacios"""
		#reemplaza cada letra por un guion bajo
		self.frase_re = regex.sub("[A-Za-z]","_", frase)
		return self.frase_re

	#reemplazo de guion por letra ingresada - retorna True o False si encontro la letra y reemplaza por _ si es debido
	def reemplazo_letra(self, letra):
		"""Reemplaza el guion por la letra ingresada en caso de estar en la frase, retorna True si encontro y reemplazo
		algo, False si no encontro la letra en la frase"""
		#se crea una lista alterna en base a la frase y otra en base a los guiones y espacios
		lista1 = list(self.frase)
		lista2 = list(self.frase_re)
		#bandera local para verificar si esta la letra o no 
		bandera=False
		#recorre la frase (lista1) posicion a posicion
		for i in range(len(lista1)):
			#si la letra es igual a la ingresada --no recibe espacios, por ello no es necesario nada mas
			if (lista1[i] == letra):
				#que la reemplace en la posicion correspondiente
				lista2[i] = lista1[i]
				bandera=True
		#se vacia la frase_re que almacena los guiones bajos y letras
		self.frase_re = ""
		#se recorre la lista 2 con las letras o guiones reemplazadas para asignarlos nuevamente al string frase_re
		for i in lista2:
			self.frase_re = self.frase_re + i
		return bandera

	def setIntentos(self, intentos):
		"""Establece la cantidad de intentos para la frase asignada"""
		self.intentos = intentos

	def getIntentos(self):
		"""Obtiene la cantidad de intentos asignados por setIntentos"""
		return self.intentos

	def setFigura(self, figura):
		"""Establece la figura según la posición indicada"""
		self.figura = figura

	def getFigura(self,posicion):
		"""Obtiene la figura establecida por setFigura"""
		return self.figura[posicion]


#el programa inicia por acá
if __name__=="__main__":
	#crea el objeto
	ahorcado = Ahorcado()
	##se mira el tamaño del diccionario -en el archivo diccionario el objeto diccionarios
	tam_dir =  len(diccionario.diccionario)
	#se elige la frase de manera aleatoria del archivo diccionario.py
	new_frase = diccionario.diccionario[random.randint(1, tam_dir)]
	#establece la frase
	ahorcado.setFrase(new_frase)
	#verifica que la frase tenga caracteres validos (letras y espacios unicamente)
	if (regex.search("^[a-zA-Z ]+$", ahorcado.getFrase())):
		#Sanitizar: quitar espacios laterales y poner en mayusculas y establecerla nuevamente
		ahorcado.setFrase(ahorcado.sanitizar(ahorcado.getFrase()))
		#contar la cantidad real de letras 
		#si la cantidad de letras es mayor a 0 sirve, sino no
		if (ahorcado.cant_letras(ahorcado.getFrase())):
			print("Cantidad de letras:", ahorcado.cant_letras(ahorcado.getFrase()))
			#Contar la cantidad de caracteres
			print("Cantidad de caracteres:", len(ahorcado.getFrase()))
			#reemplazar las letras por guiones y los espacios dejarlos igual
			print("estado:", ahorcado.letras_x_guiones(ahorcado.getFrase()))
			
			def intentos_figura(letras_real):
				"""verifica los intentos que tiene el usuario, los intentos los determina
				la cantidad real de letras: 1-4=7intentos, 5-8=10 intentos, >9=15 intentos.
				Tambien establece las figuras correspondientes a la cantidad de intentos,
				retorna los intentos"""
				if (letras_real <= 4):
					#establece los intentos en 7
					ahorcado.setIntentos(7)
					#establece la figura correspondiente 
					ahorcado.setFigura(fig.figura7i)
				elif(letras_real >= 5 and letras_real <= 8 ):
					ahorcado.setIntentos(10)
					ahorcado.setFigura(fig.figura10i)
				else:
					ahorcado.setIntentos(15)
					ahorcado.setFigura(fig.figura15i)			
				return ahorcado.getIntentos() 
			
			#se verifica y establecen los intentos (vidas) y las figuras a usar
			intentos_figura(ahorcado.cant_letras(ahorcado.getFrase()))
			print("Intentos:",ahorcado.getIntentos())
			#esta figura es la inicial en todo -- fuera de servicio :D
			#print(fig.figuraini[0])
			#se toma la última figura en la lista. (la lista esta invertida, por ello la última figura es en realidad la primera)
			print(ahorcado.getFigura( ahorcado.getIntentos() ))
			#se agrega la figura correspondiente

			#mientras tenga intentos que juegue
			while(ahorcado.getIntentos() > 0):
				#ingresar una letra 
				letra = input("Ingrese una letra (o frase completa): ")
				#quita los espacion y la pone en mayuscula
				letra = ahorcado.sanitizar(letra)
				#agrega los espacion necesarios para pantalla limpia
				print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				#verifica que sea una sola letra 
				if ( regex.search("^[a-zA-Z]$",letra) ):
					#ahora se busca la letra que ingresó si esta o no en la frase y la reemplaza
					if (ahorcado.reemplazo_letra(letra)):
						#se verifica que la frase este o no completa, si esta, termina el juego,
						if (ahorcado.frase_re == ahorcado.getFrase()):
							print("Haz ganado, frase completa.", ahorcado.getFrase())
							#termina el ciclo y por ende el juego
							break
						#sino, sigue el juego
						else:
							#como encontro la letra, pone nuevamente los intentos, la figura y la frase_re en pantalla
							print("LETRA COINCIDENTE:", letra)
							print("intentos restantes:", ahorcado.getIntentos() )
							print( ahorcado.getFigura( ahorcado.getIntentos() ) )
							print(ahorcado.frase_re)
					else:	
						#no reemplazo ninguna letra, por ello pierde un punto, vida o intento					
						print("PIERDE UN PUNTO, LETRA NO COINCIDE")
						ahorcado.setIntentos(ahorcado.getIntentos()-1)
						print("intentos restantes:", ahorcado.getIntentos())
						print(ahorcado.getFigura( ahorcado.getIntentos() ))
						print(ahorcado.frase_re)
				#sino es una letra sino la frase completa
				elif(letra == ahorcado.getFrase()):
					print("Haz ganado, frase completa", ahorcado.getFrase())
					#muestra el muñeco ganador y dice si quiere jugar otra vez - no hay lol
					break
					#GANA Y SE ACABA LA RONDA, NUEVA FRASE
				#sino es un acierto, pierde un punto y muestra ahorcado un nivel mas
				else:
					print("Debe ingresar una letra o la frase completa respetando espacios:", letra)
					#PIERDE UN PUNTO
					ahorcado.setIntentos(ahorcado.getIntentos()-1)
					print("intentos restantes:",ahorcado.getIntentos())
					#muestra muñeco en la posicion que va
					print(ahorcado.getFigura(ahorcado.getIntentos()))
					print(ahorcado.frase_re)
			#termina el while por ende el juego
			print(ahorcado.getFrase())
		#else de la cantidad de letras que sea mayor a 0 o mas de 1
		else:
			print(ahorcado.getFrase(), "no es una frase valida.")
	#else de la frase con caracteres validos, validacion hecha por futuras aplicaiones y evitar fatiga de una vez
	else:
		print(ahorcado.getFrase(), "no es una frase valida.")
	
#TO DO

#deberia guardar en una lista las letras que el usuario ya ha ingresado
#para asi darle la opcion de que ingrese otra que no sea esa misma
#a modo recordatorio

#Agregarle un indicio acerca de la palabra que va a adivinar. 

#agregar opcion para seguir jugando o finalizar juego... 