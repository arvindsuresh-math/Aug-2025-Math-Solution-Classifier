def solve():
    """Index: 2221.
    Returns: the total money Diana earned over three months.
    """
    # L1
    july_earnings = 150 # earned $150 in July
    august_multiplier = 3 # 3 times this amount
    august_earnings = august_multiplier * july_earnings

    # L2
    september_multiplier = 2 # twice the money she earned in August
    september_earnings = september_multiplier * august_earnings

    # L3
    total_earnings = july_earnings + august_earnings + september_earnings

    # FA
    answer = total_earnings
    return answer