def solve():
    """Index: 5222.
    Returns: the amount of money saved by buying the gallon container.
    """
    # L1
    gallons = 1 # 1 gallon of mayo
    ounces_per_gallon = 128 # WK
    total_ounces_gallon = gallons * ounces_per_gallon

    # L2
    ounces_per_small_bottle = 16 # a 16-ounce bottle
    num_small_bottles = total_ounces_gallon / ounces_per_small_bottle

    # L3
    cost_per_small_bottle = 3 # bottle costs $3
    cost_small_bottles = num_small_bottles * cost_per_small_bottle

    # L4
    cost_gallon_costco = 8 # 1 gallon of mayo at Costco for 8 dollars
    money_saved = cost_small_bottles - cost_gallon_costco

    # FA
    answer = money_saved
    return answer