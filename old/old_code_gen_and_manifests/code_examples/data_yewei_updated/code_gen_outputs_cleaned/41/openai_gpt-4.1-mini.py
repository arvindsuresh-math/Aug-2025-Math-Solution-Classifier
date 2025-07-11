def solve(
    cost_shoes_sara: int = 50,  # Sara buys a pair of shoes which costs $50
    cost_dress_sara: int = 200  # and a dress which costs $200
):
    """Index: 41.
    Returns: the total amount Rachel should budget to spend twice as much as Sara on shoes and dress.
    """
    #: L1
    cost_shoes_rachel = cost_shoes_sara * 2

    #: L2
    cost_dress_rachel = cost_dress_sara * 2

    #: L3
    total_budget_rachel = cost_shoes_rachel + cost_dress_rachel

    answer = total_budget_rachel  # FINAL ANSWER
    return answer