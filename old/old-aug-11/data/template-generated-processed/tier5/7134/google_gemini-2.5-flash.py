def solve():
    """Index: 7134.
    Returns: the number of erasers Celine collected.
    """
    # L2
    multiplier_celine = 2 # twice as many erasers as Gabriel did
    celine_coefficient = multiplier_celine

    # L3
    multiplier_julian = 2 # twice as many erasers as Celine did
    julian_coefficient = multiplier_julian * celine_coefficient
    simplified_julian_coefficient = 4 # This is 2*2, used in template

    # L4
    gabriel_coefficient = 1 # WK
    total_coefficient_sum = gabriel_coefficient + celine_coefficient + julian_coefficient

    # L6
    total_erasers_total = 35 # 35 erasers in total
    gabriel_erasers_value = total_erasers_total / total_coefficient_sum

    # L7
    celine_collected_final = gabriel_erasers_value * multiplier_celine

    # FA
    answer = celine_collected_final
    return answer