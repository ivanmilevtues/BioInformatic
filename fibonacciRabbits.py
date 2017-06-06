def fib_rabbits(n, k):
    rabbits = [0,1]
    for i in range(n-1):
        print(rabbits)
        rabbits[i % 2] = rabbits[(i-1) % 2] + k*rabbits[i % 2]

    return rabbits[n % 2]


def main():
    rabbits = str(fib_rabbits(28, 2))

    print(rabbits)


if __name__ == '__main__':
    main()

