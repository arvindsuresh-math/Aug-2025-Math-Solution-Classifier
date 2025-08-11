def solve():
    """Index: 6340.
    Returns: the amount of milk left over.
    """
    # L1
    total_milk_ounces = 72 # 72 ounces of milk
    milk_per_milkshake = 4 # 4 ounces of milk
    milkshakes_from_milk = total_milk_ounces / milk_per_milkshake

    # L2
    total_ice_cream_ounces = 192 # 192 ounces of ice cream
    ice_cream_per_milkshake = 12 # 12 ounces of ice cream
    milkshakes_from_ice_cream = total_ice_cream_ounces / ice_cream_per_milkshake

    # L3
    actual_milkshakes_made = min(milkshakes_from_milk, milkshakes_from_ice_cream)

    # L4
    milk_used = actual_milkshakes_made * milk_per_milkshake

    # L5
    milk_left_over = total_milk_ounces - milk_used

    # FA
    answer = milk_left_over
    return answer