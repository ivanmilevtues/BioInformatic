COINS = [1, 5, 10, 25]

def give_change(money):
    COINS.sort(reverse=True)
    result = {}

    for k in COINS:
        result[k] = 0

    for i in COINS:
        result[i] = int(money / i)
        money %= i

    return result

def main():
    print(give_change(77))


if __name__ == '__main__':
    main()