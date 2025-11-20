# -----------------------------------------------
# Integrante 3: Concatenación y extracción de subcadenas
# -----------------------------------------------

# ----- Concatenación de cadenas -----

# Usando el operador +
cadena1 = "Hola"
cadena2 = "Mundo"
concatenacion_mas = cadena1 + " " + cadena2  # Se agrega un espacio entre ambas
print("Concatenación con + :", concatenacion_mas)

# Usando join()
palabras = ["Hola", "desde", "Python"]
concatenacion_join = " ".join(palabras)  # Une la lista usando un espacio
print("Concatenación con join():", concatenacion_join)


# ----- Extracción de subcadenas -----

texto = "Programación"

# Indexado: obtener un solo carácter
primer_caracter = texto[0]      # Primer carácter
ultimo_caracter = texto[-1]     # Último carácter
print("Primer carácter:", primer_caracter)
print("Último carácter:", ultimo_caracter)

# Slicing: obtener varias posiciones
subcadena_1 = texto[0:6]   # Desde índice 0 hasta 5 (no incluye el 6)
subcadena_2 = texto[6:]    # Desde el índice 6 hasta el final
subcadena_3 = texto[:]     # Copia completa
print("Subcadena [0:6]:", subcadena_1)
print("Subcadena [6:]:", subcadena_2)
print("Subcadena completa [:]:", subcadena_3)

print("\n----------------------------")
print("Código - Conversión y conteo") 
print("----------------------------")

# ----- Conversión de mayúsculas y minúsculas -----

mensaje = "Python es un Lenguaje Muy Versátil"

# Convertir todo a mayúsculas usando upper()
mensaje_mayusculas = mensaje.upper()
print("\n-------- Conversión --------")
print("Original:", mensaje)
print("Mayúsculas:", mensaje_mayusculas)

# Convertir todo a minúsculas usando lower()
mensaje_minusculas = mensaje.lower()
print("Minúsculas:", mensaje_minusculas)

# ----- Conteo de caracteres y palabras -----

frase_estudio = "Fundamentos de la programación en la universidad"

# 1. Contar caracteres (len)
# La función len() cuenta todo, incluyendo espacios en blanco.
total_caracteres = len(frase_estudio)

print("\n---------- Conteo ----------")
print(f"Frase analizada: '{frase_estudio}'")
print("Total de caracteres (con espacios):", total_caracteres)

# 2. Contar palabras
# Primero usamos split() para 'romper' la cadena en una lista de palabras
lista_de_palabras = frase_estudio.split()
# Luego contamos cuántos elementos tiene esa lista
cantidad_palabras = len(lista_de_palabras)

print("Lista generada:", lista_de_palabras)
print("Cantidad de palabras:", cantidad_palabras)
print("\n----------------------------\n")