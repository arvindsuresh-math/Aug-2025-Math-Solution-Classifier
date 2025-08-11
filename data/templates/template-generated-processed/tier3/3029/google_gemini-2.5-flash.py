def solve():
    """Index: 3029.
    Returns: the average number of times Mr. Roper cuts his yard per month.
    """
    # L1
    months_high_frequency = 6 # beginning in April and ending in September
    cuts_per_month_high_frequency = 15 # 15 days a month
    total_cuts_high_frequency = months_high_frequency * cuts_per_month_high_frequency

    # L2
    months_low_frequency = 6 # From October to the end of March
    cuts_per_month_low_frequency = 3 # three times a month
    total_cuts_low_frequency = months_low_frequency * cuts_per_month_low_frequency

    # L3
    total_annual_cuts = total_cuts_high_frequency + total_cuts_low_frequency

    # L4
    months_in_year = 12 # WK
    average_cuts_per_month = total_annual_cuts / months_in_year

    # FA
    answer = average_cuts_per_month
    return answer