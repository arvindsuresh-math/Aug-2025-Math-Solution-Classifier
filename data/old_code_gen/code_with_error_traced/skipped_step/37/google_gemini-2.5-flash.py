def solve(
        num_friends: int = 5, # Five friends
        num_hamburgers: int = 5, # 5 pieces of hamburger
        cost_hamburger: int = 3, # that cost $3 each
        num_french_fries: int = 4, # 4 sets of French fries
        cost_french_fries: float = 1.20, # that cost $1.20
        num_soda: int = 5, # 5 cups of soda
        cost_soda: float = 0.5, # that cost $0.5 each
        num_spaghetti_platters: int = 1, # 1 platter of spaghetti
        cost_spaghetti_platter: float = 2.7 # that cost $2.7
    ):
    """Index: 37.
    Returns: the amount each friend will pay if they split the bill equally.
    """

    #: L1
    cost_total_hamburgers = cost_hamburger * num_hamburgers # eval: 15 = 3 * 5

    #: L2
    cost_total_french_fries = cost_french_fries * num_french_fries # eval: 4.8 = 1.2 * 4

    #: L3
    cost_total_soda = cost_soda * num_soda # eval: 2.5 = 0.5 * 5

    #: L4
    total_bill = cost_total_hamburgers + cost_total_french_fries + cost_total_soda + cost_spaghetti_platter # eval: 25.0 = 15 + 4.8 + 2.5 + 2.7

    #: L5

    #: FA
    answer = num_french_fries
    return answer # eval: return 4
