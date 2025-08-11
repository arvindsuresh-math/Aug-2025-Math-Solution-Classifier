def solve():
    """Index: 4204.
    Returns: Alexander's height in inches on his 12th birthday.
    """
    # L1
    inches_per_foot = 12 # WK
    growth_rate_feet_per_year = 0.5 # grows 1/2 a foot a year
    growth_per_year_inches = inches_per_foot * growth_rate_feet_per_year

    # L2
    target_birthday = 12 # 12th birthday
    initial_birthday = 8 # 8th birthday
    total_years_growing = target_birthday - initial_birthday
    total_growth_inches = total_years_growing * growth_per_year_inches

    # L3
    initial_height_inches = 50 # 50 inches on his 8th birthday
    final_height = initial_height_inches + total_growth_inches

    # FA
    answer = final_height
    return answer