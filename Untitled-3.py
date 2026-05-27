 = input("Ingrese 4 números separados por comas: ")
partes = [p.strip() for p in entrada.split(",")]
numeros_tupla = tuple(float(p) for p in partes)
promedio = sum(numeros_tupla) / len(numeros_tupla)
maximo = max(numeros_tupla)
minimo = min(numeros_tupla)
print("Tupla:", numeros_tupla)
print("Promedio:", promedio)
print("Máximo:", maximo)
print("Mínimo:", minimo)

# 4. Pide nombre, edad y curso y guarda en diccionario
nombre = input("Ingrese su nombre: ").strip()
edad = int(input("Ingrese su edad: "))
curso = input("Ingrese su curso: ").strip()
alumno = {"nombre": nombre, "edad": edad, "curso": curso}
print("Diccionario alumno:", alumno)

# 5. Crea lista de 10 enteros y realiza operaciones
lista_enteros = [12, 34, 56, 78, 90, 3, 45, 67, 89, 23]

# 5.1 Imprime todos uno por uno
for n in lista_enteros:
    print(n)

# 5.2 Imprime solo los mayores que 50
for n in lista_enteros:
    if n > 50:
        print(n)

# 5.3 Añade dos decimales con append y extend
lista_enteros.append(1.5)
lista_enteros.extend([2.75])

# 5.4 Inserta 100.5 en la posición 3
lista_enteros.insert(3, 100.5)

# 5.5 Elimina el primer número por valor y el último por índice
primer_valor = lista_enteros[0]
lista_enteros.remove(primer_valor)
lista_enteros.pop(-1)

# 5.6 Muestra lista final y cantidad de elementos
print("Lista final:", lista_enteros)
print("Cantidad de elementos:", len(lista_enteros))

# 6. Lista de 5 números decimales ingresados por el usuario
decimales = []
for i in range(5):
    decimales.append(float(input(f"Ingrese el decimal {i+1}: ")))

prom_dec = sum(decimales) / len(decimales)
mayor_dec = max(decimales)
menor_dec = min(decimales)
ordenada = sorted(decimales)

print("Decimales:", decimales)
print("Promedio:", prom_dec)
print("Mayor:", mayor_dec)
print("Menor:", menor_dec)
print("Ordenada (sorted):", ordenada)

# 7. Declara una tupla con 6 enteros y convierte/agrega/reconvierte
tupla_seis = (1, 2, 3, 4, 5, 6)
lista_temp = list(tupla_seis)
lista_temp.append(7.5)
tupla_final = tuple(lista_temp)
print("Tupla final:", tupla_final)