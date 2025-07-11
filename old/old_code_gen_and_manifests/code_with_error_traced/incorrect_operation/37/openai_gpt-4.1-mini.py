def solve(
    num_friends: int = 5,  # Five friends
    num_hamburgers: int = 5,  # 5 pieces of hamburger
    cost_per_hamburger: float = 3.0,  # $3 each hamburger
    num_fries: int = 4,  # 4 sets of French fries
    cost_per_fries: float = 1.20,  # $1.20 per fries
    num_sodas: int = 5,  # 5 cups of soda
    cost_per_soda: float = 0.5,  # $0.5 each soda
    num_spaghetti: int = 1,  # 1 platter of spaghetti
    cost_per_spaghetti: float = 2.7  # $2.7 per spaghetti
):
    """Index: 37.
    Returns: the amount each friend pays when the bill is split equally.
    """

    #: L1
    total_cost_hamburgers = cost_per_hamburger * num_hamburgers # eval: 15.0 = 3.0 * 5

    #: L2
    total_cost_fries = cost_per_fries * num_fries # eval: 4.8 = 1.2 * 4

    #: L3
    total_cost_sodas = cost_per_soda * num_sodas # eval: 2.5 = 0.5 * 5

    #: L4
    total_bill = total_cost_hamburgers + total_cost_fries + total_cost_sodas + (cost_per_spaghetti - num_spaghetti) # eval: 24.0 = 15.0 + 4.8 + 2.5 + (2.7 - 1)

    #: L5
    amount_per_friend = total_bill / num_friends # eval: 4.8 = 24.0 / 5

    #: FA
    answer = amount_per_friend
    return answer # eval: return 4.8
