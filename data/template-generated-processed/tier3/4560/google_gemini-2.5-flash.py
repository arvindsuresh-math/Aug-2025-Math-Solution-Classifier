def solve():
    """Index: 4560.
    Returns: the total number of comics James has written.
    """
    # L1
    days_per_year = 365 # WK
    years = 4 # for 4 years
    total_days = days_per_year * years

    # L2
    writing_frequency_divisor = 2 # every other day
    total_comics = total_days / writing_frequency_divisor

    # FA
    answer = total_comics
    return answer