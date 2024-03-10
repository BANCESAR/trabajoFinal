# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 17:58:55 2024

@author: juliocesar
"""

#%%
#  SEMANAS 01 _ 02 
#  Comparación de los lenguajes de programación JAVA, PYTHON y C 
#%% Operaciones Básicas:
# 1. Realiza la suma, resta, multiplicación y división de 

#  PEDIMOS AL USUARIO PARA QUE INGRESE DOS NUMEROS
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# REALIZAMOS LAS OPERACIONES 
suma = num1 + num2   # SUMA
resta = num1 - num2   #RESTA
multiplicacion = num1 * num2  #MULTIPLICACION

if num2 != 0: # ASEGURAMOS QUE EL SEGUNDO NUM SEA DIFERENTE DE SERO
    division = num1 / num2 # DIVIDIMOS AMBOS NUMEROS
else:
    division = "No es posible dividir por cero." # SI EL SEGUNO VALOR ES CERO NOS DEVUELVE ESTE TEXTO

# IMPRIMIMOS LOS RESULTADOS
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


#%%  Verificación de Número Par o Impar:
# 2.Solicita un número al usuario y determina si es par o impar.

# PEDIMOS AL USUARION QUE INGRESE UN NUMERO
numero = int(input("Ingresa un número: "))

# DETERMINAMOS SI ES PAR O IMPAR
if numero % 2 == 0:
    print(f"{numero} es un número par.") #IMPRIME QUE ES UN PAR
else:
    print(f"{numero} es un número impar.") #IMPRIME QUE ES UN IMPAR
    
#%% Área de un Triángulo: 
# 3. Pide la base y la altura de un triángulo al usuario y calcula su área. 

# PEDIMOS AL USUARION QUE NOS DE VALIRES PARA LA ALTURA Y BASE  DEL TRIANGULO
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))

# IMPLEMENTAMOS LA FORMULA PARA HALLAR EL AREA DEL TRIANGULO
area_triangulo = (base * altura) / 2

# IMPRIMIMOS EL RESULTADO
print(f"El área del triángulo con base {base} y altura {altura} es: {area_triangulo:.2f}")
    

#%% Calculadora de Factorial: 
# 4. Crea una función que calcule la factorial de un número. 

def factorial(n):
    if n == 0 or n == 1: #verificamos si el valor de n es igual a 0 o 1.
        return 1
    else:
        return n * factorial(n-1)# calculamos el factorial de n multiplicándolo por el factorial de n-1

# PEDIMOS UN NUMERO AL USUARIO
numero = int(input("Ingresa un número: "))

# CALCULAMOS EL FACTORIAL Y MOSTRAMOS EL RESULTADO
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")

#%% Número Primo: 
# 5. Verifica si un número ingresado por el usuario es primo o no.

def es_primo(numero):
    if numero < 2:#Comprueba si el número es menor que 2
        return False #Si el número es menor que 2, devuelve False
    for i in range(2, int(numero**0.5) + 1):#Inicia un bucle for que itera sobre los valores de i desde 2 hasta la raíz cuadrada entera de numero más 1.
        if numero % i == 0:# En cada iteración, verifica si el número es divisible por i
            return False
    return True

# SOLICITAMMOS INGRESAR UN NUMERO
numero_usuario = int(input("Ingresa un número: "))

# VERIFICAMOS SI EL NUMERO ES PRIMO Y NOS IMPRIME EL RESULTADO
if es_primo(numero_usuario):
    print(f"{numero_usuario} es un número primo.")
else:
    print(f"{numero_usuario} no es un número primo.")


#%% Inversión de Cadena:
# 6. Toma una cadena de texto y muestra su inversión. 

def invertir_cadena(cadena):
    cadena_invertida = cadena[::-1]# Utilizamos la notación de rebanado para crear una versión invertida de la cadena
    return cadena_invertida

# PEDIMOS AL USUARIO QUE INGRESE UNA CADENA
cadena_original = input("Ingresa una cadena de texto: ")

# OBTENEMOS LA CADENA INVERTIDA Y NOS MUESTRA EL RESULTADO
resultado = invertir_cadena(cadena_original)
print(f"La cadena invertida es: {resultado}")

#%% Suma de Números Pares: 
# 7.Calcula la suma de los números pares en un
# rango especificado por el usuario.

# PEDIMOS AL USUARIO QUE INGRESE 2 NUMERO CON UN RANGO
inicio = int(input("Ingresa el inicio del rango: "))
fin = int(input("Ingresa el fin del rango: "))

# INICIAMOS LA SUMA Y GUARDAMOS EL VALOR EN UN VARIABLE
suma_pares = 0

# CALCULAMOS LA SUMA DE LOS NUMEROS PARES EN EL RANGO ESCRITO
for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        suma_pares += numero

#IMPRIMIMOS EL RESULTADO
print(f"La suma de los números pares en el rango [{inicio}, {fin}] es: {suma_pares}")


#%% Lista de Cuadrados:
# 8.  Crea una lista de los cuadrados de los primeros 10 números naturales.

# CREAMOS LA LISTA DE LOS 10 PRIMEROS NUMERO CALCULANDO SUS CUADRADOS
cuadrados = [n**2 for n in range(1, 11)]

# IMPRIMIMOS LOS RESULTADOS
print("Lista de cuadrados de los primeros 10 números naturales:")
print(cuadrados)


#%% Contador de Vocales: 
# 9. Cuenta el número de vocales en una cadena de texto. 

# SOLCITAMOS AL USUARIO QUE INGRESE UN TEXTO
cadena = input("Ingresa una cadena de texto: ")

# INICIAMOS EL CONTADOR DE LAS VOCALES
contador_vocales = 0

# DEFINIMOS LAS VOCALES MAYUSCULAS O MINUSCULAS
vocales = "aeiouAEIOU"

# CONTAMOS EL NUMERO DE VOCALES EN LA CADENA
for letra in cadena:
    if letra in vocales:
        contador_vocales += 1

# IMPRIMIMOS EL RESULTADO
print(f"El número de vocales en la cadena es: {contador_vocales}")



#%% Números de la Serie Fibonacci:
# 10.Genera los primeros 10 números de la serie Fibonac

#CREMOS LA FUNCION PARA GENERAR LOS PRIMEROS N NUMERO DE FIBONACCI
def fibonacci(n):
    fib_series = [0, 1]  # Inicializamos la serie con los primeros dos números
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

# OBTENEMOS LOS 10 PRIMEROS NUMEROS

primeros_10_fibonacci = fibonacci(10)

# MOSTRANMOS EL RESLTADO IMPRIMIENDONOS LA RESPUESTA

print("Primeros 10 números de la serie Fibonacci:")
print(primeros_10_fibonacci)

#%% Ordenamiento de Lista: 
#11.Ordena una lista de números ingresados por el usuario de menor a mayor.

# PEDIMOS AL USUARIO QUE INGRESE NUMEROS
entrada_usuario = input("Ingresa una lista de números: ")

# CONVERTIMOS LOS NUMEROS INGRESADOS EN UNA LISTA
numeros = [float(numero) for numero in entrada_usuario.split()]

# ORDENAMOS LOS NUMERO DE LA LINSTA DE MENOR A MAYOR
numeros_ordenados = sorted(numeros)

# IMPRIMIMOS LA RESPUESTA
print("Lista ordenada de menor a mayor:", numeros_ordenados)

#%% Palíndromo: 
# 12. Verifica si una palabra ingresada por el usuario es un palíndromo. 


def es_palindromo(palabra):
    palabra = palabra.lower()  # Convierte la cadena de entrada a minúsculas
    palabra_invertida = palabra[::-1]   # Crea una versión invertida de la cadena
    
    return palabra == palabra_invertida

# SOLICITAMOS AL USUARIO QUE INGRESE UNA PALABRA
palabra_usuario = input("Ingresa una palabra: ")

# VEREFICAMOS SI LA PALABRA ES UN PALINDROMO Y MOSTRAMOS EL RESULTADO
if es_palindromo(palabra_usuario):
    print(f"{palabra_usuario} es un palíndromo.")
else:
    print(f"{palabra_usuario} no es un palíndromo.")
    
    
#%% Generador de Tablas de Multiplicar: 
# 13. Crea un programa que genere la tabla de multiplicar 
#     de un número ingresado por el usuario.

# PEDIMOS AL USUARIO QUE INGRESE UN NUMERO
numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))

# Imprimir la tabla de multiplicar del número ingresado
print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11): #Esto inicia un bucle
    resultado = numero * i #: En cada iteración del bucle, calcula el resultado de la multiplicación del número dado
    print(f"{numero} x {i} = {resultado}")




#%% Cálculo del Área de un Círculo: 
# 14. Pide el radio de un círculo al usuario y calcula su área. 

import math

# PIDE UN RADIO AL USUARIO
radio = float(input("Ingresa el radio del círculo: "))

# CALCULAMOS EL AREA DEL CIRCULO CON LA FORMULA
area_circulo = math.pi * radio**2

# IMPRIME EL RESULTADO
print(f"El área del círculo con radio {radio} es: {area_circulo:.2f}")


#%% Suma de Dígitos: 
# 15.  Toma un número entero y calcula la suma de sus dígitos.

# PEDIMOS AL USUARION QUE INGRESE UN NUMERO ENTERO
numero = int(input("Ingresa un número entero: "))

# CALCULAMOS LA SUMA DE LOS DIGITOS
suma_digitos = sum(int(digito) for digito in str(abs(numero)))

# IMPRIME EL RESULTADO
print("La suma de los dígitos es:", suma_digitos)


#%%
# SEMANA 03 _ 04
# Recursividad – Arreglos y Matrices 
#%% Ejercicio 1:
# Escribe una función recursiva que imprima los números pares del 1 al 100. 

def imprimir_pares(n):
    if n <= 100:#Verifica si n es menor o igual a 100
        if n % 2 == 0: # verificamos si n es par utilizando el operador de módulo % 
            print(n)
        imprimir_pares(n + 2) #Esto se hace para pasar al siguiente número par

imprimir_pares(2)


#%% Ejercicio 2:
# Escribe una función recursiva que imprima la suma de los números del 1 al n. 

def suma_hasta_n(n):#DEFINIMOS LA FUNCION
    if n == 1: #Se comprueba si n es igual a 1
        return #Si n es igual a 1, se devuelve 1,
    else:
        return n + suma_hasta_n(n - 1) # Si n no es igual a 1, entonces se devuelve la suma de n y el resultado de llamar recursivamente a la función suma_hasta_n con n - 1

resultado = suma_hasta_n(20)
print(f"La suma de los números del 1 al 20 es: {resultado}")

#%% Ejercicio 3: 
#Escribe una función recursiva que imprima la pirámide de números del 1 al n. 

def imprimir_piramide(n, current_row=1, current_num=1):
    if current_row > n:
        return
    
    if current_num > current_row:
#AVANZA A LA SIGUINENTE FILA
        print()  
        imprimir_piramide(n, current_row + 1, 1)
    else:
#IMPRIME EL NUMERO Y LLAMA A LA FUNCION PARA EL SIGUINETE NUMERO DE LA MISMA FILA
        print(current_num, end=" ")
        imprimir_piramide(n, current_row, current_num + 1)

# LLAMAMOS A LA FUNCION CON UN EJEMPLO 4
imprimir_piramide(4)

#%% Ejercicio 4
# Escribe una función recursiva que imprima la pirámide de números invertidos del 1 al n.

def imprimir_piramide_invertida(n, current_row=1, current_num=1):#define una función llamada imprimir_piramide_invertida
    if current_row > n:#Comprueba si current_row es mayor que n
        return
    
    if current_num > current_row: # comprobación de si current_row es mayor que n
        # Avanza a la siguiente fila
        print()  
        imprimir_piramide_invertida(n, current_row + 1, 1)
    else:
        # Imprime el número invertido y llama a la función para el siguiente número en la misma fila
        print(n - current_num + 1, end=" ")
        imprimir_piramide_invertida(n, current_row, current_num + 1)

# Llamamos a la función con un ejemplo (por ejemplo, n=4)
imprimir_piramide_invertida(4)


#%% Ejercicio 5:
# Escribe una función recursiva que imprima la tabla de multiplicar del n.

def tabla_multiplicar(n, multiplicador=1): #define una función llamada tabla_multiplicar que toma dos argumentos: n y multiplicador
    if multiplicador > 10:#verifica si el multiplicador actual es mayor que 10
        return
    else: #Se realiza el cálculo de una sola entrada de la tabla de multiplicar, se calcula el resultado multiplicando n
        resultado = n * multiplicador
        print(f"{n} x {multiplicador} = {resultado}")
        tabla_multiplicar(n, multiplicador + 1)

#TOMAMOS COMO ARGUMENTO EL NUMERO 5
tabla_multiplicar(5)



#%%Ejercicio 6:
# Crea una matriz de números reales

#CREAMOS UNA MATRIZ 3 X 3
matriz = [
    [1, 5, 1],
    [9, 5, 6],
    [2, 8, 3]
]

# IMPRIMIMOS LA MATRIZ
for ejercicio in matriz:#En cada iteración del bucle, la variable ejercicio toma el valor de cada elemento de la lista matriz
    print(ejercicio)
#%% Ejercicio 7:
#Crea una matriz de números complejos.

matriz_compleja = [ #CREAMOS UNA VARIBLE LLAMADA MARIZ_COMPLEJA
    [complex(1, 2), complex(3, 4)],# ESTAS DOS SON UNAS SUBLISTAS QUE CONTIENEN
    [complex(5, 6), complex(7, 8)] #NUMEROS COMPLEJOS
]
#ITERAMOS SOBRE CADA ELEMENTO DE LA LISTA
for fila in matriz_compleja:
    print(fila)

#%%Ejercicio 8:
#Crea una matriz de matrices.

# creamos una matriz de matrices (3x3)
matrices = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
]

for matriz in matrices: # iteramos sobre cada elemento de la lista matrices
    for fila in matriz: # itera sobre cada elemento de la matriz actual
        print(fila)
    print() # Imprimimos la matriz de matrices
    
#%%Ejercicio 9:
#Accede al elemento central de una matriz.

#CREAMOS LA MATRIZ 3X3
matriz_impar = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# OBTENEMOS EL NUMERO DE FILAS Y COLUMNAS
num_filas = len(matriz_impar)
num_columnas = len(matriz_impar[0])

#ACCEDEMOS AL VALOR CENTRAL
elemento_central = matriz_impar[num_filas // 2][num_columnas // 2]
#IMPRIMIMOS EL VALOR CENTRAL
print("Elemento central:", elemento_central)
#%%Ejercicio 10:
#Suma dos matrices de diferentes tamaños.

def sumar_matrices(matriz_grande, matriz_pequena):# DEFINIMOS LA FUNCION CON SUSU ARGUMENTOS
#OBTENEMOS LAS DIMENSIONES DE AMBAS MATRICES
    filas_grande, columnas_grande = len(matriz_grande), len(matriz_grande[0])
    filas_pequena, columnas_pequena = len(matriz_pequena), len(matriz_pequena[0])
#VERIFICAMOS SI LA MATRIZ PEQUEÑA ES SUBMATRIZ DE LA MATRIZ GRANDE
    if filas_pequena > filas_grande or columnas_pequena > columnas_grande:
        print("No se puede sumar. La matriz pequeña no es submatriz de la matriz grande.")
        return None
    
#CREAMOS UNA NUEVA MATRIZ PARA ALMACENAR LA SUMA
    resultado = []
    for i in range(filas_grande):
        fila_resultado = []
        for j in range(columnas_grande):
            if i < filas_pequena and j < columnas_pequena:
                fila_resultado.append(matriz_grande[i][j] + matriz_pequena[i][j])
            else:
                fila_resultado.append(matriz_grande[i][j])
        resultado.append(fila_resultado)

    return resultado

#DEFINIMOS LA MATRIZ GRANDE
matriz_grande = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#DEFINIMOS LA MATRIZ PEQUEÑA
matriz_pequena = [
    [10, 20],
    [30, 40]
]
#LLAMAMOS A LA FUNCION Y LAS MATRICES
resultado_suma = sumar_matrices(matriz_grande, matriz_pequena)

if resultado_suma is not None:
    for fila in resultado_suma:
        print(fila)
#%% Ejercicio 11:
# Multiplica una matriz por un número. 

def multiplicar_matriz_por_escalar(matriz, escalar):#DEFINIMOS LA FUNCION CON SUS PARAMETROS
    resultado = []#INICIAMOS CON UNA LISTA VACIA

    for fila in matriz:#ITERAMOS SOBRE CADA FILA DE LA MATRIZ
    # multiplicamos cada elemento de la fila por el escalar
        fila_resultado = [elemento * escalar for elemento in fila]
        resultado.append(fila_resultado)#construye la nueva matriz con todas las filas multiplicadas por el escalar

    return resultado
#DEFINIMOS LA MATRIZ
matriz_original = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#DEFINIMO EL ESCALAR PAR AMULTIPLICAR L MATRIZ
escalar = 2
#LLAMAMOS A LA FUNCION, A LA MATRIZ Y AL ESCALAR Y LA GUARDAMOS EN UN RESULTADO
matriz_resultado = multiplicar_matriz_por_escalar(matriz_original, escalar)
#Itera sobre cada fila de la matriz resultado y las imprime
for fila in matriz_resultado:
    print(fila)

#%%Ejercicio 12:
#Calcula la media de los elementos de una matriz. 

def calcular_media_matriz(matriz):#DEFINIMOS LA FUNCION CON SU PARAMETRO MATRIZ
#INICIALIZAMOS 2 VARIBLES DESDE 0
    total_elementos = 0
    suma_elementos = 0
#El bucle externo itera sobre cada fila de la matriz, y el bucle interno itera sobre cada elemento de la fila actual
    for fila in matriz:
        for elemento in fila:
            suma_elementos += elemento
            total_elementos += 1
# se verifica si el total de elementos es igual a 0
    if total_elementos == 0:
        print("La matriz está vacía. No se puede calcular la media.")
        return None
    else: #Si la matriz no está vacía, se calcula la media dividiendo la suma total de elementos
        media = suma_elementos / total_elementos
        return media

#DEFINIMOS LA MATRIZ
matriz_ejemplo = [
    [4, 6, 3],
    [4, 1, 9],
    [3, 8, 2]
]
#LLAMAMOS A LAFUNCION A LA MATRIZ COMO ARGUMENTO
media_matriz = calcular_media_matriz(matriz_ejemplo)
#Si el resultado de calcular_media_matriz no esta vacia, se imprime la media de los elementos de la matriz.
if media_matriz is not None:
    print(f"La media de los elementos de la matriz es: {media_matriz}")



# %% 

"""Ejercicio 1:
Crea una matriz de números aleatorios de tamaño 100x100."""

import numpy as np  # Importamos la librería NumPy y la renombramos como np

# Creamos una matriz de números aleatorios de tamaño 100x100
matriz_aleatoria = np.random.rand(100, 100)

# Mostramos la matriz generada
print("Matriz de números aleatorios de tamaño 100x100:")  # Imprimimos un mensaje indicando la naturaleza de la matriz
print(matriz_aleatoria)  # Imprimimos la matriz de números aleatorios
# %% 

"""Ejercicio 2: Calcula la media, la mediana y la desviación estándar 
de los elementos de una matriz."""

import numpy as np  # Importamos la librería NumPy y la renombramos como np

# Creamos una matriz de números aleatorios de tamaño 100x100
matriz_aleatoria = np.random.rand(100, 100)

# Calculamos la media de los elementos de la matriz
media = np.mean(matriz_aleatoria)

# Calculamos la mediana de los elementos de la matriz
mediana = np.median(matriz_aleatoria)

# Calculamos la desviación estándar de los elementos de la matriz
desviacion_estandar = np.std(matriz_aleatoria)

# Mostramos los resultados
print("Media de los elementos de la matriz:", media)  # Mostramos la media de los elementos de la matriz
print("Mediana de los elementos de la matriz:", mediana)  # Mostramos la mediana de los elementos de la matriz
print("Desviación estándar de los elementos de la matriz:", desviacion_estandar)  # Mostramos la desviación estándar de los elementos de la matriz

# %% 

"""Ejercicio 3:
Escribe una función que encuentre el elemento máximo de una matriz."""

import numpy as np  # Importamos la librería NumPy y la renombramos como np

def encontrar_maximo(matriz):
    # Función para encontrar el elemento máximo de una matriz
    maximo = np.max(matriz)  # Utilizamos la función np.max() de NumPy para encontrar el elemento máximo
    return maximo  # Devolvemos el elemento máximo encontrado

# Creamos una matriz de ejemplo de tamaño 3x3 utilizando np.array que 
#Es una función de la librería NumPy que crea matrices multidimensionales Y 
#Permite convertir listas bidimensionales en matrices NumPy.
matriz_ejemplo = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])

# Llamamos a la función para encontrar el máximo de la matriz de ejemplo
maximo_encontrado = encontrar_maximo(matriz_ejemplo)

# Mostramos el máximo encontrado
print("El elemento máximo de la matriz es:", maximo_encontrado)

# %% 

"""Ejercicio 4:
Escribe una función que encuentre la submatriz de mayor suma de una matriz"""

import numpy as np  # Importamos la librería NumPy y la renombramos como np

def encontrar_submatriz_maxima(matriz):
    # Función para encontrar la submatriz de mayor suma dentro de una matriz dada
    max_suma = float('-inf')  # Inicializamos la máxima suma con un valor negativo infinito
    submatriz_maxima = None  # Inicializamos la submatriz de mayor suma como vacía

    # Recorremos todas las submatrices posibles dentro de la matriz
    for i in range(len(matriz)):  # Iteramos sobre las filas de la matriz
        for j in range(len(matriz[0])):  # Iteramos sobre las columnas de la matriz
            for k in range(i, len(matriz)):  # Definimos el límite superior de las filas de la submatriz
                for l in range(j, len(matriz[0])):  # Definimos el límite superior de las columnas de la submatriz
                    # Calculamos la suma de la submatriz actual
                    suma_actual = np.sum(matriz[i:k+1, j:l+1])

                    # Si la suma actual es mayor que la máxima suma registrada hasta ahora
                    if suma_actual > max_suma:
                        max_suma = suma_actual  # Actualizamos la máxima suma
                        submatriz_maxima = matriz[i:k+1, j:l+1]  # Actualizamos la submatriz de mayor suma

    return submatriz_maxima  # Devolvemos la submatriz de mayor suma encontrada

# Creamos una matriz de ejemplo de tamaño 4x4 utilizando np.array que 
#Es una función de la librería NumPy que crea matrices multidimensionales Y 
#Permite convertir listas bidimensionales en matrices NumPy.
matriz_ejemplo = np.array([[1, 2, 3, 4],
                            [5, 6, 7, 8],
                            [9, 10, 11, 12],
                            [13, 14, 15, 16]])

# Llamamos a la función para encontrar la submatriz de mayor suma
submatriz_maxima_encontrada = encontrar_submatriz_maxima(matriz_ejemplo)

# Mostramos la submatriz de mayor suma encontrada
print("La submatriz de mayor suma es:")
print(submatriz_maxima_encontrada)

# %% 

"""Ejercicio 5:
Escribe una función que encuentre la matriz de covarianza de dos matrices"""

import numpy as np  # Importamos la librería NumPy y la renombramos como np

def matriz_covarianza(matriz1, matriz2):
    # Función para calcular la matriz de covarianza entre dos matrices dadas
    covarianza = np.cov(matriz1, matriz2)  # Calculamos la matriz de covarianza utilizando np.cov()
    return covarianza  # Devolvemos la matriz de covarianza calculada

# Creamos dos matrices de ejemplo utilizando np.array que 
#Es una función de la librería NumPy que crea matrices multidimensionales Y 
#Permite convertir listas bidimensionales en matrices NumPy.
matriz1 = np.array([[1, 2, 3],  # Creamos la matriz1 con 2 filas y 3 columnas
                     [4, 5, 6]])

matriz2 = np.array([[7, 8, 9],  # Creamos la matriz2 con 2 filas y 3 columnas
                     [10, 11, 12]])

# Llamamos a la función para encontrar la matriz de covarianza de las dos matrices
matriz_cov = matriz_covarianza(matriz1, matriz2)

# Mostramos la matriz de covarianza encontrada
print("Matriz de covarianza de las dos matrices:")
print(matriz_cov)


# %% 
"""semana 5"""
# %%  
"""1. Escriba una función que reciba un conjunto de números y devuelva un conjunto con 
los números primos."""

def es_primo(numero):
    # Verifica si el número es menor o igual a 1
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    # Itera sobre los números desde 2 hasta la raíz cuadrada del número + 1
    for i in range(2, int(numero ** 0.5) + 1):
        # Si el número es divisible por cualquier número en este rango, no es primo
        if numero % i == 0:
            return False

    return True  # Si el número no es divisible por ningún número, es primo


def numeros_primos(conjunto):
    primos = set()  # Inicializa un conjunto para almacenar los números primos

    # Itera sobre cada número en el conjunto dado
    for num in conjunto:
        # Verifica si el número es primo utilizando la función es_primo()
        if es_primo(num):
            # Si el número es primo, agrégalo al conjunto de números primos
            primos.add(num)

    return primos  # Devuelve el conjunto de números primos


# Ejemplo de uso:
conjunto_de_numeros = {2, 3, 4, 5, 6, 7, 8, 9, 10}

# Imprime el conjunto original
print("Conjunto original:", conjunto_de_numeros)

# Llama a la función numeros_primos para obtener el conjunto de números primos dentro del conjunto dado
numeros_primos_en_conjunto = numeros_primos(conjunto_de_numeros)

# Imprime el conjunto de números primos
print("Conjunto de números primos:", numeros_primos_en_conjunto)




# %%  

"""2. Escriba una función que reciba un conjunto de palabras y devuelva 
un conjunto con las palabras que comienzan con una letra determinada."""

def palabras_con_letra_inicial(conjunto_palabras, letra):
    # Función que recibe un conjunto de palabras y una letra inicial y devuelve las palabras que comienzan con esa letra
    palabras_con_letra = set()  # Inicializamos un conjunto para almacenar las palabras que comienzan con la letra dada
    
    # Iteramos sobre cada palabra en el conjunto dado
    for palabra in conjunto_palabras:
        # Comprobamos si la palabra comienza con la letra dada, ignorando mayúsculas y minúsculas
        if palabra.lower().startswith(letra.lower()):
            palabras_con_letra.add(palabra)  # Agregamos la palabra al conjunto si cumple la condición
    
    return palabras_con_letra  # Devolvemos el conjunto de palabras que comienzan con la letra especificada

# Ejemplo de uso:
conjunto_de_palabras = {"Hola", "Python", "Programación", "lápiz", "avión", "Manzana"}
letra_inicial = "P"

# Imprimimos el conjunto de palabras original
print("Conjunto de palabras original:", conjunto_de_palabras)

# Llamamos a la función palabras_con_letra_inicial para obtener las palabras que comienzan con la letra dada
palabras_con_letra_dada = palabras_con_letra_inicial(conjunto_de_palabras, letra_inicial)

# Imprimimos las palabras que comienzan con la letra dada
print("Palabras que comienzan con la letra '{}':".format(letra_inicial), palabras_con_letra_dada)

# %%  

"""3. Escriba una función que reciba un conjunto de números y devuelva 
un conjunto con los números que son divisibles por un número determinado."""

def numeros_divisibles(conjunto_numeros, divisor):
    # Función que recibe un conjunto de números y un divisor, y devuelve los números divisibles por el divisor
    numeros_divisibles = set()  # Inicializamos un conjunto para almacenar los números divisibles
    
    # Iteramos sobre cada número en el conjunto dado
    for numero in conjunto_numeros:
        # Verificamos si el número es divisible por el divisor
        if numero % divisor == 0:
            numeros_divisibles.add(numero)  # Agregamos el número al conjunto si es divisible por el divisor
    
    return numeros_divisibles  # Devolvemos el conjunto de números divisibles por el divisor

# Ejemplo de uso:
conjunto_de_numeros = {2, 3, 4, 5, 6, 7, 8, 9, 10}
divisor = 3

# Imprimimos el conjunto de números original
print("Conjunto de números original:", conjunto_de_numeros)

# Llamamos a la función numeros_divisibles para obtener los números divisibles por el divisor dado
numeros_divisibles_por_divisor = numeros_divisibles(conjunto_de_numeros, divisor)

# Imprimimos los números divisibles por el divisor
print("Números divisibles por {}: ".format(divisor), numeros_divisibles_por_divisor)

# %%  

"""4. Escriba una función que reciba dos conjuntos de números y devuelva 
un conjunto con los números que están en ambos conjuntos."""

def numeros_en_comun(conjunto1, conjunto2):
    # Función que recibe dos conjuntos de números y devuelve los números que están en ambos conjuntos
    numeros_comunes = conjunto1.intersection(conjunto2)
    # La función intersection() devuelve un conjunto que contiene los elementos que están presentes en ambos conjuntos
    
    return numeros_comunes
    # Devolvemos el conjunto que contiene los números comunes a ambos conjuntos

# Ejemplo de uso:
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Imprimimos los conjuntos originales
print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

# Llamamos a la función numeros_en_comun para encontrar los números que están en ambos conjuntos
numeros_comunes = numeros_en_comun(conjunto1, conjunto2)

# Imprimimos los números en común
print("Números en común:", numeros_comunes)

# %%  

"""5. Escriba una función que reciba dos conjuntos de números y 
devuelva un conjunto con los números que están en el primer conjunto 
pero no en el segundo."""

def numeros_en_primero_no_en_segundo(conjunto1, conjunto2):
    # Función que recibe dos conjuntos de números y devuelve los números que están en el primer conjunto pero no en el segundo
    numeros_diferentes = conjunto1.difference(conjunto2)
    # La función difference() devuelve un conjunto que contiene los elementos que están en el primer conjunto pero no en el segundo
    return numeros_diferentes
    # Devolvemos el conjunto que contiene los números que están en el primer conjunto pero no en el segundo

# Ejemplo de uso:
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Imprimimos los conjuntos originales
print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

# Llamamos a la función numeros_en_primero_no_en_segundo para encontrar los números que están en el primero pero no en el segundo conjunto
numeros_diferentes = numeros_en_primero_no_en_segundo(conjunto1, conjunto2)

# Imprimimos los números que están en el primero pero no en el segundo conjunto
print("Números en el primero pero no en el segundo:", numeros_diferentes)

# %%  

"""6. Escriba una función que reciba dos conjuntos de números y 
devuelva un conjunto con los números que están en el segundo conjunto
 pero no en el primero."""

def numeros_en_segundo_no_en_primero(conjunto1, conjunto2):
    # Función que recibe dos conjuntos de números y devuelve los números que están en el segundo conjunto pero no en el primero
    numeros_diferentes = conjunto2.difference(conjunto1)
    # La función difference() devuelve un conjunto que contiene los elementos que están en el segundo conjunto pero no en el primero
    return numeros_diferentes
    # Devolvemos el conjunto que contiene los números que están en el segundo conjunto pero no en el primero

# Ejemplo de uso:
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Imprimimos los conjuntos originales
print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

# Llamamos a la función numeros_en_segundo_no_en_primero para encontrar los números que están en el segundo pero no en el primer conjunto
numeros_diferentes = numeros_en_segundo_no_en_primero(conjunto1, conjunto2)

# Imprimimos los números que están en el segundo pero no en el primer conjunto
print("Números en el segundo pero no en el primero:", numeros_diferentes)

# %%  

"""7. Escriba una función que reciba un conjunto de palabras y 
devuelva un conjunto con las palabras que son anagramas"""

def encontrar_anagramas(conjunto_palabras):
    # Función que recibe un conjunto de palabras y devuelve un conjunto con las palabras que son anagramas

    anagramas = set()  # Inicializamos un conjunto para almacenar los anagramas encontrados
    conteo_palabras = {}  # Creamos un diccionario para almacenar el conteo de letras en cada palabra

    # Iteramos sobre cada palabra en el conjunto dado
    for palabra in conjunto_palabras:
        # Convertimos la palabra a una tupla de letras ordenadas alfabéticamente
        letras_ordenadas = tuple(sorted(palabra))

        # Agregamos la tupla de letras ordenadas al diccionario y aumentamos su conteo
        conteo_palabras[letras_ordenadas] = conteo_palabras.get(letras_ordenadas, 0) + 1

    # Iteramos sobre los elementos del diccionario
    for letras_ordenadas, conteo in conteo_palabras.items():
        # Si hay más de una palabra con las mismas letras ordenadas, son anagramas
        if conteo > 1:
            # Iteramos sobre las palabras con las letras ordenadas dadas
            for palabra in conjunto_palabras:
                # Si la palabra tiene las letras ordenadas correspondientes, la agregamos al conjunto de anagramas
                if tuple(sorted(palabra)) == letras_ordenadas:
                    anagramas.add(palabra)

    return anagramas

# Ejemplo de uso:
conjunto_de_palabras = {"roma", "amor", "casa", "saca", "perro", "arroz"}

# Imprimimos el conjunto de palabras original
print("Conjunto de palabras:", conjunto_de_palabras)

# Llamamos a la función encontrar_anagramas() y mostramos los resultados
print("Anagramas encontrados:", encontrar_anagramas(conjunto_de_palabras))

# %%  

"""8. Escriba una función que reciba un conjunto de palabras y 
devuelva un conjunto con las palabras que son palíndromos."""

def palabras_palindromos(conjunto_palabras):
    # Función que recibe un conjunto de palabras y devuelve las palabras que son palíndromos
    palindromos = set()  # Inicializamos un conjunto para almacenar los palíndromos
    
    for palabra in conjunto_palabras:  # Iteramos sobre cada palabra en el conjunto dado
        if palabra == palabra[::-1]:   # Comprobamos si la palabra es igual a su reverso
            palindromos.add(palabra)    # Si la palabra es igual a su reverso, la añadimos al conjunto de palíndromos
            
    return palindromos  # Devolvemos el conjunto de palabras que son palíndromos

# Ejemplo de uso:
conjunto_de_palabras = {"radar", "oso", "cívico", "sol", "anana", "python"}

# Imprimimos el conjunto de palabras original
print("Conjunto de palabras original:", conjunto_de_palabras)

# Llamamos a la función palabras_palindromos() y mostramos los palíndromos encontrados
print("Palíndromos en el conjunto:", palabras_palindromos(conjunto_de_palabras))


# %%  

"""9. Escriba una función que reciba un conjunto de palabras y 
devuelva un conjunto con las palabras que tienen una longitud determinada."""

def palabras_longitud(conjunto_palabras, longitud):
    # Función que recibe un conjunto de palabras y una longitud, y devuelve las palabras con la longitud especificada
    palabras_con_longitud = set()  # Inicializamos un conjunto para almacenar las palabras con la longitud especificada
    
    for palabra in conjunto_palabras:  # Iteramos sobre cada palabra en el conjunto dado
        if len(palabra) == longitud:   # Comprobamos si la longitud de la palabra es igual a la longitud especificada
            palabras_con_longitud.add(palabra)  # Si la longitud de la palabra es la requerida, la añadimos al conjunto
            
    return palabras_con_longitud  # Devolvemos el conjunto de palabras con la longitud especificada

# Ejemplo de uso:
conjunto_de_palabras = {"Hola", "Python", "Programación", "lápiz", "avión", "Manzana"}
longitud_deseada = 5

# Imprimimos el conjunto de palabras original
print("Conjunto de palabras original:", conjunto_de_palabras)

# Llamamos a la función palabras_longitud() y mostramos las palabras con la longitud deseada
print("Palabras con longitud {}: ".format(longitud_deseada), palabras_longitud(conjunto_de_palabras, longitud_deseada))

# %% 

"""10. Escriba una función que reciba un conjunto de palabras y 
devuelva un conjunto con las palabras que contienen una letra determinada."""

def palabras_con_letra(conjunto_palabras, letra):
    # Función que recibe un conjunto de palabras y una letra, y devuelve las palabras que contienen la letra especificada
    palabras_con_la_letra = set()  # Inicializamos un conjunto para almacenar las palabras con la letra especificada
    
    for palabra in conjunto_palabras:  # Iteramos sobre cada palabra en el conjunto dado
        if letra in palabra:   # Comprobamos si la letra está presente en la palabra
            palabras_con_la_letra.add(palabra)  # Si la letra está presente, añadimos la palabra al conjunto
    
    return palabras_con_la_letra  # Devolvemos el conjunto de palabras que contienen la letra especificada

# Ejemplo de uso:
conjunto_de_palabras = {"Hola", "Python", "Programación", "lápiz", "avión", "Manzana"}
letra_deseada = 'a'

# Imprimimos el conjunto de palabras original
print("Conjunto de palabras original:", conjunto_de_palabras)

# Llamamos a la función palabras_con_letra() y mostramos las palabras que contienen la letra deseada
print("Palabras que contienen la letra '{}': ".format(letra_deseada), palabras_con_letra(conjunto_de_palabras, letra_deseada))
 
# %%  

"""11. Escriba una función que reciba un conjunto de números y 
devuelva un conjunto con los números que están ordenados de menor a mayor"""

def numeros_ordenados_menor_a_mayor(conjunto_numeros):
    # Función que recibe un conjunto de números y devuelve los números ordenados de menor a mayor
    numeros_ordenados = sorted(conjunto_numeros)  # Ordenamos el conjunto de números
    return set(numeros_ordenados)  # Devolvemos el conjunto ordenado de menor a mayor

# Ejemplo de uso:
conjunto_de_numeros = {5, 2, 8, 1, 9, 3}
print("Conjunto de números original:", conjunto_de_numeros)  # Mostramos el conjunto original
numeros_ordenados = numeros_ordenados_menor_a_mayor(conjunto_de_numeros)  # Llamamos a la función
print("Números ordenados de menor a mayor:", numeros_ordenados)  # Mostramos el resultado ordenado

# %%  

"""12. Escriba una función que reciba un conjunto de números y 
devuelva un conjunto con los números que están ordenados de mayor a menor"""

def numeros_ordenados_mayor_a_menor(conjunto_numeros):
    # Función que recibe un conjunto de números y devuelve los números ordenados de mayor a menor
    numeros_ordenados = sorted(conjunto_numeros, reverse=True)  # Ordenamos el conjunto de números en orden descendente
    return set(numeros_ordenados)  # Devolvemos el conjunto ordenado de mayor a menor

# Ejemplo de uso:
conjunto_de_numeros = {5, 2, 8, 1, 9, 3}
print("Conjunto de números original:", conjunto_de_numeros)  # Mostramos el conjunto original
numeros_ordenados = numeros_ordenados_mayor_a_menor(conjunto_de_numeros)  # Llamamos a la función
print("Números ordenados de mayor a menor:", numeros_ordenados)  # Mostramos el resultado ordenado

# %%  

"""13. Escriba una función que reciba un conjunto de números y 
devuelva un conjunto con los números que están duplicados."""

def numeros_duplicados(conjunto_numeros):
    # Función que recibe un conjunto de números y devuelve los números duplicados
    numeros_duplicados = set()  # Inicializamos un conjunto para almacenar los números duplicados
    numeros_vistos = set()  # Inicializamos un conjunto para almacenar los números que ya hemos visto

    for numero in conjunto_numeros:  # Iteramos sobre cada número en el conjunto dado
        if numero in numeros_vistos:  # Verificamos si ya hemos visto este número antes
            numeros_duplicados.add(numero)  # Si el número ya ha sido visto, lo agregamos al conjunto de duplicados
        else:
            numeros_vistos.add(numero)  # Si el número no ha sido visto antes, lo agregamos al conjunto de vistos

    return numeros_duplicados  # Devolvemos el conjunto de números duplicados

# Ejemplo de uso:
conjunto_de_numeros = {1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10}
print("Conjunto de números original:", conjunto_de_numeros)  # Mostramos el conjunto original
numeros_duplicados_encontrados = numeros_duplicados(conjunto_de_numeros)  # Llamamos a la función
print("Números duplicados:", numeros_duplicados_encontrados)  # Mostramos los números duplicados encontrados

# %%  

"""14. Escriba una función que reciba un conjunto de números y 
devuelva un conjunto con los números que no están duplicados."""

def numeros_no_duplicados(conjunto_numeros):
    # Función que recibe un conjunto de números y devuelve los números que no están duplicados
    numeros_no_duplicados = set()  # Inicializamos un conjunto para almacenar los números que no están duplicados
    numeros_vistos = set()  # Inicializamos un conjunto para almacenar los números que ya hemos visto
    duplicados = set()  # Inicializamos un conjunto para almacenar los números duplicados

    for numero in conjunto_numeros:  # Iteramos sobre cada número en el conjunto dado
        if numero in numeros_vistos:  # Verificamos si ya hemos visto este número antes
            duplicados.add(numero)  # Si el número ya ha sido visto, lo agregamos al conjunto de duplicados
        else:
            numeros_vistos.add(numero)  # Si el número no ha sido visto antes, lo agregamos al conjunto de vistos

    numeros_no_duplicados = conjunto_numeros - duplicados  # Obtenemos los números que no están duplicados

    return numeros_no_duplicados  # Devolvemos el conjunto de números que no están duplicados

# Ejemplo de uso:
conjunto_de_numeros = {1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10}
print("Conjunto de números original:", conjunto_de_numeros)  # Mostramos el conjunto original
numeros_no_duplicados_encontrados = numeros_no_duplicados(conjunto_de_numeros)  # Llamamos a la función
print("Números no duplicados:", numeros_no_duplicados_encontrados)  # Mostramos los números no duplicados encontrados

# %%  

"""15. Escriba una función que reciba un conjunto de números y 
devuelva un conjunto con los números que son primos y están ordenados 
de menor a mayor"""

def es_primo(numero):
    # Función que verifica si un número es primo
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    # Comprobamos si el número es divisible por algún número entre 2 y su raíz cuadrada
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False  # Si es divisible, el número no es primo

    return True  # Si no se encontraron divisores, el número es primo

def numeros_primos_ordenados(conjunto_numeros):
    # Función que recibe un conjunto de números y devuelve los números primos ordenados de menor a mayor
    primos_ordenados = sorted({num for num in conjunto_numeros if es_primo(num)})  # Filtramos los números primos y los ordenamos
    return primos_ordenados  # Devolvemos el conjunto de números primos ordenados

# Ejemplo de uso:
conjunto_de_numeros = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
print("Conjunto de números original:", conjunto_de_numeros)  # Mostramos el conjunto original
numeros_primos = numeros_primos_ordenados(conjunto_de_numeros)  # Llamamos a la función
print("Números primos ordenados:", numeros_primos)  # Mostramos los números primos ordenados encontrados

# %%  

"""16. Escriba una función que reciba un conjunto de palabras y 
devuelva un conjunto con las palabras que sonpalíndromos y están 
ordenadas de menor a mayor."""

def es_palindromo(palabra):
    # Función que verifica si una palabra es un palíndromo
    return palabra == palabra[::-1]

def palabras_palindromos_ordenadas(conjunto_palabras):
    # Función que recibe un conjunto de palabras y devuelve los palíndromos ordenados de menor a mayor
    palindromos_ordenados = sorted({palabra for palabra in conjunto_palabras if es_palindromo(palabra)})
    return palindromos_ordenados

# Ejemplo de uso:
conjunto_de_palabras = {"radar", "oso", "cívico", "sol", "anana", "python"}
print("Conjunto de palabras original:", conjunto_de_palabras)  # Mostramos el conjunto original
palindromos_ordenados = palabras_palindromos_ordenadas(conjunto_de_palabras)  # Llamamos a la función
print("Palíndromos ordenados:", palindromos_ordenados)  # Mostramos los palíndromos ordenados encontrados

# %%  

"""17. Escriba una función que reciba un conjunto de palabras y 
devuelva un conjunto con las palabras que tienen una longitud 
determinada y están ordenadas de menor a mayor."""

def palabras_longitud_ordenadas(conjunto_palabras, longitud):
    # Función que recibe un conjunto de palabras y una longitud, y devuelve las palabras con la longitud especificada, ordenadas
    palabras_longitud = sorted({palabra for palabra in conjunto_palabras if len(palabra) == longitud})
    return palabras_longitud

# Ejemplo de uso:
conjunto_de_palabras = {"Hola", "Python", "Programación", "lápiz", "avión", "Manzana"}
longitud_deseada = 5
print("Conjunto de palabras original:", conjunto_de_palabras)  # Mostramos el conjunto original
palabras_longitud = palabras_longitud_ordenadas(conjunto_de_palabras, longitud_deseada)  # Llamamos a la función
print("Palabras de longitud {} ordenadas:".format(longitud_deseada), palabras_longitud)  # Mostramos las palabras de longitud deseada ordenadas

# %%  

"""18. Escriba una función que reciba un conjunto de palabras y 
devuelva un conjunto con las palabras que contienen una letra 
determinada y están ordenadas de mayor a menor."""

def palabras_con_letra_ordenadas(conjunto_palabras, letra):
    # Función que recibe un conjunto de palabras y una letra, y devuelve las palabras que contienen la letra especificada, ordenadas
    palabras_con_letra = sorted({palabra for palabra in conjunto_palabras if letra in palabra}, reverse=True)
    return palabras_con_letra

# Ejemplo de uso:
conjunto_de_palabras = {"Hola", "Python", "Programación", "lápiz", "avión", "Manzana"}
letra_deseada = 'a'
print("Conjunto de palabras original:", conjunto_de_palabras)  # Mostramos el conjunto original
palabras_con_letra = palabras_con_letra_ordenadas(conjunto_de_palabras, letra_deseada)  # Llamamos a la función
print("Palabras con la letra '{}' ordenadas de mayor a menor:".format(letra_deseada), palabras_con_letra)  # Mostramos las palabras con la letra deseada ordenadas de mayor a menor

# %%  
# %%  
# %%  
# %%  
# %%  
# %%  
# %%  
# %%  
"""19. Escriba una función que reciba un conjunto de números y 
devuelva un conjunto con los números que están ordenados de menor 
a mayor y que no están duplicados."""

def numeros_ordenados_no_duplicados(conjunto_numeros):
    # Función que recibe un conjunto de números y devuelve los números ordenados de menor a mayor y no duplicados
    numeros_ordenados = sorted(set(conjunto_numeros))  # Convertimos el conjunto en una lista, eliminando duplicados, y luego la ordenamos
    return numeros_ordenados

# Ejemplo de uso:
conjunto_de_numeros = {5, 2, 8, 1, 9, 3, 5, 8, 2}  # Ejemplo con duplicados
print("Conjunto de números original:", conjunto_de_numeros)  # Mostramos el conjunto original
numeros_ordenados_no_duplicados = numeros_ordenados_no_duplicados(conjunto_de_numeros)  # Llamamos a la función
print("Números ordenados y no duplicados:", numeros_ordenados_no_duplicados)  # Mostramos los números ordenados y no duplicados

# %% 

"""20. Escriba una función que reciba un conjunto de palabras y 
devuelva un conjunto con las palabras que son palíndromos, tienen
 una longitud determinada y están ordenadas de menor a mayor."""

def es_palindromo(palabra):
    # Función que verifica si una palabra es un palíndromo
    return palabra == palabra[::-1]

def palabras_palindromos_longitud_ordenadas(conjunto_palabras, longitud):
    # Función que recibe un conjunto de palabras, una longitud y devuelve los palíndromos de esa longitud ordenados
    palindromos_ordenados = sorted({palabra for palabra in conjunto_palabras if es_palindromo(palabra) and len(palabra) == longitud})
    return palindromos_ordenados

# Ejemplo de uso:
conjunto_de_palabras = {"radar", "oso", "cívico", "sol", "anana", "python", "reconocer"}
longitud_deseada = 5
print("Conjunto de palabras original:", conjunto_de_palabras)  # Mostramos el conjunto original
palindromos_longitud_ordenados = palabras_palindromos_longitud_ordenadas(conjunto_de_palabras, longitud_deseada)  # Llamamos a la función
print("Palíndromos de longitud {} ordenados:".format(longitud_deseada), palindromos_longitud_ordenados)  # Mostramos los palíndromos de longitud deseada ordenados     
    

#%%
#%% SEMANA 8 Y 9

# #problema1
# #EJERCICIO PARTE1
# # 1. Validar la edad de un usuario.

def validar_edad(edad):
    """
    Función para validar la edad de un usuario.
    """
    try:
        # Convertimos la edad a un entero
        edad = int(edad)
        # Verificamos si la edad es un entero positivo
        assert edad >= 0, "La edad debe ser un número positivo."
        # Verificamos si la edad está dentro del rango válido
        assert 0 < edad <= 120, "La edad debe estar entre 1 y 120 años."
        # Si todas las validaciones pasan, la edad es válida
        print("La edad es válida.")
    except ValueError:
        # Capturamos el error si no se puede convertir la edad a un entero
        print("Error: La edad debe ser un número entero.")
    except AssertionError as e:
        # Capturamos el error si la edad no cumple con las condiciones
        print("Error:", e)

# Llamamos a la función para validar la edad
validar_edad("25")


#%%
# # 2. Verificar el tipo de dato de una variable.
    
def verificar_tipo_dato(variable): #Esta línea define una función llamada verificar_tipo_dato
    """
    Función que verifica el tipo de dato de una variable.

    Args:
    - variable: La variable cuyo tipo de dato se desea verificar.

    Returns:
    - str: Una cadena que indica el tipo de dato de la variable.
    """
    tipo_dato = type(variable).__name__  # Obtenemos el nombre del tipo de dato de la variable
    return tipo_dato

# Ejemplo de uso
mi_variable = 42
tipo_dato_variable = verificar_tipo_dato(mi_variable)  # Verificamos el tipo de dato de la variable

print(f"El tipo de dato de la variable es: {tipo_dato_variable}") # imprimir



 #%%   
# # 3. Validar el rango de una calificación.
def validar_calificacion(calificacion):     ##Esta línea define una función llamada validar_calificacion
    """
    Función para validar el rango de una calificación.

    Args:
    - calificacion: float, la calificación a validar.

    Returns:
    - bool: True si la calificación está en el rango válido, False de lo contrario.
    """
    if 0 <= calificacion <= 10:  # Verifica si la calificación está en el rango de 0 a 10
        return True  # Devuelve True si la calificación está en el rango válido
    else:
        return False  # Devuelve False si la calificación está fuera del rango válido

# Ejemplo de uso
while True:
    try:
        calificacion = float(input("Ingrese la calificación: "))  # Solicita al usuario ingresar la calificación
        if validar_calificacion(calificacion):  # Llama a la función para validar la calificación
            print("La calificación es válida.")
            break  # Sale del bucle si la calificación es válida
        else:
            print("La calificación debe estar en el rango de 0 a 10. Inténtelo nuevamente.")
    except ValueError:
        print("Ingrese un valor numérico válido.")


#%%
# # 4. Asegurar que una lista no esté vacía.
def asegurar_lista_no_vacia(lista):     ##Esta línea define una función llamada asegurar_lista_no_vacia
    """
    Función para asegurar que una lista no esté vacía.

    Args:
    - lista: list, la lista que se desea verificar.

    Returns:
    - bool: True si la lista no está vacía, False de lo contrario.
    """
    if lista:  # Verifica si la lista tiene al menos un elemento
        return True  # Devuelve True si la lista no está vacía
    else:
        return False  # Devuelve False si la lista está vacía

# Ejemplo de uso
mi_lista = [1, 2, 3]
if asegurar_lista_no_vacia(mi_lista):  # Llama a la función para verificar si la lista no está vacía
    print("La lista no está vacía.")
else:
    print("La lista está vacía.")

    print("La lista está vacía.")
#%%
# # 5. Validar la igualdad de dos objetos.

class Persona:
    """
    Clase que representa a una persona con un nombre y una edad.
    """
    def __init__(self, nombre, edad):
        # Inicializamos los atributos de la clase Persona
        self.nombre = nombre
        self.edad = edad

# Creamos dos objetos de la clase Persona
persona1 = Persona("Juan", 30)  # Creamos el primer objeto Persona con nombre "Juan" y edad 30
persona2 = Persona("Juan", 30)  # Creamos el segundo objeto Persona con nombre "Juan" y edad 30

# Validamos la igualdad de los dos objetos
assert persona1 == persona2, "Los objetos no son iguales."

# Imprimimos el resultado de la validación
print("Los objetos son iguales:", persona1 == persona2)

#%%
# # 6. Asegurar que un ciclo while se ejecuta al menos una vez.
# # Definir una variable
# Definimos una función que simula un ciclo while que se ejecuta al menos una vez

def ciclo_while_al_menos_una_vez():
    """
    Función para simular un ciclo while que se ejecuta al menos una vez.
    """
    contador = 0  # Inicializamos el contador
    total = 0  # Inicializamos el total

    while True:  # Iniciamos un ciclo while infinito
        total += contador  # Sumamos el valor del contador al total
        contador += 1  # Incrementamos el contador en 1

        if contador >= 5:  # Si el contador es mayor o igual a 5, salimos del ciclo
            break

    assert total > 0, "El ciclo while no se ejecutó al menos una vez."

    # Si la aserción es verdadera, imprimimos el total calculado
    print("El ciclo while se ejecutó al menos una vez. Total:", total)

# Llamamos a la función para simular el ciclo while
ciclo_while_al_menos_una_vez()


#%%
# # 7. Asegurar que una función retorna un valor específico.
def dividir(a, b):
    """
    Función para dividir dos números y asegurar que el resultado sea un valor específico.
    """
    assert b != 0, "No se puede dividir entre cero."  # Aseguramos que el divisor no sea cero
    resultado = a / b
    return resultado

# Llamamos a la función para dividir dos números y verificar el resultado
resultado_division = dividir(10, 2)

# Aseguramos que el resultado de la división sea igual a 5
assert resultado_division == 5, "El resultado de la división no es el esperado."

print("La función retornó el valor específico correctamente:", resultado_division)


#%%
# # 8. Validar el estado de una variable después de una operación.
# # Definir una variable

# Definimos una función para validar el estado de una variable después de una operación
def validar_estado_variable():
    """
    Función para validar el estado de una variable después de una operación.
    """
    variable = 5  # Inicializamos la variable con un valor inicial

    # Realizamos una operación en la variable
    variable *= 2  # Multiplicamos la variable por 2

    # Validamos el estado de la variable después de la operación
    assert variable == 10, "El estado de la variable no es correcto después de la operación."

    # Si la aserción es verdadera, imprimimos un mensaje indicando que el estado de la variable es correcto
    print("El estado de la variable es correcto después de la operación.")

# Llamamos a la función para validar el estado de la variable después de una operación
validar_estado_variable()

    
#%%
# 9. Asegurar que un módulo se ha importado correctamente.
# Importar el módulo
try:
    import modulo_ejemplo  # Intentamos importar el módulo deseado
    
    # Si no hay errores al importar el módulo, se imprimirá un mensaje de confirmación
    print("El módulo se ha importado correctamente.")
    
except ModuleNotFoundError:
    # Si el módulo no se encuentra o hay algún error en la importación, se captura la excepción ModuleNotFoundError
    print("No se pudo importar el módulo. Verifique que el módulo exista y esté accesible.")



#%%
# Ejercicios parte 02:
# 10. Desarrollar el código de buscar nodo en la lista enlazada simple.

class Nodo:     # Esta línea define una clase llamada Nodo
    """
    Clase que define un nodo de una lista enlazada simple.
    """
    def __init__(self, dato):
        # Inicializamos el nodo con un dato y un enlace al siguiente nodo
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaSimple:
    """
    Clase que define una lista enlazada simple.
    """
    def __init__(self):
        # Inicializamos la lista enlazada con un nodo cabeza
        self.cabeza = None

    def buscar(self, dato):
        """
        Función para buscar un nodo con un dato específico en la lista enlazada.
        """
        actual = self.cabeza  # Comenzamos desde el nodo cabeza

        while actual is not None:
            if actual.dato == dato:  # Comparamos el dato del nodo actual con el dato buscado
                return True  # Si encontramos el dato, retornamos True
            actual = actual.siguiente  # Pasamos al siguiente nodo

        return False  # Si no encontramos el dato, retornamos False

# Creamos una lista enlazada simple
lista = ListaEnlazadaSimple()

# Añadimos algunos nodos a la lista
lista.cabeza = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
lista.cabeza.siguiente = nodo2
nodo2.siguiente = nodo3

# Buscamos un nodo con dato 2 en la lista
resultado = lista.buscar(2)
print("¿El nodo con dato 2 se encuentra en la lista?", resultado)

#%%
# Suma de Nodos
# 11. Implementa una función que sume todos los nodos de una lista enlazada simple.
class Nodo:     # Esta línea define una clase llamada Nodo
    """
    Clase que define un nodo de una lista enlazada simple.
    """
    def __init__(self, dato):
        # Inicializamos el nodo con un dato y un enlace al siguiente nodo
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaSimple:
    """
    Clase que define una lista enlazada simple.
    """
    def __init__(self):
        # Inicializamos la lista enlazada con un nodo cabeza
        self.cabeza = None

    def agregar_nodo(self, dato):
        """
        Agrega un nuevo nodo al final de la lista enlazada.
        """
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def sumar_nodos(self):
        """
        Calcula la suma de todos los nodos de la lista enlazada.
        """
        suma = 0
        actual = self.cabeza
        while actual is not None:
            suma += actual.dato
            actual = actual.siguiente
        return suma

# Creamos una lista enlazada simple
lista = ListaEnlazadaSimple()

# Agregamos algunos nodos a la lista
lista.agregar_nodo(1)
lista.agregar_nodo(2)
lista.agregar_nodo(3)
lista.agregar_nodo(4)
lista.agregar_nodo(5)

# Calculamos la suma de todos los nodos de la lista
resultado = lista.sumar_nodos()
print("La suma de los nodos de la lista es:", resultado)


#%%
# Longitud de la Lista
# 12. Crea una función que devuelva la longitud de una lista enlazada simple.

def longitud_lista(self):       # Esta línea define una clase llamada longitud_lista
    """
    Devuelve la longitud de la lista enlazada simple.
    """
    longitud = 0  # Inicializamos la longitud en 0
    actual = self.cabeza  # Empezamos desde el nodo cabeza
    
    while actual is not None:
        longitud += 1  # Incrementamos la longitud en 1 por cada nodo encontrado
        actual = actual.siguiente  # Avanzamos al siguiente nodo
        
    return longitud  # Devolvemos la longitud encontrada


#%%
# Concatenar Listas
# 13. Implementa una función que concatene dos listas enlazadas simples.
def concatenar_listas(self, otra_lista):
    """
    Concatena la lista actual con otra lista enlazada simple.
    """
    if self.cabeza is None:  # Si la lista actual está vacía
        self.cabeza = otra_lista.cabeza  # La cabeza de la lista actual apunta a la cabeza de la otra lista
    else:
        actual = self.cabeza  # Comenzamos desde la cabeza de la lista actual
        while actual.siguiente is not None:  # Recorremos hasta el último nodo de la lista actual
            actual = actual.siguiente
        actual.siguiente = otra_lista.cabeza  # Enlazamos el último nodo de la lista actual con la cabeza de la otra lista

#%%
# Eliminar Duplicados
# 14. Crea una función que elimine los nodos duplicados de una lista enlazada simple.

def eliminar_duplicados(self):  # Esta línea define una clase llamada eliminar_duplicados
    """
    Elimina los nodos duplicados de la lista enlazada simple.
    """
    if self.cabeza is None:  # Si la lista está vacía, no hay nada que hacer
        return

    nodos_vistos = set()  # Creamos un conjunto para almacenar los valores de los nodos vistos
    anterior = None  # Inicializamos un puntero anterior como None
    actual = self.cabeza  # Empezamos desde el nodo cabeza

    while actual is not None:  # Recorremos la lista
        if actual.dato in nodos_vistos:  # Si el dato del nodo actual ya ha sido visto
            anterior.siguiente = actual.siguiente  # Eliminamos el nodo actual
        else:
            nodos_vistos.add(actual.dato)  # Agregamos el dato del nodo actual al conjunto de nodos vistos
            anterior = actual  # Movemos el puntero anterior al nodo actual
        actual = actual.siguiente  # Movemos el puntero actual al siguiente nodo


    
#%%
# Invertir Lista
# 15. Implementa una función que invierta el orden de una lista enlazada simple

def invertir_lista(self): # Esta línea define una clase llamada invertir_lista
    """
    Invierte el orden de una lista enlazada simple.
    """
    anterior = None  # Inicializamos un puntero anterior como None
    actual = self.cabeza  # Empezamos desde el nodo cabeza

    while actual is not None:  # Recorremos la lista
        siguiente_temp = actual.siguiente  # Guardamos el siguiente nodo temporalmente
        actual.siguiente = anterior  # Invertimos el puntero del nodo actual para que apunte al nodo anterior
        anterior = actual  # Movemos el puntero anterior al nodo actual
        actual = siguiente_temp  # Movemos el puntero actual al siguiente nodo

    self.cabeza = anterior  # El nodo anterior es ahora la nueva cabeza de la lista (último nodo original)

#%% LABORATORIO DE 10 Y 11
#%%bn
# Ejercicio parte 01 – Listas Enlazadas Dobles:
# Duplicar Nodos:
# 1. Crea una lista con al menos 4 nodos, duplica cada nodo de la lista e imprime la lista original y la lista 
# duplicada hacia adelante y hacia atrás.

class Nodo:     # Esta línea define una clase llamada Nodo
    def __init__(self, valor):  #define un método que inicializa un objeto de la clase Nodo
        self.valor = valor  # Establece el valor del nodo
        self.siguiente = None  # Inicializa el puntero al siguiente nodo como None
        self.anterior = None  # Inicializa el puntero al nodo anterior como None

# Creamos la lista original con al menos 4 nodos
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)

nodo1.siguiente = nodo2  # Enlaza nodo1 con nodo2
nodo2.anterior = nodo1  # Enlaza nodo2 con nodo1
nodo2.siguiente = nodo3  # Enlaza nodo2 con nodo3
nodo3.anterior = nodo2  # Enlaza nodo3 con nodo2
nodo3.siguiente = nodo4  # Enlaza nodo3 con nodo4
nodo4.anterior = nodo3  # Enlaza nodo4 con nodo3

# Función para duplicar los nodos
def duplicar_nodos(lista):
    if lista is None:
        return

    actual = lista
    while actual is not None:
        nuevo_nodo = Nodo(actual.valor)  # Crea un nuevo nodo con el mismo valor que el nodo actual
        nuevo_nodo.siguiente = actual.siguiente  # Establece el siguiente del nuevo nodo al siguiente del nodo actual
        if actual.siguiente:  # Verifica si hay un siguiente nodo al nodo actual
            actual.siguiente.anterior = nuevo_nodo  # Establece el nodo anterior al siguiente nodo al nuevo nodo
        actual.siguiente = nuevo_nodo  # Establece el siguiente del nodo actual al nuevo nodo
        nuevo_nodo.anterior = actual  # Establece el nodo anterior al nuevo nodo al nodo actual
        actual = actual.siguiente.siguiente  # Avanza dos pasos en la lista

# Duplicamos los nodos
duplicar_nodos(nodo1)

# Función para imprimir la lista hacia adelante
def imprimir_adelante(lista):
    actual = lista
    while actual:
        print(actual.valor, end=" -> ")
        actual = actual.siguiente
    print("None")

# Función para imprimir la lista hacia atrás
def imprimir_atras(lista):
    actual = lista
    while actual.siguiente:
        actual = actual.siguiente
    while actual:
        print(actual.valor, end=" -> ")
        actual = actual.anterior
    print("None")

# Imprimimos la lista original hacia adelante y hacia atrás
print("Lista original hacia adelante:")
imprimir_adelante(nodo1)
print("Lista original hacia atrás:")
imprimir_atras(nodo1)

# Imprimimos la lista duplicada hacia adelante y hacia atrás
print("Lista duplicada hacia adelante:")
imprimir_adelante(nodo1)
print("Lista duplicada hacia atrás:")
imprimir_atras(nodo1)


#%%bn
# Contar Nodos Pares e Impares:
# 2. Crea una lista con al menos 9 nodos, cuenta cuántos nodos tienen un dato par y cuántos tienen un dato 
# impar e imprime la lista hacia adelante y hacia atrás.
class Nodo:     # Esta línea define una clase llamada Nodo
    def __init__(self, dato):   #define un método que inicializa un objeto de la clase Nodo
        self.dato = dato  # Establece el dato del nodo
        self.siguiente = None  # Inicializa el puntero al siguiente nodo como None
        self.anterior = None  # Inicializa el puntero al nodo anterior como None

# Creamos la lista con al menos 9 nodos
nodo1 = Nodo(1)  # Creamos el primer nodo con el dato 1
nodo2 = Nodo(2)  # Creamos el segundo nodo con el dato 2
nodo3 = Nodo(3)  # Creamos el tercer nodo con el dato 3
nodo4 = Nodo(4)  # Creamos el cuarto nodo con el dato 4
nodo5 = Nodo(5)  # Creamos el quinto nodo con el dato 5
nodo6 = Nodo(6)  # Creamos el sexto nodo con el dato 6
nodo7 = Nodo(7)  # Creamos el séptimo nodo con el dato 7
nodo8 = Nodo(8)  # Creamos el octavo nodo con el dato 8
nodo9 = Nodo(9)  # Creamos el noveno nodo con el dato 9

# Enlazamos los nodos para formar la lista
nodo1.siguiente = nodo2
nodo2.anterior = nodo1
nodo2.siguiente = nodo3
nodo3.anterior = nodo2
nodo3.siguiente = nodo4
nodo4.anterior = nodo3
nodo4.siguiente = nodo5
nodo5.anterior = nodo4
nodo5.siguiente = nodo6
nodo6.anterior = nodo5
nodo6.siguiente = nodo7
nodo7.anterior = nodo6
nodo7.siguiente = nodo8
nodo8.anterior = nodo7
nodo8.siguiente = nodo9
nodo9.anterior = nodo8

# Función para contar nodos pares e impares
def contar_pares_impares(lista):
    contador_pares = 0  # Inicializa el contador de nodos pares
    contador_impares = 0  # Inicializa el contador de nodos impares
    actual = lista  # Establece el nodo actual como el inicio de la lista
    while actual:
        if actual.dato % 2 == 0:  # Verifica si el dato del nodo es par
            contador_pares += 1  # Incrementa el contador de nodos pares
        else:
            contador_impares += 1  # Incrementa el contador de nodos impares
        actual = actual.siguiente  # Avanza al siguiente nodo en la lista
    return contador_pares, contador_impares  # Devuelve el conteo de nodos pares e impares

# Función para imprimir la lista hacia adelante
def imprimir_adelante(lista):
    actual = lista  # Establece el nodo actual como el inicio de la lista
    while actual:
        print(actual.dato, end=" -> ")  # Imprime el dato del nodo seguido de una flecha
        actual = actual.siguiente  # Avanza al siguiente nodo en la lista
    print("None")  # Imprime "None" al final de la lista

# Función para imprimir la lista hacia atrás
def imprimir_atras(lista):
    actual = lista  # Establece el nodo actual como el inicio de la lista
    while actual.siguiente:  # Encuentra el último nodo de la lista
        actual = actual.siguiente
    while actual:  # Imprime los nodos en orden inverso
        print(actual.dato, end=" -> ")  # Imprime el dato del nodo seguido de una flecha
        actual = actual.anterior  # Avanza al nodo anterior en la lista
    print("None")  # Imprime "None" al final de la lista

# Contamos nodos pares e impares
pares, impares = contar_pares_impares(nodo1)

# Imprimimos la lista hacia adelante y hacia atrás
print("Lista hacia adelante:")
imprimir_adelante(nodo1)
print("Lista hacia atrás:")
imprimir_atras(nodo1)

# Imprimimos el conteo de nodos pares e impares
print("Nodos pares:", pares)
print("Nodos impares:", impares)


#%%bn
# Insertar Nodo en Posición Específica:
# 3. Crea una lista con al menos 5 nodos, inserta un nuevo nodo con el dato 15 en la posición 3 e imprime la 
# lista hacia adelante y hacia atrás.
class Nodo:     # Esta línea define una clase llamada Nodo
    def __init__(self, dato):   #define un método que inicializa un objeto de la clase Nodo
        self.dato = dato  # Establece el dato del nodo
        self.siguiente = None  # Inicializa el puntero al siguiente nodo como None
        self.anterior = None  # Inicializa el puntero al nodo anterior como None

# Creamos la lista con al menos 5 nodos
nodo1 = Nodo(1)  # Creamos el primer nodo con el dato 1
nodo2 = Nodo(2)  # Creamos el segundo nodo con el dato 2
nodo3 = Nodo(3)  # Creamos el tercer nodo con el dato 3
nodo4 = Nodo(4)  # Creamos el cuarto nodo con el dato 4
nodo5 = Nodo(5)  # Creamos el quinto nodo con el dato 5

# Enlazamos los nodos para formar la lista
nodo1.siguiente = nodo2
nodo2.anterior = nodo1
nodo2.siguiente = nodo3
nodo3.anterior = nodo2
nodo3.siguiente = nodo4
nodo4.anterior = nodo3
nodo4.siguiente = nodo5
nodo5.anterior = nodo4

# Función para insertar un nuevo nodo en una posición específica
def insertar_nodo(posicion, dato, lista):
    nuevo_nodo = Nodo(dato)  # Creamos un nuevo nodo con el dato dado
    actual = lista  # Establecemos el nodo actual como el inicio de la lista
    for _ in range(posicion - 1):  # Avanzamos a la posición deseada en la lista
        actual = actual.siguiente
    nuevo_nodo.siguiente = actual.siguiente  # Enlazamos el nuevo nodo con el siguiente nodo
    nuevo_nodo.anterior = actual  # Enlazamos el nuevo nodo con el nodo anterior
    if actual.siguiente:  # Verificamos si hay un nodo siguiente
        actual.siguiente.anterior = nuevo_nodo  # Enlazamos el nodo siguiente con el nuevo nodo
    actual.siguiente = nuevo_nodo  # Enlazamos el nodo actual con el nuevo nodo

# Insertamos un nuevo nodo con el dato 15 en la posición 3
insertar_nodo(3, 15, nodo1)

# Función para imprimir la lista hacia adelante
def imprimir_adelante(lista):
    actual = lista  # Establecemos el nodo actual como el inicio de la lista
    while actual:
        print(actual.dato, end=" -> ")  # Imprimimos el dato del nodo seguido de una flecha
        actual = actual.siguiente  # Avanzamos al siguiente nodo en la lista
    print("None")  # Imprimimos "None" al final de la lista

# Función para imprimir la lista hacia atrás
def imprimir_atras(lista):
    actual = lista  # Establecemos el nodo actual como el inicio de la lista
    while actual.siguiente:  # Encuentramos el último nodo de la lista
        actual = actual.siguiente
    while actual:  # Imprimimos los nodos en orden inverso
        print(actual.dato, end=" -> ")  # Imprimimos el dato del nodo seguido de una flecha
        actual = actual.anterior  # Retrocedemos al nodo anterior en la lista
    print("None")  # Imprimimos "None" al final de la lista

# Imprimimos la lista hacia adelante y hacia atrás
print("Lista hacia adelante:")
imprimir_adelante(nodo1)
print("Lista hacia atrás:")
imprimir_atras(nodo1)


#%% bn
# Eliminar Nodos Duplicados:
# 4. Crea una lista con nodos que contengan datos duplicados, elimina todos los nodos duplicados, dejando 
# solo una instancia de cada dato e imprime la lista hacia adelante y hacia atrás.
class Nodo:     # Esta línea define una clase llamada Nodo
    def __init__(self, dato):   #define un método que inicializa un objeto de la clase Nodo
        self.dato = dato  # Establece el dato del nodo
        self.siguiente = None  # Inicializa el puntero al siguiente nodo como None
        self.anterior = None  # Inicializa el puntero al nodo anterior como None

# Creamos la lista con nodos que contienen datos duplicados
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(2)  # Dato duplicado
nodo5 = Nodo(4)
nodo6 = Nodo(3)  # Dato duplicado

# Enlazamos los nodos para formar la lista
nodo1.siguiente = nodo2
nodo2.anterior = nodo1
nodo2.siguiente = nodo3
nodo3.anterior = nodo2
nodo3.siguiente = nodo4
nodo4.anterior = nodo3
nodo4.siguiente = nodo5
nodo5.anterior = nodo4
nodo5.siguiente = nodo6
nodo6.anterior = nodo5

# Función para eliminar nodos duplicados en la lista
def eliminar_duplicados(lista):
    if lista is None:  # Si la lista está vacía, no hacemos nada
        return

    actual = lista  # Establece el nodo actual como el inicio de la lista
    while actual:
        dato_actual = actual.dato  # Obtenemos el dato del nodo actual
        siguiente_nodo = actual.siguiente  # Obtenemos el siguiente nodo
        while siguiente_nodo:
            if siguiente_nodo.dato == dato_actual:  # Si encontramos un nodo con dato duplicado
                siguiente_siguiente = siguiente_nodo.siguiente  # Obtenemos el nodo siguiente al duplicado
                actual.siguiente = siguiente_siguiente  # Enlazamos el nodo actual con el nodo siguiente al duplicado
                if siguiente_siguiente:  # Si hay un nodo siguiente al duplicado
                    siguiente_siguiente.anterior = actual  # Enlazamos el nodo siguiente al duplicado con el nodo actual
            siguiente_nodo = siguiente_nodo.siguiente
        actual = actual.siguiente  # Pasamos al siguiente nodo en la lista

# Llamamos a la función para eliminar los nodos duplicados
eliminar_duplicados(nodo1)

# Función para imprimir la lista hacia adelante
def imprimir_adelante(lista):
    actual = lista  # Establecemos el nodo actual como el inicio de la lista
    while actual:
        print(actual.dato, end=" -> ")  # Imprimimos el dato del nodo seguido de una flecha
        actual = actual.siguiente  # Avanzamos al siguiente nodo en la lista
    print("None")  # Imprimimos "None" al final de la lista

# Función para imprimir la lista hacia atrás
def imprimir_atras(lista):
    actual = lista  # Establecemos el nodo actual como el inicio de la lista
    while actual.siguiente:  # Encuentramos el último nodo de la lista
        actual = actual.siguiente
    while actual:  # Imprimimos los nodos en orden inverso
        print(actual.dato, end=" -> ")  # Imprimimos el dato del nodo seguido de una flecha
        actual = actual.anterior  # Retrocedemos al nodo anterior en la lista
    print("None")  # Imprimimos "None" al final de la lista

# Imprimimos la lista hacia adelante y hacia atrás después de eliminar los duplicados
print("Lista después de eliminar nodos duplicados:")
imprimir_adelante(nodo1)
print("Lista hacia atrás:")
imprimir_atras(nodo1)

#%% bn
# Invertir la Lista:
# 5. Crea una lista con al menos 6 nodos, invierte el orden de la lista (el último elemento se convierte en el 
# primero y viceversa) e imprime la lista hacia adelante y hacia atrás

class Nodo:     # Esta línea define una clase llamada Nodo
    def __init__(self, dato):   #define un método que inicializa un objeto de la clase Nodo
        self.dato = dato  # Establece el dato del nodo
        self.siguiente = None  # Inicializa el puntero al siguiente nodo como None
        self.anterior = None  # Inicializa el puntero al nodo anterior como None

# Creamos la lista con al menos 6 nodos
nodo1 = Nodo(1)  # Creamos el primer nodo con el dato 1
nodo2 = Nodo(2)  # Creamos el segundo nodo con el dato 2
nodo3 = Nodo(3)  # Creamos el tercer nodo con el dato 3
nodo4 = Nodo(4)  # Creamos el cuarto nodo con el dato 4
nodo5 = Nodo(5)  # Creamos el quinto nodo con el dato 5
nodo6 = Nodo(6)  # Creamos el sexto nodo con el dato 6

# Enlazamos los nodos para formar la lista
nodo1.siguiente = nodo2
nodo2.anterior = nodo1
nodo2.siguiente = nodo3
nodo3.anterior = nodo2
nodo3.siguiente = nodo4
nodo4.anterior = nodo3
nodo4.siguiente = nodo5
nodo5.anterior = nodo4
nodo5.siguiente = nodo6
nodo6.anterior = nodo5

# Función para invertir la lista
def invertir_lista(lista):
    actual = lista  # Establecemos el nodo actual como el inicio de la lista
    ultimo = None  # Inicializamos el nodo último como None
    while actual:
        siguiente_temporal = actual.siguiente  # Guardamos el siguiente nodo temporalmente
        actual.siguiente = actual.anterior  # Invertimos el puntero siguiente y anterior del nodo actual
        actual.anterior = siguiente_temporal  # Establecemos el puntero anterior como el siguiente temporal
        ultimo = actual  # Actualizamos el último nodo
        actual = siguiente_temporal  # Avanzamos al siguiente nodo
    return ultimo  # Devolvemos el último nodo, que se convierte en el primero

# Invertimos la lista
nuevo_primero = invertir_lista(nodo1)

# Función para imprimir la lista hacia adelante
def imprimir_adelante(lista):
    actual = lista  # Establecemos el nodo actual como el inicio de la lista
    while actual:
        print(actual.dato, end=" -> ")  # Imprimimos el dato del nodo seguido de una flecha
        actual = actual.siguiente  # Avanzamos al siguiente nodo en la lista
    print("None")  # Imprimimos "None" al final de la lista

# Función para imprimir la lista hacia atrás
def imprimir_atras(lista):
    actual = lista  # Establecemos el nodo actual como el inicio de la lista
    while actual.siguiente:  # Encuentramos el último nodo de la lista
        actual = actual.siguiente
    while actual:  # Imprimimos los nodos en orden inverso
        print(actual.dato, end=" -> ")  # Imprimimos el dato del nodo seguido de una flecha
        actual = actual.anterior  # Retrocedemos al nodo anterior en la lista
    print("None")  # Imprimimos "None" al final de la lista

# Imprimimos la lista invertida hacia adelante y hacia atrás
print("Lista invertida hacia adelante:")
imprimir_adelante(nuevo_primero)
print("Lista invertida hacia atrás:")
imprimir_atras(nuevo_primero)

#%%
# Ejercicios parte 02:
#%% bn
# Invertir una cadena:
 # 6. Utilizar una pila para invertir el orden de los caracteres de una cadena.

class Pila:     # Esta línea define una clase llamada Pila
    def __init__(self): #define un método que inicializa un objeto de la clase Nodo
        self.items = []  # Inicializamos una lista para almacenar los elementos de la pila

    def esta_vacia(self):
        return len(self.items) == 0  # Verificamos si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agregamos un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Eliminamos y devolvemos el elemento superior de la pila
        else:
            return None  # Devolvemos None si la pila está vacía

def invertir_cadena(cadena):
    pila = Pila()  # Creamos una instancia de la clase Pila

    # Apilamos cada carácter de la cadena en la pila en orden inverso
    for caracter in cadena:
        pila.apilar(caracter)

    cadena_invertida = ""  # Inicializamos una cadena vacía para almacenar la cadena invertida

    # Desapilamos los caracteres de la pila y los agregamos a la cadena invertida
    while not pila.esta_vacia():
        cadena_invertida += pila.desapilar()

    return cadena_invertida  # Devolvemos la cadena invertida

# Ejemplo de uso
cadena_original = "Hola Mundo"
cadena_invertida = invertir_cadena(cadena_original)
print("Cadena original:", cadena_original)
print("Cadena invertida:", cadena_invertida)

#%% bn
# # Convertir número decimal a binario:
# # 7. Implementar un programa que convierta un número decimal a su representación en sistema binario 
# # utilizando una pila.

class Pila:     # Esta línea define una clase llamada Pila
    def __init__(self): #define un método que inicializa un objeto de la clase Nodo
        self.items = []  # Inicializamos una lista para almacenar los elementos de la pila

    def esta_vacia(self):
        return len(self.items) == 0  # Verificamos si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agregamos un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Eliminamos y devolvemos el elemento superior de la pila
        else:
            return None  # Devolvemos None si la pila está vacía

def decimal_a_binario(decimal):
    pila = Pila()  # Creamos una instancia de la clase Pila

    # Convertimos el número decimal a binario
    while decimal > 0:
        residuo = decimal % 2  # Obtenemos el residuo de la división por 2
        pila.apilar(residuo)  # Apilamos el residuo en la pila
        decimal = decimal // 2  # Actualizamos el valor de decimal dividiéndolo por 2

    # Construimos la representación binaria a partir de los elementos de la pila
    binario = ""
    while not pila.esta_vacia():
        binario += str(pila.desapilar())  # Desapilamos los elementos y los concatenamos como cadenas

    return binario if binario != "" else "0"  # Devolvemos la representación binaria

# Solicitamos al usuario que ingrese un número decimal
numero_decimal = int(input("Ingresa un número decimal: "))

# Convertimos el número decimal a binario y lo imprimimos
numero_binario = decimal_a_binario(numero_decimal)
print("El número decimal", numero_decimal, "en binario es:", numero_binario)

#%%
# # Evaluar expresión posfija:
# # 8. Crear un programa que evalúe una expresión matemática en notación posfija utilizando una pila.

class Pila:     # Esta línea define una clase llamada Pila
    def __init__(self): #define un método que inicializa un objeto de la clase Nodo
        self.items = []  # Inicializamos una lista para almacenar los elementos de la pila

    def esta_vacia(self):
        return len(self.items) == 0  # Verificamos si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agregamos un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Eliminamos y devolvemos el elemento superior de la pila
        else:
            return None  # Devolvemos None si la pila está vacía

def evaluar_expresion_posfija(expresion):
    pila = Pila()  # Creamos una instancia de la clase Pila
    tokens = expresion.split()  # Dividimos la expresión en tokens (números y operadores)

    for token in tokens:
    if token.isdigit():
        pila.apilar(int(token))  # Si el token es un número, lo apilamos en la pila
    else:
        operando2 = pila.desapilar()  # Desapilamos el segundo operando de la pila
        operando1 = pila.desapilar()   # Desapilamos el primer operando de la pila
        if operando1 is not None and operando2 is not None:  # Verificamos que haya suficientes operandos en la pila
            if token == '+':   # Si el token es un operador de suma
                pila.apilar(operando1 + operando2)  # Apilamos el resultado de la suma
            elif token == '-':  # Si el token es un operador de resta
                pila.apilar(operando1 - operando2)  # Apilamos el resultado de la resta
            elif token == '*':  # Si el token es un operador de multiplicación
                pila.apilar(operando1 * operando2)  # Apilamos el resultado de la multiplicación
            elif token == '/':  # Si el token es un operador de división
                if operando2 != 0:   # Verificamos que no haya división por cero
                    pila.apilar(operando1 / operando2)  # Apilamos el resultado de la división
                else:
                    return "Error: División por cero"  # Retornamos un mensaje de error si hay división por cero
        else:
            return "Error: Expresión posfija mal formada"  # Retornamos un mensaje de error si la expresión posfija está mal formada

return pila.desapilar()  # Retornamos el resultado final de la evaluación de la expresión posfija


# Ejemplo de uso
expresion_posfija = "3 4 + 5 *"
resultado = evaluar_expresion_posfija(expresion_posfija)
print("Resultado de la expresión posfija '{}': {}".format(expresion_posfija, resultado))


#%%bn
# # Validar operadores anidados:
# # 9. Verificar si los operadores en una expresión matemática están correctamente anidados utilizando una 
# # pila.

class Pila:     # Esta línea define una clase llamada Pila
    def __init__(self): #define un método que inicializa un objeto de la clase Nodo
        self.items = []  # Inicializamos una lista para almacenar los elementos de la pila

    def esta_vacia(self):
        return len(self.items) == 0  # Verificamos si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agregamos un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Eliminamos y devolvemos el elemento superior de la pila
        else:
            return None  # Devolvemos None si la pila está vacía

def validar_operadores_anidados(expresion):
    pila = Pila()  # Creamos una instancia de la clase Pila

    for caracter in expresion:
        if caracter in '({[':  # Si el caracter es un paréntesis de apertura
            pila.apilar(caracter)  # Lo apilamos en la pila
        elif caracter in ')}]':  # Si el caracter es un paréntesis de cierre
            if pila.esta_vacia():  # Si la pila está vacía, los paréntesis no están balanceados
                return False
            else:
                tope = pila.desapilar()  # Desapilamos el último paréntesis de apertura
                if (caracter == ')' and tope != '(') or \
                   (caracter == '}' and tope != '{') or \
                   (caracter == ']' and tope != '['):  # Si los paréntesis no coinciden
                    return False

    return pila.esta_vacia()  # Si la pila está vacía al final, los paréntesis están balanceados

# Ejemplo de uso
expresion = "{(2 + 3) * [5 - 2]}"  # Expresión con paréntesis correctamente anidados
if validar_operadores_anidados(expresion):
    print("Los paréntesis están correctamente anidados en la expresión:", expresion)
else:
    print("Los paréntesis NO están correctamente anidados en la expresión:", expresion)

    

#%% bn
# # Ordenar una pila:
# # 10. Ordenar los elementos de una pila de manera ascendente utilizando estructuras adicionales.

class Pila:     # Esta línea define una clase llamada Pila
    def __init__(self): #define un método que inicializa un objeto de la clase Nodo
        self.items = []  # Inicializamos una lista para almacenar los elementos de la pila

    def esta_vacia(self):
        return len(self.items) == 0  # Verificamos si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agregamos un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Eliminamos y devolvemos el elemento superior de la pila
        else:
            return None  # Devolvemos None si la pila está vacía

def ordenar_pila(pila):
    pila_aux = Pila()  # Creamos una pila auxiliar para almacenar temporalmente los elementos ordenados

    # Desapilamos cada elemento de la pila original y los ordenamos en la pila auxiliar
    while not pila.esta_vacia():
        elemento = pila.desapilar()  # Desapilamos un elemento de la pila original

        # Movemos los elementos mayores de la pila auxiliar a la pila original
        while not pila_aux.esta_vacia() and pila_aux.items[-1] > elemento:
            pila.apilar(pila_aux.desapilar())

        # Apilamos el elemento en la posición correcta en la pila auxiliar
        pila_aux.apilar(elemento)

    # Movemos los elementos ordenados de la pila auxiliar a la pila original
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())

# Ejemplo de uso
pila = Pila()  # Creamos una instancia de la clase Pila
pila.apilar(5)  # Apilamos algunos elementos desordenados
pila.apilar(3)
pila.apilar(8)
pila.apilar(1)

print("Pila original:", pila.items)  # Imprimimos la pila original

ordenar_pila(pila)  # Llamamos a la función para ordenar la pila

print("Pila ordenada:", pila.items)  # Imprimimos la pila ordenada

     
#%%
# # Eliminar duplicados:
# # 11. Eliminar los elementos duplicados de una pila.

    def __init__(self): #define un método que inicializa un objeto de la clase Nodo
        self.items = []  # Inicializamos una lista para almacenar los elementos de la pila
class Pila:     # Esta línea define una clase llamada Pila

    def esta_vacia(self):
        return len(self.items) == 0  # Verificamos si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agregamos un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Eliminamos y devolvemos el elemento superior de la pila
        else:
            return None  # Devolvemos None si la pila está vacía

def eliminar_duplicados_pila(pila):
    elementos_vistos = set()  # Creamos un conjunto para almacenar los elementos ya vistos
    pila_temporal = Pila()  # Creamos una pila temporal para almacenar los elementos únicos

    # Desapilamos los elementos de la pila original y los eliminamos si no están en el conjunto de elementos vistos
    while not pila.esta_vacia():
        elemento = pila.desapilar()  # Desapilamos un elemento de la pila original
        if elemento not in elementos_vistos:
            pila_temporal.apilar(elemento)  # Apilamos el elemento en la pila temporal
            elementos_vistos.add(elemento)  # Agregamos el elemento al conjunto de elementos vistos

    # Movemos los elementos únicos de la pila temporal a la pila original
    while not pila_temporal.esta_vacia():
        pila.apilar(pila_temporal.desapilar())  # Apilamos los elementos en la pila original

# Ejemplo de uso
pila = Pila()  # Creamos una instancia de la clase Pila
pila.apilar(3)  # Apilamos algunos elementos con duplicados
pila.apilar(5)
pila.apilar(3)
pila.apilar(2)
pila.apilar(5)

print("Pila original:", pila.items)  # Imprimimos la pila original

eliminar_duplicados_pila(pila)  # Llamamos a la función para eliminar duplicados

print("Pila sin duplicados:", pila.items)  # Imprimimos la pila sin duplicados

    


#%%
# # Implementar una calculadora sencilla:
# # 12. Crear una calculadora que pueda realizar operaciones básicas (+, -, *, /) utilizando una pila para evaluar 
# # expresiones.
class Pila:     # Esta línea define una clase llamada Pila
    def __init__(self):
        self.items = []  # Inicializamos una lista para almacenar los elementos de la pila

    def esta_vacia(self):
        return len(self.items) == 0  # Verificamos si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agregamos un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Eliminamos y devolvemos el elemento superior de la pila
        else:
            return None  # Devolvemos None si la pila está vacía

def calcular(expresion):
    pila = Pila()  # Creamos una instancia de la clase Pila para realizar los cálculos

    for caracter in expresion.split():  # Dividimos la expresión en tokens separados por espacios
        if caracter.isdigit():
            pila.apilar(int(caracter))  # Si el token es un número, lo apilamos en la pila
        elif caracter in ['+', '-', '*', '/']:
            operando2 = pila.desapilar()  # Desapilamos los dos últimos operandos de la pila
            operando1 = pila.desapilar()
            if operando1 is not None and operando2 is not None:
                if caracter == '+':
                    pila.apilar(operando1 + operando2)  # Realizamos la operación de suma
                elif caracter == '-':
                    pila.apilar(operando1 - operando2)  # Realizamos la operación de resta
                elif caracter == '*':
                    pila.apilar(operando1 * operando2)  # Realizamos la operación de multiplicación
                elif caracter == '/':
                    if operando2 != 0:
                        pila.apilar(operando1 / operando2)  # Realizamos la operación de división
                    else:
                        return "Error: División por cero"  # Manejamos el caso de división por cero
            else:
                return "Error: Expresión inválida"  # Manejamos el caso de una expresión mal formada

    return pila.desapilar()  # Devolvemos el resultado final de la evaluación de la expresión

# Ejemplo de uso
expresion = "5 3 + 2 *"  # Definimos una expresión en notación posfija
resultado = calcular(expresion)  # Calculamos el resultado de la expresión
print("Resultado:", resultado)  # Imprimimos el resultado


#%%
# # Comprobar palíndromos:
# # 13. Utilizar una pila para comprobar si una palabra o frase es un palíndromo.
# class Nodo:
    
class Pila:     # Esta línea define una clase llamada Pila
    def __init__(self):
        self.items = []  # Inicializamos una lista para almacenar los elementos de la pila

    def esta_vacia(self):
        return len(self.items) == 0  # Verificamos si la pila está vacía

    def apilar(self, item):
        self.items.append(item)  # Agregamos un elemento a la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Eliminamos y devolvemos el elemento superior de la pila
        else:
            return None  # Devolvemos None si la pila está vacía

def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertimos la palabra a minúsculas para ignorar mayúsculas
    palabra = ''.join(c for c in palabra if c.isalnum())  # Eliminamos caracteres no alfanuméricos

    pila = Pila()  # Creamos una instancia de la clase Pila para invertir la palabra

    # Apilamos cada carácter de la palabra en la pila
    for letra in palabra:
        pila.apilar(letra)

    # Construimos una nueva palabra desapilando los caracteres de la pila
    palabra_invertida = ''
    while not pila.esta_vacia():
        palabra_invertida += pila.desapilar()

    # Comparamos la palabra original con la palabra invertida para determinar si es un palíndromo
    return palabra == palabra_invertida

# Ejemplo de uso
palabra = "Anita lava la tina"
if es_palindromo(palabra):
    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')

    print(f"El texto '{texto}' no es un palíndromo.")
#%%
# # Simular el proceso de deshacer (undo):
# # 14. Implementar un sistema simple de "deshacer" utilizando dos pilas, una para las acciones y otra para los 
# # deshaceres

class DeshacerSistema: # Esta línea define una clase llamada DeshacerSistema
    def __init__(self):
        self.acciones_realizadas = []  # Pila para almacenar las acciones realizadas
        self.acciones_deshacer = []    # Pila para almacenar las acciones deshechas

    def hacer(self, accion):
        self.acciones_realizadas.append(accion)  # Agregamos la acción a la pila de acciones realizadas
        self.acciones_deshacer = []               # Limpiamos la pila de acciones deshechas

    def deshacer(self):
        if self.acciones_realizadas:  # Verificamos si hay acciones realizadas para deshacer
            accion_deshacer = self.acciones_realizadas.pop()  # Deshacemos la última acción realizada
            self.acciones_deshacer.append(accion_deshacer)    # Agregamos la acción deshecha a la pila de acciones deshechas

    def rehacer(self):
        if self.acciones_deshacer:  # Verificamos si hay acciones deshechas para rehacer
            accion_rehacer = self.acciones_deshacer.pop()  # Rehacemos la última acción deshecha
            self.acciones_realizadas.append(accion_rehacer)  # Agregamos la acción rehacer a la pila de acciones realizadas

# Creamos una instancia del sistema de deshacer
sistema_deshacer = DeshacerSistema()

# Simulamos algunas acciones
sistema_deshacer.hacer("Acción 1")
sistema_deshacer.hacer("Acción 2")

# Deshacemos la última acción
sistema_deshacer.deshacer()

# Rehacemos la última acción deshecha
sistema_deshacer.rehacer()

# Imprimimos las acciones realizadas y deshechas
print("Acciones realizadas:", sistema_deshacer.acciones_realizadas)
print("Acciones deshechas:", sistema_deshacer.acciones_deshacer)

print(f"Acción rehecha: {accion_rehecha}")


#%%
SEMANA 12 Y 13
#%%
"""Ejercicio parte 01 – Colas:
Verificar si una palabra es palíndroma
1. Implementa una función que determine si una palabra es palíndroma o no. Utiliza una cola para
comparar los caracteres de la palabra en orden original y reverso."""

from collections import deque  # Importa la clase deque del módulo collections

def es_palindromo(palabra):
    # Creamos una cola vacía
    cola = deque()

    # Convertimos la palabra en minúsculas para ignorar las diferencias de mayúsculas y minúsculas
    palabra = palabra.lower()

    # Agregamos cada carácter de la palabra a la cola
    for letra in palabra:
        cola.append(letra)

    # Creamos una variable para almacenar la palabra al revés
    palabra_al_reves = ''

    # Eliminamos los caracteres de la cola uno por uno y los concatenamos para obtener la palabra al revés
    while len(cola) > 0:
        palabra_al_reves += cola.pop()

    # Comparamos la palabra original con la palabra al revés
    if palabra == palabra_al_reves:
        return True
    else:
        return False

# Ejemplo de uso de la función
palabra = input("Introduce una palabra para verificar si es un palíndromo: ")

# Llamamos a la función es_palindromo y almacenamos el resultado
resultado = es_palindromo(palabra)

# Imprimimos un mensaje apropiado según el resultado
if resultado:
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")

#%%
"""Diseño de un sistema de gestión de pedidos
2. Crea un sistema de gestión de pedidos que utilice una cola para procesar los pedidos en el orden en que
fueron recibidos. Implementa funciones para agregar pedidos, procesar pedidos y mostrar el estado
actual de la cola."""


from collections import deque  # Importa la clase deque del módulo collections

class SistemaGestionPedidos:
    def __init__(self):
        self.cola_pedidos = deque()  # Inicializa una cola vacía para almacenar los pedidos

    def agregar_pedido(self, pedido):
        # Agrega un pedido a la cola
        self.cola_pedidos.append(pedido)
        print(f"Pedido agregado: {pedido}")

    def procesar_pedido(self):
        # Verifica si hay pedidos en la cola
        if self.cola_pedidos:
            # Procesa el pedido más antiguo (el primero en la cola)
            pedido_procesado = self.cola_pedidos.popleft()
            print(f"Pedido procesado: {pedido_procesado}")
        else:
            print("No hay pedidos para procesar")

    def mostrar_estado_cola(self):
        # Muestra el estado actual de la cola de pedidos
        print("Estado actual de la cola de pedidos:")
        for pedido in self.cola_pedidos:
            print(pedido)

# Crear una instancia del sistema de gestión de pedidos
sistema_pedidos = SistemaGestionPedidos()

# Ejemplo de uso del sistema
sistema_pedidos.agregar_pedido("Pedido 1")  # Agrega el pedido "Pedido 1"
sistema_pedidos.agregar_pedido("Pedido 2")  # Agrega el pedido "Pedido 2"
sistema_pedidos.agregar_pedido("Pedido 3")  # Agrega el pedido "Pedido 3"

sistema_pedidos.procesar_pedido()  # Procesa el primer pedido en la cola
sistema_pedidos.procesar_pedido()  # Procesa el segundo pedido en la cola

sistema_pedidos.mostrar_estado_cola()  # Muestra el estado actual de la cola

#%%
"""Búsqueda de rutas en un laberinto
3. Desarrolla un programa que encuentre el camino más corto a través de un laberinto. Utiliza una cola
para realizar un recorrido en anchura (BFS) desde el punto de inicio hasta el punto de destino."""

# Importa la clase deque del módulo collections
from collections import deque  

# Define la función para encontrar el camino más corto en el laberinto
def encontrar_camino_laberinto(laberinto, inicio, fin):
    # Definimos las direcciones posibles: arriba, abajo, izquierda, derecha
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Creamos una cola para el recorrido BFS
    cola = deque()
    cola.append(inicio)  # Agregamos el punto de inicio a la cola

    # Creamos un conjunto para llevar registro de los nodos visitados
    visitados = set()
    visitados.add(inicio)

    # Creamos un diccionario para almacenar los padres de cada nodo, para reconstruir el camino
    padres = {}
    padres[inicio] = None

    # Realizamos el recorrido BFS
    while cola:
        actual = cola.popleft()  # Sacamos el primer elemento de la cola

        # Verificamos si hemos llegado al punto de destino
        if actual == fin:
            break

        # Exploramos las direcciones posibles desde el nodo actual
        for direccion in direcciones:
            fila_nueva = actual[0] + direccion[0]
            columna_nueva = actual[1] + direccion[1]
            nueva_posicion = (fila_nueva, columna_nueva)

            # Verificamos si la nueva posición está dentro del laberinto y no ha sido visitada
            if 0 <= fila_nueva < len(laberinto) and 0 <= columna_nueva < len(laberinto[0]) and laberinto[fila_nueva][columna_nueva] != '#' and nueva_posicion not in visitados:
                cola.append(nueva_posicion)
                visitados.add(nueva_posicion)
                padres[nueva_posicion] = actual

    # Reconstruimos el camino más corto desde el punto de inicio hasta el punto de destino
    camino = []
    nodo_actual = fin
    while nodo_actual is not None:
        camino.append(nodo_actual)
        nodo_actual = padres[nodo_actual]
    camino.reverse()

    return camino

# Ejemplo de uso del programa
laberinto = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' '],
    ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

inicio = (1, 1)
fin = (7, 8)

# Encuentra el camino más corto en el laberinto
camino_mas_corto = encontrar_camino_laberinto(laberinto, inicio, fin)

# Imprime el camino más corto encontrado
print("Camino más corto:", camino_mas_corto)

#%%
"""Diseño de un sistema de gestión de tareas (Avanzado)
4. Implementa un sistema de gestión de tareas que permita agregar tareas, marcar tareas como
completadas y mostrar la próxima tarea pendiente."""


from collections import deque  # Importa la clase deque del módulo collections

class SistemaGestionTareas:
    def __init__(self):
        self.tareas = deque()  # Inicializa una cola para almacenar las tareas

    def agregar_tarea(self, tarea):
        # Agrega una tarea a la cola
        self.tareas.append(tarea)  # Agrega la tarea al final de la cola
        print(f"Tarea agregada: {tarea}")  # Imprime un mensaje indicando que se ha agregado la tarea

    def marcar_completada(self):
        # Marca la tarea más antigua como completada
        if self.tareas:  # Verifica si hay tareas en la cola
            tarea_completada = self.tareas.popleft()  # Elimina y devuelve la tarea más antigua de la cola
            print(f"Tarea completada: {tarea_completada}")  # Imprime un mensaje indicando que se ha completado la tarea
        else:
            print("No hay tareas pendientes")  # Imprime un mensaje si no hay tareas pendientes

    def mostrar_proxima_tarea_pendiente(self):
        # Muestra la próxima tarea pendiente
        if self.tareas:  # Verifica si hay tareas en la cola
            print(f"Próxima tarea pendiente: {self.tareas[0]}")  # Muestra la primera tarea en la cola
        else:
            print("No hay tareas pendientes")  # Imprime un mensaje si no hay tareas pendientes

# Crear una instancia del sistema de gestión de tareas
sistema_tareas = SistemaGestionTareas()

# Ejemplo de uso del sistema
sistema_tareas.agregar_tarea("Hacer la compra")  # Agrega la tarea "Hacer la compra"
sistema_tareas.agregar_tarea("Enviar correo electrónico")  # Agrega la tarea "Enviar correo electrónico"
sistema_tareas.agregar_tarea("Preparar presentación")  # Agrega la tarea "Preparar presentación"

sistema_tareas.mostrar_proxima_tarea_pendiente()  # Muestra la próxima tarea pendiente

sistema_tareas.marcar_completada()  # Marca la próxima tarea como completada

sistema_tareas.mostrar_proxima_tarea_pendiente()  # Muestra la próxima tarea pendiente después de marcarla como completada

#%%

"""Ejercicios parte 02 - Arboles:
Contar nodos:
5. Implementar una función que cuente la cantidad de nodos en el árbol."""

class Nodo:# Esta línea define una clase llamada Nodo
    def __init__(self, valor): #define un método que inicializa un objeto de la clase Nodo con un
                                #valor específico cuando se crea una nueva instancia de la clase.
        self.valor = valor  # Inicializa el valor del nodo
        self.hijos = []     # Inicializa una lista para almacenar los hijos del nodo

def contar_nodos(raiz):
    if raiz is None:
        return 0  # Si la raíz es None, el árbol está vacío y no tiene nodos, devuelve 0

    contador = 1  # Inicializa el contador con 1 para contar el nodo actual

    for hijo in raiz.hijos:
        contador += contar_nodos(hijo)  # Recursivamente cuenta los nodos de cada hijo y los suma al contador

    return contador

# Ejemplo de uso del código
raiz = Nodo(1)  # Se crea un nodo raíz con el valor 1
raiz.hijos.append(Nodo(2))  # Se añade un hijo al nodo raíz con el valor 2
raiz.hijos.append(Nodo(3))  # Se añade otro hijo al nodo raíz con el valor 3
raiz.hijos.append(Nodo(4))  # Se añade otro hijo al nodo raíz con el valor 4

raiz.hijos[0].hijos.append(Nodo(5))  # Se añade un hijo al primer hijo del nodo raíz con el valor 5
raiz.hijos[0].hijos.append(Nodo(6))  # Se añade otro hijo al primer hijo del nodo raíz con el valor 6
raiz.hijos[1].hijos.append(Nodo(7))  # Se añade un hijo al segundo hijo del nodo raíz con el valor 7
raiz.hijos[1].hijos.append(Nodo(8))  # Se añade otro hijo al segundo hijo del nodo raíz con el valor 8

print("Cantidad de nodos:", contar_nodos(raiz))  # Se llama a la función contar_nodos con la raíz del árbol y se imprime la cantidad de nodos


#%%

"""6. Implementar una función que cuente la cantidad de nodos hoja (que no tienen hijos)."""

class Nodo:  # Esta línea define una clase llamada Nodo
    def __init__(self, valor): #define un método que inicializa un objeto de la clase Nodo
        self.valor = valor  # Inicializa el valor del nodo
        self.hijos = []     # Inicializa una lista para almacenar los hijos del nodo

def contar_nodos_hoja(raiz):
    if raiz is None:
        return 0  # Si la raíz es None, el árbol está vacío y no tiene nodos hoja, devuelve 0

    if not raiz.hijos:
        return 1  # Si la raíz no tiene hijos, es un nodo hoja, devuelve 1

    nodos_hoja = 0  # Inicializa un contador para los nodos hoja
    for hijo in raiz.hijos:
        nodos_hoja += contar_nodos_hoja(hijo)  # Recursivamente cuenta los nodos hoja de cada hijo y los suma al contador

    return nodos_hoja  # Devuelve el total de nodos hoja encontrados en el árbol

# Ejemplo de uso del código
raiz = Nodo(1)  # Se crea un nodo raíz con el valor 1
raiz.hijos.append(Nodo(2))  # Se añade un hijo al nodo raíz con el valor 2
raiz.hijos.append(Nodo(3))  # Se añade otro hijo al nodo raíz con el valor 3
raiz.hijos.append(Nodo(4))  # Se añade otro hijo al nodo raíz con el valor 4
raiz.hijos[0].hijos.append(Nodo(5))  # Se añade un hijo al primer hijo del nodo raíz con el valor 5
raiz.hijos[0].hijos.append(Nodo(6))  # Se añade otro hijo al primer hijo del nodo raíz con el valor 6
raiz.hijos[1].hijos.append(Nodo(7))  # Se añade un hijo al segundo hijo del nodo raíz con el valor 7
raiz.hijos[1].hijos.append(Nodo(8))  # Se añade otro hijo al segundo hijo del nodo raíz con el valor 8


print("Cantidad de nodos hoja:", contar_nodos_hoja(raiz))  # Llama a la función y muestra la cantidad de nodos hoja

#%%
"""7. Implementar una función que cuente la cantidad de nodos internos (que tienen al menos un hijo)."""

class Nodo:         # Esta línea define una clase llamada Nodo
    def __init__(self, valor):  #define un método que inicializa un objeto de la clase Nodo
        self.valor = valor  # Inicializa el valor del nodo
        self.hijos = []     # Inicializa una lista para almacenar los hijos del nodo

def contar_nodos_internos(raiz):
    if raiz is None:
        return 0  # Si la raíz es None, el árbol está vacío y no tiene nodos internos, devuelve 0

    if not raiz.hijos:
        return 0  # Si la raíz no tiene hijos, no es un nodo interno, devuelve 0

    nodos_internos = 1  # Inicializa el contador con 1 para contar el nodo actual (si tiene al menos un hijo)

    for hijo in raiz.hijos:
        nodos_internos += contar_nodos_internos(hijo)  # Recursivamente cuenta los nodos internos de cada hijo y los suma al contador

    return nodos_internos

# Ejemplo de uso del código
raiz = Nodo(1)  # Se crea un nodo raíz con el valor 1
raiz.hijos.append(Nodo(2))  # Se añade un hijo al nodo raíz con el valor 2
raiz.hijos.append(Nodo(3))  # Se añade otro hijo al nodo raíz con el valor 3
raiz.hijos.append(Nodo(4))  # Se añade otro hijo al nodo raíz con el valor 4
raiz.hijos[0].hijos.append(Nodo(5))  # Se añade un hijo al primer hijo del nodo raíz con el valor 5
raiz.hijos[0].hijos.append(Nodo(6))  # Se añade otro hijo al primer hijo del nodo raíz con el valor 6
raiz.hijos[1].hijos.append(Nodo(7))  # Se añade un hijo al segundo hijo del nodo raíz con el valor 7
raiz.hijos[1].hijos.append(Nodo(8))  # Se añade otro hijo al segundo hijo del nodo raíz con el valor 8

print("Cantidad de nodos internos:", contar_nodos_internos(raiz))  # Se llama a la función contar_nodos_internos con la raíz del árbol y se imprime la cantidad de nodos internos


#%%

"""Calcular altura y profundidad:
8. Implementar una función que calcule la altura del árbol (la longitud del camino más largo desde la raíz
hasta una hoja)."""

class Nodo:     # Esta línea define una clase llamada Nodo
    def __init__(self, valor):       #define un método que inicializa un objeto de la clase Nodo
        self.valor = valor  # Inicializa el valor del nodo
        self.hijos = []     # Inicializa una lista para almacenar los hijos del nodo

def calcular_altura(raiz):
    if raiz is None:
        return 0  # Si la raíz es None, el árbol está vacío y su altura es 0

    if not raiz.hijos:
        return 1  # Si la raíz no tiene hijos, su altura es 1

    alturas_hijos = []  # Lista para almacenar las alturas de los hijos
    for hijo in raiz.hijos:
        alturas_hijos.append(calcular_altura(hijo))  # Calcula la altura de cada hijo

    return max(alturas_hijos) + 1  # La altura de la raíz es la máxima altura de los hijos más 1

# Ejemplo de uso del código
raiz = Nodo(1)  # Se crea un nodo raíz con el valor 1
raiz.hijos.append(Nodo(2))  # Se añade un hijo al nodo raíz con el valor 2
raiz.hijos.append(Nodo(3))  # Se añade otro hijo al nodo raíz con el valor 3
raiz.hijos[0].hijos.append(Nodo(4))  # Se añade un hijo al primer hijo del nodo raíz con el valor 4
raiz.hijos[0].hijos.append(Nodo(5))  # Se añade otro hijo al primer hijo del nodo raíz con el valor 5
raiz.hijos[1].hijos.append(Nodo(6))  # Se añade un hijo al segundo hijo del nodo raíz con el valor 6
raiz.hijos[1].hijos.append(Nodo(7))  # Se añade otro hijo al segundo hijo del nodo raíz con el valor 7
raiz.hijos[1].hijos[1].hijos.append(Nodo(8))  # Se añade un hijo al segundo hijo del segundo hijo del nodo raíz con el valor 8

print("Altura del árbol:", calcular_altura(raiz))  # Se llama a la función calcular_altura con la raíz del árbol y se imprime la altura del árbol


#%%
"""9. Implementar una función que calcule la profundidad de un nodo (la longitud del camino desde la raíz
hasta el nodo).
"""
class Nodo:     # Esta línea define una clase llamada Nodo
    def __init__(self, valor):       #define un método que inicializa un objeto de la clase Nodo
        self.valor = valor  # Inicializa el valor del nodo
        self.hijos = []     # Inicializa una lista para almacenar los hijos del nodo

def calcular_profundidad(raiz, valor_busqueda, profundidad_actual=0):
    if raiz is None:
        return -1  # Si la raíz es None, el árbol está vacío y no se encontró el nodo, se devuelve -1

    if raiz.valor == valor_busqueda:
        return profundidad_actual  # Si se encuentra el nodo, se devuelve la profundidad actual

    for hijo in raiz.hijos:
        profundidad = calcular_profundidad(hijo, valor_busqueda, profundidad_actual + 1)  # Se busca en los hijos recursivamente
        if profundidad != -1:  # Si se encontró el nodo en el subárbol, se devuelve la profundidad
            return profundidad

    return -1  # Si no se encuentra el nodo en el subárbol, se devuelve -1

# Ejemplo de uso del código
raiz = Nodo(1)  # Se crea un nodo raíz con el valor 1
raiz.hijos.append(Nodo(2))  # Se añade un hijo al nodo raíz con el valor 2
raiz.hijos.append(Nodo(3))  # Se añade otro hijo al nodo raíz con el valor 3
raiz.hijos[0].hijos.append(Nodo(4))  # Se añade un hijo al primer hijo del nodo raíz con el valor 4
raiz.hijos[0].hijos.append(Nodo(5))  # Se añade otro hijo al primer hijo del nodo raíz con el valor 5
raiz.hijos[1].hijos.append(Nodo(6))  # Se añade un hijo al segundo hijo del nodo raíz con el valor 6
raiz.hijos[1].hijos.append(Nodo(7))  # Se añade otro hijo al segundo hijo del nodo raíz con el valor 7
raiz.hijos[1].hijos[1].hijos.append(Nodo(8))  # Se añade un hijo al segundo hijo del segundo hijo del nodo raíz con el valor 8

valor_busqueda = 8  # El valor que se busca en el árbol es 8
profundidad = calcular_profundidad(raiz, valor_busqueda)  # Se calcula la profundidad del nodo con el valor 8

if profundidad != -1:  # Si la profundidad es diferente de -1, significa que se encontró el nodo
    print(f"Profundidad del nodo {valor_busqueda}: {profundidad}")  # Se imprime la profundidad del nodo
else:  # Si la profundidad es -1, significa que no se encontró el nodo en el árbol
    print(f"No se encontró el nodo {valor_busqueda} en el árbol.")  # Se imprime un mensaje indicando que el nodo no se encontró en el árbol


#%%
"""Buscar el mínimo y el máximo:
10. Implementar una función que encuentre el nodo con el valor mínimo en el árbol"""

class Nodo:     # Esta línea define una clase llamada Nodo
    def __init__(self, valor):  #define un método que inicializa un objeto de la clase Nodo
        self.valor = valor  # Inicializa el valor del nodo
        self.hijos = []     # Inicializa una lista para almacenar los hijos del nodo

def encontrar_minimo(raiz):
    if raiz is None:
        return float('inf')  # Si la raíz es None, el árbol está vacío y no hay valor mínimo, devuelve infinito

    min_valor = raiz.valor  # Inicializa el mínimo con el valor de la raíz

    for hijo in raiz.hijos:
        min_hijo = encontrar_minimo(hijo)  # Se busca el valor mínimo en cada subárbol
        min_valor = min(min_valor, min_hijo)  # Se actualiza el valor mínimo si se encuentra uno menor en los subárboles

    return min_valor
# Ejemplo de uso del código
raiz = Nodo(10)  # Se crea un nodo raíz con el valor 10
raiz.hijos.append(Nodo(5))  # Se añade un hijo al nodo raíz con el valor 5
raiz.hijos.append(Nodo(8))  # Se añade otro hijo al nodo raíz con el valor 8
raiz.hijos[0].hijos.append(Nodo(3))  # Se añade un hijo al primer hijo del nodo raíz con el valor 3
raiz.hijos[0].hijos.append(Nodo(7))  # Se añade otro hijo al primer hijo del nodo raíz con el valor 7
raiz.hijos[1].hijos.append(Nodo(12)) # Se añade un hijo al segundo hijo del nodo raíz con el valor 12
raiz.hijos[1].hijos.append(Nodo(20)) # Se añade otro hijo al segundo hijo del nodo raíz con el valor 20

minimo = encontrar_minimo(raiz)  # Se llama a la función encontrar_minimo con la raíz del árbol y se guarda el valor mínimo encontrado en la variable minimo
print("El valor mínimo en el árbol es:", minimo)  # Se imprime el valor mínimo encontrado en el árbol


#%%
"""11. Implementar una función que encuentre el nodo con el valor máximo en el árbol"""

class Nodo:     # Esta línea define una clase llamada Nodo
    def __init__(self, valor):  #define un método que inicializa un objeto de la clase Nodo
        self.valor = valor  # Inicializa el valor del nodo
        self.hijos = []     # Inicializa una lista para almacenar los hijos del nodo

def encontrar_maximo(raiz):
    if raiz is None:
        return float('-inf')  # Si la raíz es None, el árbol está vacío y no hay valor máximo, devuelve menos infinito

    max_valor = raiz.valor  # Inicializa el máximo con el valor de la raíz

    for hijo in raiz.hijos:
        max_hijo = encontrar_maximo(hijo)  # Se busca el valor máximo en cada subárbol
        max_valor = max(max_valor, max_hijo)  # Se actualiza el valor máximo si se encuentra uno mayor en los subárboles

    return max_valor

# Ejemplo de uso del código
raiz = Nodo(10)  # Se crea un nodo raíz con el valor 10
raiz.hijos.append(Nodo(5))  # Se añade un hijo al nodo raíz con el valor 5
raiz.hijos.append(Nodo(8))  # Se añade otro hijo al nodo raíz con el valor 8
raiz.hijos[0].hijos.append(Nodo(3))  # Se añade un hijo al primer hijo del nodo raíz con el valor 3
raiz.hijos[0].hijos.append(Nodo(7))  # Se añade otro hijo al primer hijo del nodo raíz con el valor 7
raiz.hijos[1].hijos.append(Nodo(12)) # Se añade un hijo al segundo hijo del nodo raíz con el valor 12
raiz.hijos[1].hijos.append(Nodo(20)) # Se añade otro hijo al segundo hijo del nodo raíz con el valor 20

maximo = encontrar_maximo(raiz)  # Se llama a la función encontrar_maximo con la raíz del árbol y se guarda el valor máximo encontrado en la variable maximo
print("El valor máximo en el árbol es:", maximo)  # Se imprime el valor máximo encontrado en el árbol



#%%
#%%
#%%
#%%
#%%
#%%