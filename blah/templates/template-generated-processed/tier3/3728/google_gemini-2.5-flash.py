def solve():
    """Index: 3728.
    Returns: the total time Marcus spends on the calzones.
    """
    # L1
    saute_onions_time = 20 # 20 minutes to saute the onions
    quarter_divisor = 4 # a quarter of that time
    saute_garlic_peppers_time = saute_onions_time / quarter_divisor

    # L2
    knead_dough_time = 30 # 30 minutes to knead the dough
    twice_multiplier = 2 # twice as long
    dough_rest_time = knead_dough_time * twice_multiplier

    # L3
    total_dough_time = dough_rest_time + knead_dough_time

    # L4
    tenth_divisor = 10 # 1/10th the combined kneading and resting time
    assemble_calzones_time = total_dough_time / tenth_divisor

    # L5
    total_time = assemble_calzones_time + saute_onions_time + saute_garlic_peppers_time + dough_rest_time + knead_dough_time

    # FA
    answer = total_time
    return answer