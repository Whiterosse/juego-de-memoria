
'''
#sentencia match

numero = 5


match numero:
    case 1:
        print("Es igual a 1")
    case 2:
        print("igual a 333")
    case 3:
        print("Igual a 4")
    case _:
        print("no es igual a ninguno")
        

numero = int(input("Ingresa un numero: "))

match numero:
    case 0:
        print("El numero es cero")
    case numero if numero % 2 == 0:
        print("El Numero es par")
    case numero if numero % 2 != 0:
        print("Es un numero ImPar")
    case _:
        print("Ingresa un numero valido")

        
#ejercicio

numero = int(input("Ingresa un numero entero: "))

match numero:
    case numero if numero < 0:
        print("El numero se encuentra en rango: negativos (menores que 0)")
    case numero if numero <= 10:
        print("El numero se encuentra entre 0 y 10")
    case numero if numero > 10:
        print("El numero se encuentra en un rango mayor a 10")
        
'''

#REPASO DE CASOS CASE

#preguntar si el numero ingresado es par o impar con case

'''
numero = int(input("Ingresar un numero natural: "))
match numero:
    case 0:
        print("El numero es cero. ")
    case numero if numero % 2 == 0:
        print("El numero ingresado es par. ")
    case numero if numero % 2 != 0:
        print("El numero ingresado NO es par. ")
    case _:
        print("Numero no Natural o no valido")
        
'''

#Escribe un programa Python que solicite al usuario ingresar un número entero y luego determine
# se encuentra ese número utilizando la declaración match. El programa debe imprimir un mensaje que indique 
# el rango al que pertenece el número.

'''
dato = int(input("ingresa un numero a evaluar: "))

match dato:
    case dato if dato > 0 and dato < 101:
        print("El numero se encuentra entre 1 y 100")
    case dato if dato > 100:
        print("El numero es superior a 100 ")
    case dato if dato < 0:
        print("El numero es inferior a 0 ")
    case _:
        print("ingresa un valor correcto. ")
        
'''

# bucle for para iterar sobre una lista

'''
lista = ["comida","cena","launch","Desayuno"]

contador = 0

for alimento in lista:
    contador += 1
    print(f"{contador} {alimento}")
'''
    
#ELEVAR NUMEROS AL CUADRADO DESDE UNA LISTA
'''
numeros = [1,2,3,4,5,6,7,8,9]

for numero in numeros:
    cuadrado = numero ** 2
    print(f"tengo el numero {numero} y su cuadrado es: {cuadrado}")
'''
#EJERCICIO FOR BUCLE

'''
Ejercicio: Calcular el promedio de una lista de números


Descripción: Escribe un programa en Python que calcule el promedio de una lista de números. Debes seguir estos pasos:


        Crea una lista llamada numeros que contenga al menos cinco números enteros.

        Inicializa una variable llamada suma en 0.

        Utiliza un ciclo for para iterar a través de la lista numeros y suma cada número a la variable suma.

        Después del ciclo for, divide la variable suma entre la cantidad de números en la lista (que puedes obtener usando la función len(numeros)).

        Imprime el resultado como el promedio de los números en la lista.


Este ejercicio te ayudará a practicar la utilización de ciclos for, variables y operaciones matemáticas básicas en Python. ¡Buena suerte!
Preguntas de esta tarea

Ejercicio: Calcular el promedio de una lista de números


Descripción: Escribe un programa en Python que calcule el promedio de una lista de números. Debes seguir estos pasos:


    Crea una lista llamada numeros que contenga al menos cinco números enteros.

    Inicializa una variable llamada suma en 0.

    Utiliza un ciclo for para iterar a través de la lista numeros y suma cada número a la variable suma.

    Después del ciclo for, divide la variable suma entre la cantidad de números en la lista (que puedes obtener usando la función len(numeros)).

    Imprime el resultado como el promedio de los números en la lista.


Este ejercicio te ayudará a practicar la utilización de ciclos for, variables y operaciones matemáticas básicas en Python. ¡Buena suerte!
'''
'''
numeros = [10,20,30,40,50]

suma = 0

for numero in numeros:
    suma += numero
    promedio = suma / len(numeros)
    print("el promedio de los numeros es igual a ", promedio)
    '''

#cicle while

# realizar contador hasta el 10 desde el numero 1
'''
contar = 0

while contar < 10:
    contar += 1
    print(contar)
    '''

#realizar conteo regresivo desde 12 meses hasta llegar a cero
'''
contar = 12

while contar:
    contar -= 1
    print(f"estamos en el mes {contar}")
    if contar == 0:
        print(f"Ya estamos en el ultimo mes {contar}")
        break
'''
#ingresar numeros desde el user y sacar si es negativo / sumarlos  

#a continuacion queda trabajo / realizar      
'''
suma = 0

dato = int(input("Ingresa un numero positivo para SUMAR y negativo para FINALIZAR: "))

while dato > 0:
    suma += dato
    dato = int(input("Ingresa un numero positivo para SUMAR y negativo para FINALIZAR: "))

print("Ingresaste numero negativo y la suma es: ", suma)
'''

'''
Tarea: Conteo Personalizado con Bucle While


Descripción:


En esta tarea, se te pide crear un programa en Python que cuente desde 1 hasta un número límite ingresado por el usuario. El programa debe utilizar un bucle while para llevar a cabo el conteo y mostrar los números en orden ascendente. Una vez que se alcance el número límite, el programa debe imprimir "Conteo completado".


Instrucciones:


        Solicita al usuario que ingrese un número entero positivo como límite para el conteo.

        Inicializa una variable llamada contador en 1.

        Utiliza un bucle while para realizar el conteo desde 1 hasta el número límite ingresado por el usuario.

        En cada iteración del bucle, muestra el valor actual de contador en la pantalla.

        Después de imprimir el número actual, incrementa el valor de contador en 1 para pasar al siguiente número.

        Cuando el valor de contador alcance o supere el número límite ingresado por el usuario, el bucle while debe detenerse.

        Imprime "Conteo completado" para indicar que el conteo ha terminado.

Preguntas de esta tarea

Tarea: Conteo Personalizado con Bucle While


Descripción:


En esta tarea, se te pide crear un programa en Python que cuente desde 1 hasta un número límite ingresado por el usuario. El programa debe utilizar un bucle while para llevar a cabo el conteo y mostrar los números en orden ascendente. Una vez que se alcance el número límite, el programa debe imprimir "Conteo completado".


Instrucciones:


    Solicita al usuario que ingrese un número entero positivo como límite para el conteo.

    Inicializa una variable llamada contador en 1.

    Utiliza un bucle while para realizar el conteo desde 1 hasta el número límite ingresado por el usuario.

    En cada iteración del bucle, muestra el valor actual de contador en la pantalla.

    Después de imprimir el número actual, incrementa el valor de contador en 1 para pasar al siguiente número.

    Cuando el valor de contador alcance o supere el número límite ingresado por el usuario, el bucle while debe detenerse.

    Imprime "Conteo completado" para indicar que el conteo ha terminado.
'''
'''

limite = int(input("Numero limite a contar "))
contar = 1
while contar <= limite:
    print(" el conteo va = " , contar)
    contar += 1
    if contar == limite:
            break
print("conteo completado")
'''
# cadenas

'''
nombre = "camilo"
apellido = "rincon"
frase = "hola, esto es una frase "

longitud = len(nombre)
print(longitud)

print(apellido[0])
mayus = apellido.upper()
print(mayus)
'''

#tuplas

'''
personas = (("juan", 33), ("johana", 29),("Emiliano",3))

#la idea es conocer la edad de la persona, si es mayor o menor

for nombre, edad in personas:
    if edad < 18:
        print(nombre, edad)
'''
'''
tupla = (("manzana", "banana" , "cereza"))
palabra_buscar = input("ingresa la palabra: ")


for letra in tupla:
    if letra == palabra_buscar:
        print("la palabra está en tupla")
    else:
        print("la palabra no está en tupla")
'''

#lista de colores

#Escribe un programa en Python que cree una lista de colores y luego muestre cada color en una línea separada.
'''

lista = "rojo", "azul", "verde", "naranja"

for color in lista:
    print(color)
'''

#DICCIONARIO

#diccionario anidado =
'''
personas = {
    "persona1":{
        "nombre" : "juan",
        "edad" : "33 años",
        "genero" : "masculino"
    },
    
    "persona2" : {
        "nombre" : "johana",
        "edad" : "30 años",
        "genero" : "femenino" 
    }
}

dato = personas["persona1"]
print(dato["nombre"])
'''

#diccionario no anidado, normal

'''
persona = {
    "nombre" : None,
    "apellido" : None,
    "edad" : None,
    "genero" : None
}

persona["nombre"] = input("Ingresa tu nombre: ")
persona["apellido"] = input("Ingresa tu apellido: ")
persona["edad"] = input("ingresa tu edad: ")
persona["genero"] = input("Cual es tu genero? ")

print("tu nombre es ", persona["nombre"] , persona["apellido"] , "tienes " , persona["edad"] , "y te identificas como " , persona["genero"])
'''

#tarea
#Escribe un programa en Python que permita al usuario ingresar su nombre, edad, dirección y número de teléfono, y luego muestre estos datos en pantalla.
'''
datos_personales = {
    "nombre" : None,
    "edad" : None,
    "direccion" : None,
    "telefono" : None
}

datos_personales["nombre"] = input("ingresa tu nombre ")
datos_personales["edad"] = input("ingresar la edad (solo el numero) ")
datos_personales["direccion"] = input("tu direccion es: ")
datos_personales["telefono"] = input("numero telefonico ")

print("tu nombre es" , datos_personales["nombre"] , "tienes" , datos_personales["edad"], "años", "vives en la direccion " 
,datos_personales["direccion"] , "y tu numero telefonico es " , datos_personales["telefono"])
'''

#funciones

#realizar funcion para saludar
'''
def saludar(nombre):
    print(f"hola, {nombre}")
    
saludar("Camilo")
'''

#realizar funcion suma para sumar 2 numeros dados por el user
'''
def suma(a,b):
    mate = a+b
    return mate

a = int(input("ingresa el dato 1: "))
b = int(input("ingresa el dato 2: "))

mate = suma(a,b)
print(mate)
'''
#funcion para determinar si un numero es PAR o IMPAR

#def numero(dato):
#    if dato % 2 == 0:
#        return True
#    else:
#        return False
#        
#    
#
#dato = int(input("ingresa un numero: "))
#if numero(dato) == True:
#    print(f"{dato}, es PAR ")
#else:
#    print(f"{dato}, es IMPAR ")



#numero = int(input("ingresa un numero "))
#
#if numero % 2 == 0:
#    print("es par ")
#else:
#    print("Impar")
#    

#Realizar una funcion que indique Cual es el mayor numero almacenado en lista de numero
'''
def listanumero1(numero):
    mayor = max(numero)
    return mayor

def listanumero2(numero):
    menor = min(numero)
    return menor

numeros = [1,2,5,7,65,50,101]
numeroMayor = listanumero1(numeros)
print(numeroMayor)

numeros = [1,2,5,7,65,50,101]
numeroMenor = listanumero2(numeros)
print(numeroMenor)

'''

#Escribe un programa en Python que realice operaciones matemáticas simples 
#(suma, resta, multiplicación y división) utilizando una función.
#El programa debe permitir al usuario ingresar dos números y seleccionar una operación para realizar.