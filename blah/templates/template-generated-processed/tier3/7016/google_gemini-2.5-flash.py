def solve():
    """Index: 7016.
    Returns: the plant's monthly growth rate in feet.
    """
    # L1
    final_height = 80 # 80 feet tall after a year
    current_height = 20 # currently 20 feet tall
    growth_in_a_year = final_height - current_height

    # L2
    months_per_year = 12 # WK
    monthly_growth_rate = growth_in_a_year / months_per_year

    # FA
    answer = monthly_growth_rate
    return answer