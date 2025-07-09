def solve(
    num_hamburgers: int = 5, # 5 pieces of hamburger
    cost_per_hamburger: float = 3, # cost $3 each
    num_fries: int = 4, # 4 sets of French fries
    cost_per_fries: float = 1.20, # cost $1.20
    num_sodas: int = 5, # 5 cups of soda
    cost_per_soda: float = 0.5, # cost $0.5 each
    cost_spaghetti: float = 2.7, # 1 platter of spaghetti that cost $2.7
    num_friends: int = 5 # Five friends
):
    """Index: 37.
    Returns: the amount each friend will pay if they split the bill equally.
    """

    #: L1
    total_cost_hamburgers = num_hamburgers * cost_per_hamburger # eval: 15 = 5 * 3

    #: L2
    total_cost_fries = num_fries * cost_per_fries # eval: 4.8 = 4 * 1.2

    #: L3
    total_cost_sodas = num_sodas * cost_per_soda # eval: 2.5 = 5 * 0.5

    #: L4
    total_bill = total_cost_hamburgers + total_cost_fries + total_cost_sodas + total_cost_fries # eval: 27.1 = 15 + 4.8 + 2.5 + 4.8

    #: L5
    cost_per_friend = total_bill / num_friends # eval: 5.42 = 27.1 / 5

    #: FA
    answer = cost_per_friend
    return answer # eval: return 5.42
