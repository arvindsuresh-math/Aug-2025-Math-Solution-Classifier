def solve():
    """Index: 2400.
    Returns: the total amount Alexander spends on apples and oranges.
    """
    # L1
    num_apples = 5 # 5 apples
    price_per_apple = 1 # $1 each
    apples_cost = num_apples * price_per_apple

    # L2
    num_oranges = 2 # 2 oranges
    price_per_orange = 2 # $2 each
    oranges_cost = num_oranges * price_per_orange

    # L3
    total_cost = apples_cost + oranges_cost

    # FA
    answer = total_cost
    return answer