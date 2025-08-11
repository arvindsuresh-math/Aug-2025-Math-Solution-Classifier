def solve():
    """Index: 423.
    Returns: the amount of money Mom has left after shopping.
    """
    # L1
    price_banana_pack = 4 # €4 each (bananas)
    num_banana_packs = 2 # 2 packs of bananas
    price_pears = 2 # pears for €2
    price_asparagus = 6 # asparagus for €6
    price_chicken = 11 # chicken for €11
    total_spent = price_banana_pack + price_banana_pack + price_pears + price_asparagus + price_chicken

    # L2
    initial_money = 55 # left with €55
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer