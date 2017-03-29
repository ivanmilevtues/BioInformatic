from itertools import permutations

def calc_num_of_coins(change):
    return sum(v for k, v in change.items())


def give_change(money, coins):
    result = {}

    for i in coins:
        result[i] = int(money / i)
        money %= i

    return result


def change(money):
    COINS = [25, 20, 10, 5, 1]
    smallest_change = []
    for coins_configuration in permutations(COINS):
        curr_change = give_change(money, coins_configuration)
        curr_num = calc_num_of_coins(curr_change)
        try:
            if smallest_num_coins > curr_num:
                smallest_num_coins = curr_num
                smallest_change = curr_change
        except NameError:
            smallest_num_coins = curr_num
            smallest_change = curr_change

    return smallest_change


def recursive_change(money, coins):
    if money == 0:
        return 0

    for coin in coins:
        print(money, '>= ', coin)
        if money >= coin:
            num_coins = recursive_change(money - coin, coins) + 1
            print(num_coins)
            try:
                if num_coins + 1 < best_num_coins:
                    best_num_coins = num_coins + 1
            except NameError:
                best_num_coins = num_coins
    return best_num_coins



def DPChange(money, coins, d):
    

def main():
    print(change(77))
    # print(recursive_change(77, [25, 20, 10, 5, 1]))

if __name__ == '__main__':
    main()