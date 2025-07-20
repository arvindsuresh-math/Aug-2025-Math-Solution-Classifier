def solve():
    """Index: 5030.
    Returns: the earnings from the tickets in 6 minutes.
    """
    # L1
    tickets_per_minute = 5 # sells an average of 5 such tickets
    cost_per_ticket = 3 # One ticket to the underground costs $3
    earnings_per_minute = tickets_per_minute * cost_per_ticket

    # L2
    total_minutes = 6 # in 6 minutes
    total_earnings = earnings_per_minute * total_minutes

    # FA
    answer = total_earnings
    return answer