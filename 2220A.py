def main():
    t = int(input())  # test cases
    for _ in range(t):
        n = int(input())
        listNumbers = list(map(int, input().split()))
        if len(listNumbers) != len(set(listNumbers)):
            print(-1)
        else:
            listNumbers.sort(reverse=True)
            print(*listNumbers)


if __name__ == "__main__":
    main()