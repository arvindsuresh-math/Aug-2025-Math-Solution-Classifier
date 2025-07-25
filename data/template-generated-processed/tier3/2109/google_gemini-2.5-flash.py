from fractions import Fraction

def solve():
    """Index: 2109.
    Returns: the number of mountains still intact at the end of the year.
    """
    # L1
    erupted_percentage_first_phase = Fraction(20, 100) # 20% of the volcanoes exploded
    total_volcanoes = 200 # 200 active volcanoes
    erupted_first_phase = erupted_percentage_first_phase * total_volcanoes

    # L2
    remaining_after_first_phase = total_volcanoes - erupted_first_phase

    # L3
    erupted_percentage_second_phase = Fraction(40, 100) # 40% of the remaining exploded
    erupted_second_phase = erupted_percentage_second_phase * remaining_after_first_phase

    # L4
    remaining_after_second_phase = remaining_after_first_phase - erupted_second_phase

    # L5
    erupted_percentage_third_phase = Fraction(50, 100) # another 50% of the volcanoes that hadn't already erupted also exploded
    erupted_third_phase = erupted_percentage_third_phase * remaining_after_second_phase

    # L6
    mountains_intact_end_year = remaining_after_second_phase - erupted_third_phase

    # FA
    answer = mountains_intact_end_year
    return answer