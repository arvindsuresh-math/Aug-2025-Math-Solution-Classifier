def solve():
    """Index: 5777.
    Returns: the total number of pounds of food Peter will buy.
    """
    # L1
    chicken_pounds = 16 # 16 pounds of bone-in chicken
    hamburger_divisor = 2 # half that amount in hamburgers
    hamburger_pounds = chicken_pounds / hamburger_divisor

    # L2
    hotdog_extra_pounds = 2 # 2 more pounds of hot dogs
    hotdog_pounds = hotdog_extra_pounds + hamburger_pounds

    # L3
    sides_divisor = 2 # half the amount of hot dogs
    sides_pounds = hotdog_pounds / sides_divisor

    # L4
    total_food_pounds = chicken_pounds + hamburger_pounds + hotdog_pounds + sides_pounds

    # FA
    answer = total_food_pounds
    return answer