def solve():
    """Index: 2221.
    Returns: the total amount of money Diana earned over July, August, and September.
    """
    # L1
    july_earnings = 150 # Diana earned $150 in July
    august_multiplier = 3 # earned 3 times this amount in August
    august_earnings = august_multiplier * july_earnings

    # L2
    september_multiplier = 2 # earned twice the money she earned in August
    september_earnings = september_multiplier * august_earnings

    # L3
    total_earnings = july_earnings + august_earnings + september_earnings

    # FA
    answer = total_earnings
    return answer