def solve():
    """Index: 6942.
    Returns: the total number of legs of all his animals.
    """
    # L1
    num_kangaroos = 23 # 23 kangaroos
    legs_per_kangaroo = 2 # Kangaroos have two legs
    total_kangaroo_legs = num_kangaroos * legs_per_kangaroo

    # L2
    multiplier_goats_kangaroos = 3 # three times as many goats as kangaroos
    num_goats = num_kangaroos * multiplier_goats_kangaroos

    # L3
    legs_per_goat = 4 # goats have four legs
    total_goat_legs = num_goats * legs_per_goat

    # L4
    total_legs_all_animals = total_goat_legs + total_kangaroo_legs

    # FA
    answer = total_legs_all_animals
    return answer