def solve():
    """Index: 2601.
    Returns: the total amount James has made so far this year.
    """
    # L1
    january_income = 4000 # James made $4000 in January
    feb_multiplier = 2 # made twice as much
    february_income = january_income * feb_multiplier

    # L2
    march_less_than_feb = 2000 # made $2000 less than in February
    march_income = february_income - march_less_than_feb

    # L3
    total_income = january_income + february_income + march_income

    # FA
    answer = total_income
    return answer