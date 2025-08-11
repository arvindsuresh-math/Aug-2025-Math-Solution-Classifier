def solve():
    """Index: 4132.
    Returns: the total height of the tree when it is 5 years old.
    """
    # L1
    first_year_growth = 2 # 2 feet in the first year
    growth_factor_second_year = 1.5 # 50% more than the first year
    second_year_growth = first_year_growth * growth_factor_second_year

    # L2
    growth_factor_third_year = 1.5 # 50% more than in the second year
    third_year_growth = second_year_growth * growth_factor_third_year

    # L3
    growth_factor_fourth_year = 2 # twice as much as the third year
    fourth_year_growth = third_year_growth * growth_factor_fourth_year

    # L4
    growth_divisor_fifth_year = 2 # half as much as the fourth year
    fifth_year_growth = fourth_year_growth / growth_divisor_fifth_year

    # L5
    total_height = first_year_growth + second_year_growth + third_year_growth + fourth_year_growth + fifth_year_growth

    # FA
    answer = total_height
    return answer