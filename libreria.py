# 1.
#Funcion: Da un formato de soles a un monto
#Parametros: monto => monto a formatear
#Retorna: str
def formatear_soles(monto):
	if(isinstance(monto, int) or isinstance(monto, float)):
		return "S/.{:0,.2f}".format(monto)
	else:
		return False
#Fin formatear_soles


# 2.
#Funcion: Pone la primera letra en mayuscula
#Parametros: cadena => cadena a capitalizar
#Retorna: str
def capitalizar_cadena(cadena):
	if(isinstance(cadena, str)):
		return cadena.capitalize()
	else:
		return false
#Fin capitalizar_cadena


# 3.
#Funcion: Cuenta los caracteres de una cadena
#Parametros: cadena => cadena a contar
#Retorna: int
def contar_caracteres(cadena):
	if(isinstance(cadena, str)):
		return len(cadena)
	else:
		return False
#Fin contar_cadena


# 4
#Funcion: Rellena con ceros a la izquierda
#Parametros: numero => numero a rellenar
#Retorna: str
def rellenar_ceros(numero,relleno):
	if(isinstance(numero, str)):
		return numero.zfill(relleno)
	else:
		return False
#Fin rellenar_ceros

# 5.
#Funcion: Invierte una cadena
#Parametros: cadena => cadena a invertir
#Retorna: str
def invertir_cadena(cadena):
	if(isinstance(cadena, str)):
		return "".join(reversed(cadena))
	else:
		return False
#Fin invertir_cadena

# 6.
#Funcion: Busca un caracter o subcadena en una cadena
#Parametros: cadena => cadena a invertir
#			 busqueda => caracter o subcadena a buscar
#Retorna: bool
def buscar_cadena(cadena, busqueda):
	if(isinstance(cadena, str)):
		if(cadena.find(busqueda) != -1):
			return True
		else:
			return False
	else:
		return False
#Fin buscar_cadena

# 7.
# #Funcion: Cuenta la cantidad de veces que se repite una subcadena
#Parametros: cadena => cadena a invertir
#			 busqueda => caracter o subcadena a buscar
#Retorna: int
def contar_busqueda(cadena, busqueda):
	if(isinstance(cadena, str)):
		return cadena.count(busqueda)
	else:
		return False
#Fin contar_busqueda

# 8.
#Funcion: Valida que los caracteres de la cadena sean alfabeticos
#Parametros: cadena => cadena a validar
#Retorna: bool
def validar_alfa(cadena):
	if(isinstance(cadena, str)):
		if(cadena.isalpha()):
			return True
		else:
			return False
	else:
		return False
#Fin validar_alfa


# 9.
#Funcion: Valida que toda la cadena sea minuscula
#Parametros: cadena => cadena a validar
#Retorna: bool
def validar_minus(cadena):
	if(isinstance(cadena, str)):
		if(cadena.islower()):
			return True
		else:
			return False
	else:
		return False
#Fin validar_minus


# 10.
#Funcion: Valida que toda la cadena sea mayuscula
#Parametros: cadena => cadena a validar
#Retorna: bool
def validar_mayus(cadena):
	if(isinstance(cadena, str)):
		if(cadena.isupper()):
			return True
		else:
			return False
	else:
		return False
#Fin validar_mayus

#11.
# #Funcion: Elimina los espacios en blanco al inicio y final de la cadena
#Parametros: cadena => cadena a corregir
#Retorna: str
def eliminar_espacios(cadena):
	if(isinstance(cadena, str)):
		return cadena.strip()
	else:
		return False
#Fin eliminar_espacios

# 12.
# #Funcion: reemplaza una cadena por otra
#Parametros: cadena => cadena a corregir
#			 busqueda => cadena a buscar
#			 reemplazo => cadena que reemplaza
#Retorna: str
def reemplazar_cadena(cadena, busqueda, reemplazo):
	if(isinstance(cadena, str)):
		return cadena.replace(busqueda, reemplazo)
	else:
		return False
#Fin reemplazar_cadena

# 13.
# #Funcion: Valida que la cadena ingresada sea un email
#Parametros: correo => email a validar
#Retorna: bool
def validar_correo(correo):
	if(isinstance(correo, str)):
		if(correo.find("@") != -1):
			return True
		else:
			return False
	else:
		return False
#Fin validar_mayus


# 14.
# #Funcion: Muestro el dia segun el numero ingresado
#Parametros: dia
#Retorna: str

def mostrar_dia(dia):
	if(isinstance(dia,int)):
		if(dia>=1 and dia<=7):
			dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
			return dias[dia - 1]
		else:
			return False
	else:
		return False
#fin_mostrar_dia


# 15.
# #Funcion: Valida que una cadena inicie con un valor ingresado
#Parametros: cadena
#            busqueda
#Retorna: bool

def validar_inicio(cadena,busqueda):
	if (isinstance(cadena, str) and isinstance(busqueda, str)):
		return cadena.startswith(busqueda)
	else:
		return False
#fin_validar_inicio


# 16.
# #Funcion: Valida que una cadena inicie con un valor ingresado
#Parametros: cadena
#            busqueda
#Retorna: bool

def validar_fin(cadena,busqueda):
	if (isinstance(cadena,str) and isinstance(busqueda,str)):
		return cadena.endswith(busqueda)
	else:
		return False
#fin_validar_fin


# 17.
#Funcion: crea un titulo con un formate para reporte
#Parametros: cadena
#Retorna: str

def crear_titulo(cadena):
	if(isinstance(cadena,str)):
		return "{0:*^20}".format(cadena)
	else:
		return False
#fin_crear_titulo


# 18.
# #Funcion: da formato de decimales segun el numero y los decimales
#Parametros: entero
#            decimales
#Retorna: float o bool

def formatear_entero(entero,decimales):
    if(isinstance(entero,float)):
    	return "{0:.{1}f}".format(entero,decimales)
    else:
    	return False


#19.
# Funcion: convertir una cadena a minuscula
# Parametros: cadena
# Retorna: str o bool

def convertir_minuscula(cadena):
	if(isinstance(cadena,str)):
		return cadena.lower()
	else:
		return False
#fin_convertir_minuscula


#20.
# Funcion: convertir una cadena a mayuscula
# Parametros: cadena
# Retorna: str o bool

def convertir_mayuscula(cadena):
	if(isinstance(cadena,str)):
		return cadena.upper()
	else:
		return False
#fin_convertir_mayuscula

# 21.
# Funcion: validar nota del alumno
# Parametros: nota
# Retorna: str

def nota_alumno(nota):
	if(nota >= 11 and nota <= 20):
		return "APROBADO"
	else:
		return "DESAPROBADO"
#fin_nota_alumno


# 22.
# Funcion: validar un pago mensual
# Parametros: pago
# Retorna: bool
def pago_mensual(pago):
	if(pago >= 1200 and pago <= 2000):
		return True
	else:
		return False
#fin_pago_mensual


#23.
# Funcion: comprobar si edad es un digito
# Parametros: edad
# Retorna: bool

def verificar_edad(edad):
	if(isinstance(edad,int)):
		return True
	else:
		return False
#fin verificar_edad

#24.
# Funcion: truncar una cadena si excede el numero de caracteres ingresado 
# Parametros: cadena, limite
# Retorna: cadena
def truncar_cadena(cadena, limite):
	if(len(cadena) > limite):
		return cadena[:limite] + "..." 
	else:
		return cadena

#25.
# Funcion: convierte una cadena singular en plural
# Parametros: cadena
# Retorna: cadena
def convertir_plural(cadena):
	if("aeiou".find(cadena[len(cadena)-1:]) != -1):
		return cadena + "s"
	else:
		return cadena + "es"

#26.
# Funcion: convierte una cadena en slug
# Parametros: cadena
# Retorna: cadena
def crear_slug(cadena):
	if(isinstance(cadena, str)):
		return cadena.lower().replace(" ", "-")
	else:
		return False

#27.
# Funcion: Muestra el ciclo de vida de una persona segun la edad ingresada 
# Parametros: edad
# Retorna: cadena
def ciclo_vida(edad):
	if(isinstance(edad, int)):
		if(edad >= 0 and edad <= 4):
			return "Bebe"
		elif(edad >= 5 and edad <= 12):
			return "Niño"
		elif(edad >= 13 and edad <= 20):
			return "Adolescente"
		elif(edad >= 21 and edad <= 59):
			return "Adulto"
		else:
			return "Anciano"
	else:
		return False

#28.
# Funcion: convierte una cadena en url valida
# Parametros: cadena
# Retorna: cadena
def crear_url(cadena):
	if(isinstance(cadena, str)):
		return "http://www.{0}".format(cadena)
	else:
		return False

#29.
# Funcion: crear un correo de gmail
# Parametros: cadena
# Retorna: cadena
def crear_correo(cadena):
	if(isinstance(cadena, str)):
		return "{0}@gmail.com".format(cadena)
	else:
		return False

#30.
# Funcion: funcion para saber si tenemos el peso ideal
# Parametros: peso, altura
# Retorna: cadena
def peso_ideal(peso,altura):
	imc = peso/(altura**2)
	if(imc >= 18.5 and imc <= 24.9):
		return "Peso ideal"
	else:
		return "Peso no ideal"