def solve():
    """Index: 4652.
    Returns: the remaining ounces Jamie can drink before needing to use the bathroom.
    """
    # L1
    ounces_from_milk_cup = 8 # a cup of milk at lunch; A cup equals 8 ounces
    ounces_from_grape_juice_pint = 16 # a pint of grape juice at recess; a pint equals 16 ounces
    total_drank_initial = ounces_from_milk_cup + ounces_from_grape_juice_pint

    # L2
    max_liquid_before_bathroom = 32 # any more than 32 ounces of liquid
    remaining_drinkable = max_liquid_before_bathroom - total_drank_initial

    # FA
    answer = remaining_drinkable
    return answer