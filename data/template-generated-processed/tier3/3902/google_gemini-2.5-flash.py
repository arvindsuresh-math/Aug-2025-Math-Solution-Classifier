def solve():
    """Index: 3902.
    Returns: the total ounces of coconut oil the chef will use.
    """
    # L1
    butter_per_cup_mix = 2 # 2 ounces of butter for every 1 cup of baking mix
    remaining_butter = 4 # 4 ounces of butter remaining
    cups_covered_by_butter = remaining_butter / butter_per_cup_mix

    # L2
    total_baking_mix_cups = 6 # 6 cups of baking mix
    cups_requiring_coconut_oil = total_baking_mix_cups - cups_covered_by_butter

    # L3
    coconut_oil_per_cup_mix = 2 # 2 ounces of coconut oil to be substituted for the 2 ounces of butter
    total_coconut_oil_needed = cups_requiring_coconut_oil * coconut_oil_per_cup_mix

    # FA
    answer = total_coconut_oil_needed
    return answer