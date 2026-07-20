
'''

10101 -> 11111
10101 -> 10101

'''
def maximo(string, n):
    for x in range(1, n-1):
        if string[x+1] == "1" and string[x-1] == "1":
            string[x] = "1"
    return string 


def main():
    #test_cases = int(input())
    #n = int(input())
    s = list(input())
    n = 4
    print(maximo(s, n))
    
    
if __name__ == "__main__":
    main()