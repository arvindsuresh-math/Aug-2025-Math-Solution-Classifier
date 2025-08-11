def solve():
    """Index: 544.
    Returns: the number of kilograms of dog food Elise already had.
    """
    # L1
    bought_bag1 = 15 # a 15kg bag
    bought_bag2 = 10 # another 10kg bag
    total_bought = bought_bag1 + bought_bag2

    # L2
    total_now = 40 # now has 40kg of dog food
    already_had = total_now - total_bought

    # FA
    answer = already_had
    return answer