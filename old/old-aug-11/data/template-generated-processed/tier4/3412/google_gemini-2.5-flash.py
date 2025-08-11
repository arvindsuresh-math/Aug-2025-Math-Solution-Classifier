def solve():
    """Index: 3412.
    Returns: the total ounces of chocolate milk Charles will drink.
    """
    # L1
    total_milk_ounces = 130 # 130 ounces of milk
    milk_per_glass = 6.5 # 6.5 ounces of milk
    glasses_from_milk = total_milk_ounces / milk_per_glass

    # L2
    total_syrup_ounces = 60 # 60 ounces of chocolate syrup
    syrup_per_glass = 1.5 # 1.5 ounces of chocolate syrup
    glasses_from_syrup = total_syrup_ounces / syrup_per_glass

    # L3
    max_glasses_possible = min(glasses_from_milk, glasses_from_syrup)

    # L4
    ounces_per_glass = 8 # 8-ounce glasses
    total_chocolate_milk_ounces = max_glasses_possible * ounces_per_glass

    # FA
    answer = total_chocolate_milk_ounces
    return answer