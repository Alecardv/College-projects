# -----------------------------------------------------------------------------
# | Desarrollador: Jose Alejandro Cardona                                     |
# | Dado un valor y una aridad este codigo calcula combinaciones de numeros   |
# | con una longitud correspondiente a la aridad que sumen dicho valor sin    |
# | repetir numeros y siendo estos comprendidos entre el 1 y el 9.            |
# | Ejemplo: Valor= 5, Aridad = 2 ---> Combinaciones: [1,4][2,3]              |
# -----------------------------------------------------------------------------

# Selecciona el numero de elementos que indique la aridad en el dominio
# ignorando el valor "#" cuando este no esta en la primera posicion y 
# devolviendolo cuando se encuentra en ella como condicion de parada:
def seleccionar(aridad, dominio):
	i = 0
	temp = []

	if dominio[0] == "#":
		return "#"
	else:
		while i <= aridad:
			
			if dominio[i] == "#":
				i += 1
			else:
				temp.append(dominio[i])
				i += 1

	if len(temp) > aridad: 
		temp.remove(temp[len(temp)-1])
		return temp
	else:
		return temp

# Establece si el candidato cumple la condicion de que la suma de sus 
# elementos debe ser igual al valor, de cumplirse devuelve el vector con los
# encontrados anteriores y los nuevos, sino devuelve la condicion de parada
def establecer(candidato, valor, encontrados):
	
	if "#" in candidato: return "#"

	if sumar(candidato) == valor:
		agregar(candidato, encontrados)
		return encontrados
	else:
		return "#"

def rebuildDomain(dominio, aridad, switcher):
	
	temp = []

	if switcher == 0:
		if dominio[aridad-1] == "#":
			dominio.remove("#")
			temp = dominio[switcher]
			dominio.remove(dominio[switcher])
			dominio.append(temp)
			dominio.append("#")

		else:
			temp = dominio[aridad-1]
			dominio.remove(dominio[aridad-1])
			dominio.append(temp)

	elif switcher == 1:
		if dominio[aridad-1] == "#":
			dominio.remove("#")
			temp = dominio[switcher]
			dominio.remove(dominio[switcher])
			dominio.append(temp)
			dominio.append("#")	
		else:
			temp = dominio[aridad-1]
			dominio.remove(dominio[aridad-1])
			dominio.append(temp)

	elif switcher == 2:
		if dominio[aridad-1] == "#":
			dominio.remove("#")
			temp = dominio[switcher]
			dominio.remove(dominio[switcher])
			dominio.append(temp)
			dominio.append("#")
		else:
			temp = dominio[aridad-1]
			dominio.remove(dominio[aridad-1])
			dominio.append(temp)

	elif switcher == 3:
		temp = dominio[3]
		dominio.remove(dominio[3])
		dominio.append(temp)

	elif switcher == 4:
		temp = dominio[4]
		dominio.remove(dominio[4])
		dominio.append(temp)

	elif switcher == 5:
		temp = dominio[5]
		dominio.remove(dominio[5])
		dominio.append(temp)

	elif switcher == 6:
		temp = dominio[6]
		dominio.remove(dominio[6])
		dominio.append(temp)

	elif switcher == 7:
		temp = dominio[7]
		dominio.remove(dominio[7])
		dominio.append(temp)

	elif switcher == 8:
		temp = dominio[8]
		dominio.remove(dominio[8])
		dominio.append(temp)
	
	return dominio

def buscar(arity, value, domain):
	found = []
	iterator = 0
	switcher = arity

	while switcher != 0:
		
		switcher -= 1
		iterator = 0

		while (iterator < (9-arity)):
			print domain
			candidate = seleccionar(arity,domain)
			foundTemp = establecer(candidate, value, found)
			
			if foundTemp != "#":
				found = foundTemp
				iterator += 1
				domain = rebuildDomain(domain, arity, switcher)
			else:
				iterator += 1
				domain = rebuildDomain(domain, arity, switcher)

	return	found

# Agrega elementos al vector de destino desde el vector de origen
# garantizando no ingresar elementos repetidos
def agregar(vect,destino):
	i = 0

	while (i < len(vect)):
		if (not (vect[i] in destino)):
			destino.append(vect[i])
			i += 1
		else:
			i += 1
	return destino

# Suma todos los elementos dentro del vector:
def sumar(vect):
	suma = 0
	i = 0
	for i in vect: suma += i
	return suma

dominio = [1,2,3,4,5,6,7,8,9,"#"]

#print rebuildDomain(dominio, 0)
print buscar(3,10,dominio) #6 8 9
