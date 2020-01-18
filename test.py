import libreria

# 1.
assert(libreria.formatear_soles(1250.5) == "S/.1,250.50")
print("formatear_soles OK")

# 2.
assert(libreria.capitalizar_cadena("titulo") == "Titulo")
print("capitalizar_cadena OK")

# 3.
assert(libreria.contar_caracteres("bienvenidos") == 11)
print("contar_caracteres OK")

# 4.
assert(libreria.rellenar_ceros("10",5) == "00010")
print("rellenar_ceros OK")

# 5.
assert(libreria.invertir_cadena("espejo") == "ojepse")
print("invertir_cadena OK")

# 6.
assert(libreria.buscar_cadena("facebook","face") == True)
print("buscar_cadena OK")

# 7.
assert(libreria.contar_busqueda("hola mundo","mundo") == 1)
print("contar_busqueda OK")

# 8.
assert(libreria.validar_alfa("abcde") == True)
print("validar_alfa OK")

# 9.
assert(libreria.validar_minus("cadena") == True)
print("validar_minus OK")

# 10.
assert(libreria.validar_mayus("CADENA") == True)
print("validar_mayus OK")

# 11.
assert(libreria.eliminar_espacios("    Hola   ") == "Hola")
print("eliminar_espacios OK")

# 12.
assert(libreria.reemplazar_cadena("Hola mundo", "mundo", "a todos") == "Hola a todos")
print("reeplazar_cadena OK")

#13
assert(libreria.validar_correo("admin@gmail.com") == True)
print("validar_correo OK")


# 14.
assert(libreria.mostrar_dia(2) == "Martes")
print("mostrar_dia OK")

# 15.
assert(libreria.validar_inicio("carpeta","car") == True)
print("validar_inicio OK")

# 16.
assert(libreria.validar_fin("muebleria","eria") == True)
print("validar_fin OK")

# 17.
assert(libreria.crear_titulo("titulo") == "*******titulo*******")
print("crear_titulo OK")


# 18.
assert(libreria.formatear_entero(10.540,2) == "10.54")
assert(libreria.formatear_entero(30.35,1) == "30.4")
print("convertir_minuscula OK")

# 19.
assert(libreria.convertir_minuscula("CADENA") == "cadena")
assert(libreria.convertir_minuscula("TELEVISION") == "television")
print("convertir_minuscula OK")

# 20.
assert(libreria.convertir_mayuscula("viernes") == "VIERNES" )
assert(libreria.convertir_mayuscula("abril") == "ABRIL")
print("convertir_mayuscula OK")

# 21.
assert(libreria.nota_alumno(13) == "APROBADO")
assert(libreria.nota_alumno(10) == "DESAPROBADO")
print("nota_alumno OK")

# 22.
assert(libreria.pago_mensual(1300) == True)
assert(libreria.pago_mensual(100) == False)
print("pago_mensual OK")

# 23.
assert(libreria.verificar_edad(20) == True)
assert(libreria.verificar_edad(35) == True)
print("verificar_edad OK")

# 24.
assert(libreria.truncar_cadena("Hola a todos",4) == "Hola...")
assert(libreria.truncar_cadena("Bienvenido",3) == "Bie...")
print("truncar_cadena OK")

# 25.
assert(libreria.convertir_plural("pajaro") == "pajaros")
assert(libreria.convertir_plural("avion") == "aviones")
print("convertir_plural OK")

# 26.
assert(libreria.crear_slug("python y sus funciones") == "python-y-sus-funciones")
assert(libreria.crear_slug("El lenguaje Python") == "el-lenguaje-python")
print("crear_slug OK")

# 27.
assert(libreria.ciclo_vida(23) == "Adulto")
assert(libreria.ciclo_vida(75) == "Anciano")
print("ciclo_vida OK")

# 28.
assert(libreria.crear_url("peru21.pe") == "http://www.peru21.pe")
assert(libreria.crear_url("unprg.edu.pe") == "http://www.unprg.edu.pe")
print("crear_url OK")

# 29.
assert(libreria.crear_correo("genesis20") == "genesis20@gmail.com")
assert(libreria.crear_correo("unprg") == "unprg@gmail.com")
print("crear_correo OK")

# 30.
assert(libreria.peso_ideal(64, 1.74) == "Peso ideal")
assert(libreria.peso_ideal(80, 1.50) == "Peso no ideal")
print("peso_ideal OK")