def solve():
    """Index: 5153.
    Returns: Juanico's age 30 years from now.
    """
    # L1
    gladys_future_age = 40 # Gladys will be 40 years old ten years from now
    years_to_subtract_L1 = 10 # ten years from now
    gladys_current_age = gladys_future_age - years_to_subtract_L1

    # L2
    juanico_age_less = 4 # 4 years less than half the age of Gladys
    half_numerator = 1 # 1/2*30
    half_denominator = 2 # 1/2*30
    half_gladys_age = half_numerator / half_denominator * gladys_current_age

    # L3
    juanico_current_age = half_gladys_age - juanico_age_less

    # L4
    years_to_add_L4 = 30 # 30 years from now
    juanico_future_age = years_to_add_L4 + juanico_current_age

    # FA
    answer = juanico_future_age
    return answer