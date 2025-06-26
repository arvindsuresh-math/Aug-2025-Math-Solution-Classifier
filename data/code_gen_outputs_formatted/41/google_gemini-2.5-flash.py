def solve(
        sara_shoes_cost: int = 50, # Sara buys a pair of shoes which costs $50
        sara_dress_cost: int = 200 # and a dress which costs $200
    ):
    """Index: 41.
    Returns: the total amount Rachel should budget for her shoes and dress.
    """

    #: L1
    rachel_shoes_cost = sara_shoes_cost * 2

    #: L2
    rachel_dress_cost = sara_dress_cost * 2

    #: L3
    total_rachel_budget = rachel_shoes_cost + rachel_dress_cost

    answer = total_rachel_budget # FINAL ANSWER
    return answer