'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def solver(lista, k):
    tabla = set()
    for numero in lista:
        if numero > k:
            continue
        else:
            if numero in tabla:
                print('{}+{}'.format(numero, k-numero))
                return True
            tabla.add(k-numero)
    return False


lista = [1,4,6,12,21,65,7,0,14,2]

print(solver(lista, 29))