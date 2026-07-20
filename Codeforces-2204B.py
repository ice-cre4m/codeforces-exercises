def mayor(lista):
    Max = 0
    for number in lista:
        if number > Max:
            Max = number
    return Max

def busqueda_inv(valor,lista):
    for i in range(0,len(lista)):
        if lista[-i] == valor:
            return (len(lista) - 1) -  i
    return -1

def main():
    test_cases = int(input())
    for i in range (0,test_cases):
        n = int(input())
        integers = list(map(int, input().split()))
        operaciones = 0
        while integers:
            
            del integers[(len(integers) - busqueda_inv(mayor(integers), integers)):len(integers)]
            print(integers)
            operaciones += 1
        print(operaciones)
                
    
if __name__ == "__main__":
    main()
    #ssprint(mayor([2,1,2,2,1]), busqueda_inv(mayor([2,1,2,2,1]), [2,1,2,2,1]))
    
