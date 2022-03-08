
def func(lista):
    suma = lista[0]
    diff = suma
    prod = suma
    for x in lista[1:]:
        suma += x
        diff -= x
        prod *= x

    return suma, diff, prod

lista = [1, 2, 3, 4]

print(func(lista))
