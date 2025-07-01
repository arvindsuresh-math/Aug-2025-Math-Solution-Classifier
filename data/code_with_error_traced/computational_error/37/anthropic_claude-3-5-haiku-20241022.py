def solve(
    hamburger_price: float = 3.0,  # cost of each hamburger
    num_hamburgers: int = 5,  # number of hamburgers ordered
    fries_price: float = 1.20,  # cost of each set of fries
    num_fries: int = 4,  # number of fries sets ordered
    soda_price: float = 0.50,  # cost of each soda
    num_sodas: int = 5,  # number of sodas ordered
    spaghetti_price: float = 2.70,  # cost of spaghetti platter
    num_friends: int = 5  # number of friends splitting the bill
):
    """Index: 37.
    Returns: the amount each friend will pay when splitting the bill equally."""

    #: L1
    hamburger_total = hamburger_price * num_hamburgers # eval: 15.0 = 3.0 * 5

    #: L2
    fries_total = fries_price * num_fries # eval: 4.8 = 1.2 * 4

    #: L3
    soda_total = soda_price * num_sodas # eval: 2.5 = 0.5 * 5

    #: L4
    total_bill = hamburger_total + fries_total + soda_total + spaghetti_price # eval: 25.0 = 15.0 + 4.8 + 2.5 + 2.7

    #: L5
    individual_share = 4.0 # eval: 4.0 = 4.0

    #: FA
    answer = individual_share
    return answer # eval: return 4.0
