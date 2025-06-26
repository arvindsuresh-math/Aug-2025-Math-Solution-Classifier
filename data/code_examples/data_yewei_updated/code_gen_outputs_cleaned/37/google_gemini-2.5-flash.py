def solve(
        num_friends: int = 5, # Five friends
        num_hamburgers: int = 5, # 5 pieces of hamburger
        cost_hamburger_each: int = 3, # cost $3 each
        num_fries_sets: int = 4, # 4 sets of French fries
        cost_fries_set: float = 1.20, # cost $1.20
        num_soda_cups: int = 5, # 5 cups of soda
        cost_soda_each: float = 0.5, # cost $0.5 each
        num_spaghetti_platters: int = 1, # 1 platter of spaghetti
        cost_spaghetti_platter: float = 2.7 # cost $2.7
    ):
    """Index: 37.
    Returns: the amount each friend will pay if they split the bill equally.
    """
    #: L1
    cost_hamburgers = cost_hamburger_each * num_hamburgers

    #: L2
    cost_fries = cost_fries_set * num_fries_sets

    #: L3
    cost_soda = cost_soda_each * num_soda_cups

    #: L4
    total_bill = cost_hamburgers + cost_fries + cost_soda + cost_spaghetti_platter

    #: L5
    cost_per_friend = total_bill / num_friends

    answer = cost_per_friend # FINAL ANSWER
    return answer