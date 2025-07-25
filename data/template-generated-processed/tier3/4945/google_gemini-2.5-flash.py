def solve():
    """Index: 4945.
    Returns: the difference in number between spotted females and horned males.
    """
    # L1
    total_cows = 300 # 300 cows in a field
    ratio_part_divisor = 3 # There are twice as many females as males (1 male + 2 female = 3 parts)
    female_ratio_multiplier = 2 # There are twice as many females as males
    intermediate_calculation_L1 = total_cows / ratio_part_divisor
    female_cows = intermediate_calculation_L1 * female_ratio_multiplier

    # L2
    male_divisor = 2 # There are twice as many females as males (males are half of females)
    male_cows = female_cows / male_divisor

    # L3
    spotted_female_divisor = 2 # Half the females are spotted
    spotted_females = female_cows / spotted_female_divisor

    # L4
    horned_male_divisor = 2 # half the males have horns
    horned_males = male_cows / horned_male_divisor

    # L5
    difference_spotted_horned = spotted_females - horned_males

    # FA
    answer = difference_spotted_horned
    return answer