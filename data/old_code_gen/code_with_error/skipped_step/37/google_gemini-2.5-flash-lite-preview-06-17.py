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

    #: L2
    total_cost_fries = num_fries * cost_per_fries

    #: L3
    total_cost_sodas = num_sodas * cost_per_soda

    #: L4
    total_bill = num_friends + total_cost_fries + total_cost_sodas + cost_spaghetti

    #: L5
    cost_per_friend = total_bill / num_friends

    #: FA
    answer = cost_per_friend
    return answer