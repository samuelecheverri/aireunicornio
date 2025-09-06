frutas = {"manzana", "banana", "naranja"}
print(frutas)

#  Agregar un nuevo elemento
frutas.add("pera")
print(frutas)

#  Intentar agregar un duplicado
frutas.add("banana")
print(frutas)  # No se repite

#  Comprobar si un elemento está presente
print("¿Hay mango?", "mango" in frutas)

#  Recorrer el set con un bucle
for fruta in frutas:
    print(fruta)

#  Eliminar un elemento existente
frutas.remove("pera")
print(frutas)

#  Eliminar un elemento sin error si no existe
frutas.discard("uva")  # No lanza error
print(frutas)

#  Eliminar un elemento aleatorio
elemento = frutas.pop()
print(f"Se eliminó: {elemento}")
print(frutas)

#  Vaciar el conjunto
frutas.clear()
print(frutas)

#  Crear un conjunto desde una lista (eliminando duplicados)
numeros = [1, 2, 2, 3, 3, 4]
conjunto = set(numeros)
print(conjunto)

#  Unión de dos conjuntos
a = {1, 2, 3}
b = {3, 4, 5}
print("Unión:", a | b)

#  Intersección
print("Intersección:", a & b)

#  Diferencia (elementos de a que no están en b)
print("Diferencia:", a - b)

# 14. Diferencia simétrica (elementos no comunes)
print("Diferencia simétrica:", a ^ b)

#  Verificar si dos sets son disjuntos
print("¿Disjuntos?", a.isdisjoint({7, 8}))

#  Verificar si un set es subconjunto de otro
print("¿a es subconjunto de b?", a.issubset({1, 2, 3, 4}))

#  Verificar si un set es superconjunto de otro
print("¿a es superconjunto de {1, 2}?", a.issuperset({1, 2}))

#  Copiar un set
copia = a.copy()
print("Copia:", copia)

#  Convertir set a lista
lista = list(a)
print("Como lista:", lista)

#  Crear un set a partir de una cadena (caracteres únicos)
letras = set("programar")
print("Letras únicas:", letras)