def solve():
    """Index: 6526.
    Returns: how much Tom sold the games for.
    """
    # L1
    initial_cost = 200 # Tom bought his games for $200
    tripled_factor = 3 # They tripled in value
    increased_value = initial_cost * tripled_factor

    # L2
    sold_percentage_decimal = 0.4 # sold 40% of them
    sold_value = increased_value * sold_percentage_decimal

    # FA
    answer = sold_value
    return answer