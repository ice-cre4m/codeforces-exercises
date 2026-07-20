"""
You are given an integer 𝑛. You must construct a permutation∗ of length 3𝑛 such that, 
if you partition the permutation into 𝑛 contiguous blocks with 3 elements,
the sum of the medians† of these blocks is maximised.



"""

def crear_permutaciones(p, t):
    resultado = []
    num_permutaciones = int(t/3)
    for i in range(0,num_permutaciones):
        print(p[i],p.pop(len(p)-2),p.pop())

def main():
    test_cases = int(input())
    
    for x in range(0, test_cases):
        n = 3*int(input())
        permutation = []
        for i in range(1,n+1):
            permutation.append(i)
        crear_permutaciones(permutation, n)
    
    
if __name__ == "__main__":
    main()
    
    
    
