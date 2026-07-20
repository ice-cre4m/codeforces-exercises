"""
    # MEX Reordering
"""
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int, input().split()))
        print(verificarMEX(array, n))
                
def reorderList(array):
    sortedArray = sorted(array)
    for int in range(0, len(sortedArray)-1):
        if sortedArray[int] == sortedArray[int+1]:
            sortedArray.append(sortedArray.pop(int))
    if sortedArray == array:
        return "NO"
    return sortedArray

def verificarMEX(array, n):
    if array == "NO":
        return "NO"
    
    for x in range(1, n):
            if (MEX(array[0:x]) == MEX(array[x:n])):
                verificarMEX(reorderList(array), n)
    return "YES"
   
def MEX(lista):
    sortedList = sorted(lista)
    
    if 0 not in lista:
        return 0
    
    for i in sortedList:
        if(i+1 not in sortedList):
            return i+1
        
        
if __name__ == "__main__":
    main()