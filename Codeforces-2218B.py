def main():
    n = int(input())
    for i in range(0,n):
        numbers = []
        sum = 0 
        # La forma correcta:
        numbers = list(map(int, input().split()))
        numbers.sort()
        for x in range(0,6):
            numbers[x] = -numbers[x]
        for number in numbers:
            sum += number
        print(sum)
if __name__ == "__main__":
    main()
    