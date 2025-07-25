def solve():
    """Index: 4353.
    Returns: the amount of money Norris has left.
    """
    # L1
    september_savings = 29 # saved $29 in September
    october_savings = 25 # saved $25 in October
    november_savings = 31 # saved $31 in November
    total_saved = september_savings + october_savings + november_savings

    # L2
    hugo_spent = 75 # Hugo spent $75 on an online game
    norris_left = total_saved - hugo_spent

    # FA
    answer = norris_left
    return answer