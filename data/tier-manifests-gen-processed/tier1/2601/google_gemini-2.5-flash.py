def solve():
    """Index: 2601.
    Returns: the total amount James has made so far this year.
    """
    # L1
    january_earnings = 4000 # $4000 in January
    multiplier_february = 2 # twice as much
    february_earnings = january_earnings * multiplier_february

    # L2
    march_less_than_february = 2000 # $2000 less than in February
    march_earnings = february_earnings - march_less_than_february

    # L3
    total_earnings = january_earnings + february_earnings + march_earnings

    # FA
    answer = total_earnings
    return answer