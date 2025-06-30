def solve(
        sara_shoes_cost: int = 50, # Sara buys a pair of shoes which costs $50
        sara_dress_cost: int = 200 # and a dress which costs $200
    ):
    """Index: 41.
    Returns: the total amount Rachel should budget for her shoes and dress.
    """

    #: L1
    rachel_shoes_cost = sara_shoes_cost * 2 # eval: 100 = 50 * 2

    #: L2
    rachel_dress_cost = sara_dress_cost * 2 # eval: 400 = 200 * 2

    #: L3
    total_rachel_budget = rachel_shoes_cost + rachel_dress_cost # eval: 500 = 100 + 400

    #: FA
    answer = total_rachel_budget # eval: 500 = 500
    return answer # eval: return 500
