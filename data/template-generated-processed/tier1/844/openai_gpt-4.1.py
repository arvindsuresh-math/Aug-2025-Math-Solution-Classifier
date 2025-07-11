def solve():
    """Index: 844.
    Returns: how much older Andy is than Rahim right now, in years.
    """
    # L1
    rahim_now = 6 # Rahim is 6 now
    multiplier = 2 # twice as old
    andy_in_5_years = multiplier * rahim_now

    # L2
    years_until_then = 5 # In 5 years
    andy_now = andy_in_5_years - years_until_then

    # L3
    difference = andy_now - rahim_now

    # FA
    answer = difference
    return answer