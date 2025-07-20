def solve():
    """Index: 6023.
    Returns: the number of pies Smith's Bakery sold.
    """
    # L1
    mcgees_pies = 16 # If Mcgee’s Bakery sold 16 pies
    multiplier = 4 # four times the number of pies
    four_times_mcgees = mcgees_pies * multiplier

    # L2
    more_than_four_times = 6 # 6 more than four times
    smiths_pies = four_times_mcgees + more_than_four_times

    # FA
    answer = smiths_pies
    return answer