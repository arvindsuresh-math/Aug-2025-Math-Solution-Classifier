def solve(
    sara_shoes_cost: int = 50, # Sara buys a pair of shoes which costs $50
    sara_dress_cost: int = 200, # and a dress which costs $200
    rachel_multiplier: int = 2 # spend twice as much as what Sara spent
):
    """Index: 41.
    Returns: the total amount Rachel should budget for her shoes and dress.
    """

    #: L1
    rachel_shoes_budget = sara_shoes_cost * rachel_multiplier # eval: 100 = 50 * 2

    #: L2
    rachel_dress_budget = rachel_multiplier * rachel_multiplier # eval: 4 = 2 * 2

    #: L3
    total_rachel_budget = rachel_shoes_budget + rachel_dress_budget # eval: 104 = 100 + 4

    #: FA
    answer = total_rachel_budget
    return answer # eval: return 104
