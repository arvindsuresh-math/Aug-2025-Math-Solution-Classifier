def solve():
    """Index: 3678.
    Returns: the age of the tree when it is 23 feet tall.
    """
    # L1
    final_height = 23 # 23 feet tall
    initial_height = 5 # 5 feet tall
    height_grown = final_height - initial_height

    # L2
    growth_rate_per_year = 3 # gains 3 feet per year
    years_older = height_grown / growth_rate_per_year

    # L3
    initial_age = 1 # 1 year old
    final_age = years_older + initial_age

    # FA
    answer = final_age
    return answer