def solve():
    """Index: 6073.
    Returns: the total number of light bulbs not broken in both the foyer and kitchen.
    """
    # L1
    total_kitchen_bulbs = 35 # there are 35 light bulbs in the kitchen
    kitchen_denominator = 5 # Three fifths of the light bulbs
    bulbs_per_fifth_kitchen = total_kitchen_bulbs / kitchen_denominator

    # L2
    kitchen_numerator = 3 # Three fifths of the light bulbs
    broken_kitchen_bulbs = bulbs_per_fifth_kitchen * kitchen_numerator

    # L3
    not_broken_kitchen_bulbs = total_kitchen_bulbs - broken_kitchen_bulbs

    # L4
    broken_foyer_bulbs = 10 # 10 light bulbs in the foyer are broken
    foyer_denominator = 3 # A third of the light bulbs in the foyer
    total_foyer_bulbs = broken_foyer_bulbs * foyer_denominator

    # L5
    not_broken_foyer_bulbs = total_foyer_bulbs - broken_foyer_bulbs

    # L6
    total_not_broken_bulbs = not_broken_kitchen_bulbs + not_broken_foyer_bulbs

    # FA
    answer = total_not_broken_bulbs
    return answer