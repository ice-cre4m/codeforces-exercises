"""
Codeforces 2231A - A. Construct an Array

Debemos contruir un array en cada test case donde cumpla las dos condiciones: 
1. El array no puede tener un elemento en un indice x donde ese elemento sea igual o superior al largo del array multiplicado por 2.
2. El array y las sumas de dos elementos del array no pueden tener elementos repetidos.
"""

def main():
    #t = int(input())
    t = 1
    for _ in range(t):
        n = int(input())
        lista = []
        for i in range(n*2):
            lista.append(i)
        print(lista)
        print(crear_array_sumas(lista))

def crear_array_sumas(array):
    sumas = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            sumas.append(array[i] + array[j])
    return sumas



if __name__ == "__main__":
    main()