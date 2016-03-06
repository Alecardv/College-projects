from menu import *
import sys

hechos ={}
sujetos ={}
funciones ={}
reglas ={}
subReglas = []
# POSIBLES ACCIONES A REALIZAR
actions = ["Insertar","Eliminar","Consultar","Salir"]
# POSIBLES OPCIONES SOBRE LA CUAL SE EJECUTARA UNA ACCION X
options = ["Funciones","Sujetos","Hechos","Reglas","Atras"]
Operadores = {"No":"No", "Y":"Y", "O":"O", "Implica":"Implica", "Si y solo si":"Si y solo si", "Para todo":"Para todo", "Existe":"Existe", "Tal que": "Tal que"}
#Acciones a realizar
actionsRules = ["Funciones", "Sujetos", "Hechos", "Operadores", "Salir"]
#Opciones sobre la accion
optionsRules = ["Consultar", "Establecer", "Volver"]

## METODOS GENERALES

def exist(key,dictionary):
	return key in dictionary
	

# METODOS PARA INSERTAR ELEMENTOS Implementado por Carolina
def insertarFuncion():
	key1 = "F%d"%(len(funciones)+1)
	funciones[key1] = raw_input("Ingrese la funcion:")
	

def insertarSujeto():
	key2 = "S%d"%(len(sujetos)+1)
	sujetos[key2] = raw_input("Ingrese el sujeto: ")
	
	
def insertarHecho():
	consultarFuncion("x")

	suj1 = None
	suj2 = None
	fun = None
	while True:
		fun = raw_input("Ingrese la funcion: ")
		if(exist(fun, funciones)):
			break
		else: 
			print("Ingrese una funcion valida\n")
	consultarSujeto("x")
	while True:
		suj1 = raw_input("Ingrese el primer sujeto: ")
		if(exist(suj1, sujetos)):
			break
		else: 
			print("Ingrese un sujeto valido\n")
	consultarSujeto("x")
	while True:
		suj2 = raw_input("Ingrese el segundo sujeto: ")
		if(exist(suj2, sujetos)):
			break
		else: 
			print("Ingrese una funcion valida\n")

	key3 = "H%d"%(len(hechos)+1)
	hechos[key3] =  (fun,suj1,suj2)

def insertarRegla():
	subReglas = []
	printmenuRules()

def construirRegla():
	key = "R%d"%(len(reglas)+1)
	reglas[key] = subReglas

# IMPLEMENTADO POR: Alejandro Cardona

#Elimina un elemento
def eliminar(diccionario, op):
	if(exist(op,diccionario)):
		del diccionario[op]

#METODOS PARA ELIMINAR ELEMENTOS
def eliminarFuncion():
	consultarFuncion("Funciones")
	op = raw_input ("Que funcion desea eliminar: ")
	eliminar(funciones, op)
	

def eliminarSujeto():
	consultarSujeto("Sujeto")
	op = raw_input ("Que sujeto desea eliminar: ")
	eliminar(sujetos, op)
	

def eliminarHecho():
	consultarHecho("Hechos")
	op = raw_input ("Que hecho desea eliminar: ")
	eliminar(hechos, op)
	

def eliminarRegla():
	consultarRegla("Reglas")
	op = raw_input ("Que regla desea eliminar: ")
	eliminar(reglas, op)
	
# METODOS PARA CONSULTAR ELEMENTOS Implementado por Beto

def consultarFuncion(key=None):
	if(key is None):
			key = raw_input("Que funcion desea consultar: ")
	flag = exist(key,funciones)
	if(flag):
		print ("%s: %s")%(key,funciones[key])
	else:
		for s in funciones:
			print ("%s = %s: %s")%(key,s,funciones[s])
	

def consultarSujeto(key=None):
	if(key is None):
		key = raw_input("Que sujeto desea consultar: ")
	flag = exist(key,sujetos)
	if(flag):
		print ("%s: %s")%(key,sujetos[key])
	else:
		for s in sujetos:
			print ("%s = %s: %s")%(key,s,sujetos[s])

	
def printHecho(h,f,s1,s2):
	
	print ("%s = %s %s %s\n")%(h,sujetos[s1],funciones[f],sujetos[s2])

def consultarHecho(key=None,s1=None,s2=None):
	if(key is None):
		key = raw_input("Que hecho desea Consultar: ")
		s1 = raw_input("Ingrese el primer sujeto: ")
		s2 = raw_input("Ingrese el segundo sujeto: ")
	Hechos = []
	if(exist(key,funciones)):
		if(exist(s1,sujetos) and exist(s2,sujetos)):
			for hecho in hechos:
				if(hechos[hecho][0] == key):
					Hechos.append((hecho,hechos[hecho][1],hechos[hecho][2]))
		elif(exist(s1,sujetos) and not( exist(s2,sujetos))):
			for hecho in hechos:
				if(hechos[hecho][0] == key and hechos[hecho][1] == s1):
					Hechos.append((hecho,hechos[hecho][1],hechos[hecho][2]))
		elif(exist(s2,sujetos) and not( exist(s1,sujetos))):
			for hecho in hechos:
				if(hechos[hecho][0] == key and hechos[hecho][2] == s2):
					Hechos.append((hecho,hechos[hecho][1],hechos[hecho][2]))
		elif(not(exist(s2,sujetos)) and not( exist(s1,sujetos))):
			for hecho in hechos:
				if(hechos[hecho][0] == key):
					Hechos.append((hecho,hechos[hecho][1],hechos[hecho][2]))

		for i in Hechos:
			printHecho(i[0],key,i[1],i[2])
		

	else:
		for hecho in hechos:
			printHecho(hecho,hechos[hecho][0],hechos[hecho][1],hechos[hecho][2])
		
	return (len(Hechos) > 0)
	


def consultarRegla():
	print reglas
	


# METODOS FUNCIONAMIENTO DEL MENU
def printMenu():
	myMenu.printMenu()

def exit():
	sys.exit("Bye!")

# DICCIONARIO PARA LA ASOCIACION DE METODOS Y EL MENU
functions = {"Insertar":{"Funciones":insertarFuncion, "Sujetos":insertarSujeto, "Hechos":insertarHecho, "Reglas":insertarRegla, "Atras":printMenu},
"Eliminar":{"Funciones":eliminarFuncion, "Sujetos":eliminarSujeto, "Hechos":eliminarHecho, "Reglas":eliminarRegla, "Atras":printMenu},
"Consultar":{"Funciones":consultarFuncion, "Sujetos":consultarSujeto, "Hechos":consultarHecho, "Reglas":consultarRegla, "Atras":printMenu},
"Salir":exit}







#OBJETO MENU
myMenu =  Menu(actions,options,functions)

#------------------------


def consultarOperadores():
	n = 0
	for k in Operadores:
		print "%d: %s"%(n+1,k)
		n += 1

def printmenuRules():
	menuRules.printMenu()

def establecerSubRegla():
	key = raw_input ("Seleccione una opcion: ")
	subReglas.append(key)


#Diccionario asociacion de metodos en el menu
functionsRules = {"Funciones":{"Consultar":consultarFuncion, "Establecer":establecerSubRegla, "Volver":printmenuRules},
"Sujetos":{"Consultar":consultarSujeto, "Establecer":establecerSubRegla, "Volver":printmenuRules},
"Hechos":{"Consultar":consultarHecho, "Establecer":establecerSubRegla, "Volver":printmenuRules},
"Operadores":{"Consultar":consultarOperadores, "Establecer":establecerSubRegla, "Volver":printmenuRules},
"Salir":construirRegla}


#OBJETO MENU DE REGLAS
menuRules = Menu(actionsRules, optionsRules, functionsRules)


printMenu()