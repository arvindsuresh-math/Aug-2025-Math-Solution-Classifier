def solve():
    """Index: 1453.
    Returns: the number of chocolate bars.
    """
    # L1
    box_weight_kg = 2 # 2 kilogram box
    grams_per_kilogram = 1000 # WK
    box_weight_g = box_weight_kg * grams_per_kilogram

    # L2
    bar_weight_g = 125 # A chocolate bar weighs 125 g
    number_of_bars = box_weight_g / bar_weight_g

    # FA
    answer = number_of_bars
    return answer