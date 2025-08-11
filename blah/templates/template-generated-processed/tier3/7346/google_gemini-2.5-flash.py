def solve():
    """Index: 7346.
    Returns: the total number of Starbursts candies Penelope has.
    """
    # L2
    m_and_m_per_unit = 5 # 5 M&M candies for every 3 Starbursts candies
    total_m_and_m = 25 # 25 M&M candies
    num_units_m_and_m = total_m_and_m / m_and_m_per_unit

    # L3
    starbursts_per_unit = 3 # 3 Starbursts candies
    total_starbursts = num_units_m_and_m * starbursts_per_unit

    # FA
    answer = total_starbursts
    return answer