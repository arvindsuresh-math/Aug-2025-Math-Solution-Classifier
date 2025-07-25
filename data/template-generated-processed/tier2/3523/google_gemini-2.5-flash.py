def solve():
    """Index: 3523.
    Returns: the number of female brunettes under 5 feet tall.
    """
    # L1
    total_students = 200 # 200 students
    female_percent_num = 60 # 60% of the students
    female_percent_decimal = 0.6 # from solution text: 0.6*200
    num_female_students = female_percent_decimal * total_students

    # L2
    brunette_female_percent_decimal = 0.5 # 50% of the females
    num_female_brunettes = brunette_female_percent_decimal * num_female_students

    # L3
    under_5_feet_percent_num = 50 # 50% of the female brunettes
    percent_factor = 0.01 # WK
    num_female_brunettes_under_5_feet = under_5_feet_percent_num * percent_factor * num_female_brunettes

    # FA
    answer = num_female_brunettes_under_5_feet
    return answer