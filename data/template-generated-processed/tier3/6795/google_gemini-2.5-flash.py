def solve():
    """Index: 6795.
    Returns: the number of bottles of lower sodium soy sauce Stephanie should buy.
    """
    # L1
    first_recipe_cups = 2 # calls for 2 cups of lower sodium soy sauce
    second_recipe_cups = 1 # calls for 1 cup
    third_recipe_cups = 3 # calls for 3 cups
    total_cups_needed = first_recipe_cups + second_recipe_cups + third_recipe_cups

    # L2
    ounces_per_cup = 8 # There are 8 ounces in 1 cup
    total_ounces_needed = total_cups_needed * ounces_per_cup

    # L3
    ounces_per_bottle = 16 # One bottle of lower sodium soy sauce holds 16 ounces
    bottles_to_buy = total_ounces_needed / ounces_per_bottle

    # FA
    answer = bottles_to_buy
    return answer