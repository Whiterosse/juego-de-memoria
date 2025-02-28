tempe = int(input("Ingresa la tempertura a convertir: "))
grado = input("es farenheit(f) o celsius(c)?: ")

if grado == "c":
    print((tempe * 1.8)+32, "celsius+++")
elif grado == "f":
    print((tempe - 32)*0.555, "farenheit+++")
else:
    print("ingresa un valor correcto")

