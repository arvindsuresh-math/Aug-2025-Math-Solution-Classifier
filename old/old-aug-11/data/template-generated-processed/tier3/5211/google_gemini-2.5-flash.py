def solve():
    """Index: 5211.
    Returns: the total ounces of the drink.
    """
    # L1
    coke_parts = 2 # 2 parts Coke
    sprite_parts = 1 # 1 part Sprite
    mountain_dew_parts = 3 # 3 parts Mountain Dew
    total_parts = coke_parts + sprite_parts + mountain_dew_parts

    # L2
    coke_fraction = coke_parts / total_parts

    # L3
    coke_ounces = 6 # 6 ounces of Coke
    total_ounces = coke_ounces / coke_fraction

    # FA
    answer = total_ounces
    return answer