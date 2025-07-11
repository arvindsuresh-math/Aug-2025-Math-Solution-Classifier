def solve():
    """Index: 2250.
    Returns: the number of cans of chickpeas Thomas should buy for 20 servings of hummus.
    """
    # L1
    servings_needed = 20 # to make 20 servings
    cups_per_serving = 1 # 1 cup of chickpeas per serving
    total_cups = servings_needed * cups_per_serving

    # L2
    ounces_per_cup = 6 # 6 ounces in one cup
    total_ounces = total_cups * ounces_per_cup

    # L3
    ounces_per_can = 16 # 16 ounces in a can
    cans_needed = total_ounces / ounces_per_can

    # L4
    import math
    answer = math.ceil(cans_needed)
    return answer