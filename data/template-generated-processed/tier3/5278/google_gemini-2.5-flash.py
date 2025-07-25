def solve():
    """Index: 5278.
    Returns: the total number of bottles in the box.
    """
    # L1
    items_per_dozen = 12 # WK
    water_bottle_dozens = 2 # 2 dozen water bottles
    water_bottles = water_bottle_dozens * items_per_dozen

    # L2
    half_dozen_fraction = 1/2 # half a dozen more apple bottles
    additional_apple_bottles = half_dozen_fraction * items_per_dozen

    # L3
    apple_bottles = water_bottles + additional_apple_bottles

    # L4
    total_bottles = apple_bottles + water_bottles

    # FA
    answer = total_bottles
    return answer