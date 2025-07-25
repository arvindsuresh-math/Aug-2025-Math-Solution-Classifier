def solve(
    sara_shoe_cost: int = 50,  # Sara buys a pair of shoes which costs $50
    sara_dress_cost: int = 200,  # Sara buys a dress which costs $200
    rachel_multiplier: int = 2  # Rachel wants to spend twice as much
):
    """Index: 41.
    Returns: the total amount Rachel should budget for shoes and a dress.
    """

    #: L1
    rachel_shoe_cost = sara_shoe_cost * rachel_multiplier # eval: 100 = 50 * 2

    #: L2
    rachel_dress_cost = sara_dress_cost * rachel_multiplier # eval: 400 = 200 * 2

    #: L3

    #: FA
    answer = sara_shoe_cost
    return answer # eval: return 50
