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
1). ENCABEZADO
ES EL COMENTARIO SIRVE PARA QUIEN REVISE SEPA DE QUE TRATA EL PROGRAMA
 

2). CONCATENACION
Cadena1 = “Hola” guarda la cadena “Hola” en la variable cadena1.
Cadena2 = “Mundo” guarda “Mundo” en cadena2.
Cadena1 +” “+ cadena2 une las dos cadenas con un espacio en medio. El operador + concatena strings directamente.
El resultado “Hola Mundo” se guarda en concatenación_mas.
Print (…) muestra en pantalla: concatenación con +: Hola Mundo
 

3). CONCATENACION USANDO JOIN ()
 
Palabras es una lista de strings: \left["\right.Hola”, “desde”,” Python\left."\right].
“ ”. Join (palabras) toma cada elemento de la lista y los une en una sola cadena usando “” (un espacio) como separador.
Si hubiera usado “,”. join (palabras), el separador sería una coma.
El resultado “Hola desde Python” se guarda en cancatenacion_join.
Print (…) muestra: concatenación con join(): Hola desde Python

4). DEFINICIÓN DEL TEXTO PARA EXTRACCIÓN 
 
Guarda la cadena “programación “en la variable texto. A partir de aquí extraemos caracteres y subcadenas.

5). INDEXADO OBTENER UN SOLO CARÁCTER
 
Texto \left[0\right] devuelve el carácter en la posición 0 (el primero). En “programación “es “p”.
Texto \left[-1\right] usa índice negativo: -1 es el último carácter de la cadena. En este caso es “n”.
Se imprimen: 
Primer carácter: p 
Ultimo carácter: n 
Los índices empiezan en 0. Entonces texto\left[1\right] seria la segunda letra 

6). SLICING REBANADO DE SUBCADENA 
Texto \left[0:6\right]toma desde el índice 0 hasta el índice 6, pero no incluye el carácter en el índice 6. Esto devuelve los índices 0,1,2,3,4,5. Para “programación “ 
Texto \left[0:6\right]”progra”
Se imprime: subcadena \left[0:6\right] :progra
Texto \left[6\right] toma desde el índice 6 hasta el final de la cadena (incluye el carácter en 6) 
Texto \left[6:\right] desde el carácter en posición 6 hasta el final “macion”
Se imprime subcadena \left[6:\right]:macion
Texto \left[:\right] copia la cadena completa (desde inicio hasta el final) 
Texto \left[:\right]”programación “
Se imprime: subcadena completa \left[:\right]:programación 
Regla general del slicing a: b: 
Empieza en a (incluye a).
Termina en b (no incluye b).
Si a se omite, empieza en 0. Si b se omite, llega al final. 

