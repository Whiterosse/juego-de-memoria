# SENTENCIAS IF, ELIF, ELSE

x = int(input("ingresa un numero "))

if x < 15:
    print("El numero ingresado es menor que 15")
elif x <= 15:
    print("El numero ingresado es igual a 15")
else:
    print("El numero ingresado es mayor a 15... ")
    
 

 
#ejercicio

notas = float(input("ingresa la nota del estudiante: "))

if notas >= 90:
    print("¡Felicidades! Has aprobado con una calificación sobresaliente.")
elif notas >= 70:
    print("Has aprobado satisfactoriamente.")
elif notas >= 60:
    print("Has aprobado, pero necesitas mejorar un poco.")
else:
    print("Lo siento, has suspendido. Debes esforzarte más en la próxima evaluación.")