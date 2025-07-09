def solve(
    num_friends: int = 5, # Five friends
    num_hamburger: int = 5, # 5 pieces of hamburger
    cost_hamburger: float = 3, # cost $3 each
    num_fries: int = 4, # 4 sets of French fries
    cost_fries: float = 1.20, # cost $1.20
    num_soda: int = 5, # 5 cups of soda
    cost_soda: float = 0.5, # cost $0.5 each
    num_spaghetti: int = 1, # 1 platter of spaghetti
    cost_spaghetti: float = 2.7 # cost $2.7
):
    """Index: 37.
    Returns: the amount each friend will pay if they split the bill equally.
    """

    #: L1
    cost_total_hamburger = cost_hamburger * num_hamburger # eval: 15 = 3 * 5

    #: L2
    cost_total_fries = cost_fries * num_fries # eval: 4.8 = 1.2 * 4

    #: L3
    cost_total_soda = cost_hamburger * num_soda # eval: 15 = 3 * 5

    #: L4
    total_bill = cost_total_hamburger + cost_total_fries + cost_total_soda + cost_spaghetti # eval: 37.5 = 15 + 4.8 + 15 + 2.7

    #: L5
    cost_per_friend = total_bill / num_friends # eval: 7.5 = 37.5 / 5

    #: FA
    answer = cost_per_friend
    return answer # eval: return 7.5
