1

num1 = float(input("ingresa el primer numero: "))
num2 = float(input("ingresa el segundo numero: "))
if num1 > num2:
    print(f"el numero mayor es: {num1}")
elif num2 > num1:
    print(f"el numero mayor es: {num2}")
else:
    print("ambos numeros son iguales.")
2

nota = float(input("ingresa la nota del estudiante (0 a 5):"))
if nota < 0 or nota > 5:
     print(" La nota no es válida, debe estar entre 0 y 5.")
else:
    
    if nota >= 3:
        print("Aprobado")
    else:
        print("Reprobó")
3


numero = int(input("ingrese un numero: "))
print(f"tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
4



palabra = input("Ingresa una palabra: ")
vocales = "aeiouAEIOU"
contador = 0
for letra in palabra:
     if letra in vocales:
        contador += 1
print(f"La palabra '{palabra}' tiene {contador} vocal(es).")