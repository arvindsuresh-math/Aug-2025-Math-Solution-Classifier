def solve():
    """Index: 41.
    Returns: the total amount Rachel should budget if she wants to spend twice as much as Sara on shoes and dress.
    """
    # L1
    sara_shoes = 50 # pair of shoes which costs $50
    multiplier = 2 # twice as much
    rachel_shoes = sara_shoes * multiplier

    # L2
    sara_dress = 200 # dress which costs $200
    rachel_dress = sara_dress * multiplier

    # L3
    total_budget = rachel_shoes + rachel_dress

    # FA
    answer = total_budget
    return answer