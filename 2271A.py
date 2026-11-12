def main():
    t = int(input())  # test_cases
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a == b:
            print(a)
        elif b > a:
            if b == a + 1:
                print(b)
            else:
                print(-1)
        else:  # a > b
            if (a + b) % 2 == 0:
                print(a)
            else:
                print(a + 1)

if __name__ == "__main__":
    main()


# Move one unit up or one unit down: (x,y)→(x,y+1) or (x,y)→(x,y−1).
# Then move one unit to the right: (x,y)→(x+1,y). 

#Por ejmplo podemos pasar por 0,1 pero no por 0,2. La unica relga que sigue es la diferencia entre x y y
#No es posible si la diferencia entre x y y es mayor a 1 