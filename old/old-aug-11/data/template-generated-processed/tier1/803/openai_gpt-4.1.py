def solve():
    """Index: 803.
    Returns: the least amount of money the teacher can spend on the bags.
    """
    # L1
    vampire_students = 11 # 11 indicate they want the vampire-themed bag
    pack_size = 5 # packs of 5 of each theme
    pack_price = 3 # price of $3 per package
    individual_price = 1 # price of $1 each
    vampire_packs = 2 # 2 packs of 5 for vampire
    vampire_individuals = 1 # 1 individual bag for vampire
    vampire_cost = vampire_packs * pack_price + vampire_individuals * individual_price

    # L2
    pumpkin_students = 14 # 14 indicate they want the pumpkin-themed bag
    pumpkin_packs = 2 # 2 packs of 5 for pumpkin
    pumpkin_individuals = 4 # 4 individual bags for pumpkin
    pumpkin_cost = pumpkin_packs * pack_price + pumpkin_individuals * individual_price

    # L3
    total_cost = vampire_cost + pumpkin_cost

    # FA
    answer = total_cost
    return answer