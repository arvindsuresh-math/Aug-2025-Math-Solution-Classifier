def solve():
    """Index: 2259.
    Returns: the total amount Adam would have to spend if he buys both laptops.
    """
    # L1
    first_laptop_price = 500 # The first laptop is $500
    second_laptop_multiplier = 3 # second laptop is 3 times as costly as the first
    second_laptop_price = first_laptop_price * second_laptop_multiplier

    # L2
    total_cost = second_laptop_price + first_laptop_price

    # FA
    answer = total_cost
    return answer