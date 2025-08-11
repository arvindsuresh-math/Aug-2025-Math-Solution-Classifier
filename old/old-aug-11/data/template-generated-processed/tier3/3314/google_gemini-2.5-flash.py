def solve():
    """Index: 3314.
    Returns: the total cost to buy the needed sheets of paper.
    """
    # L1
    sheets_needed = 5000 # needs 5000 sheets of bond paper
    sheets_per_ream = 500 # A bond paper ream has 500 sheets
    reams_needed = sheets_needed / sheets_per_ream

    # L2
    cost_per_ream = 27 # costs $27
    total_cost = reams_needed * cost_per_ream

    # FA
    answer = total_cost
    return answer