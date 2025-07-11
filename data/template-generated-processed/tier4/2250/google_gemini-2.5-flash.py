import math

def solve():
    """Index: 2250.
    Returns: the number of cans of chickpeas Thomas should buy.
    """
    # L1
    num_servings = 20 # To make 20 servings
    cups_per_serving = 1 # 1 cup of chickpeas
    total_cups_needed = num_servings * cups_per_serving

    # L2
    ounces_per_cup = 6 # In one cup of chickpeas, there are 6 ounces
    total_ounces_needed = total_cups_needed * ounces_per_cup

    # L3
    ounces_per_can = 16 # In a can of chickpeas, there are 16 ounces
    cans_raw = total_ounces_needed / ounces_per_can

    # L4
    cans_to_buy = math.ceil(cans_raw)

    # FA
    answer = cans_to_buy
    return answer