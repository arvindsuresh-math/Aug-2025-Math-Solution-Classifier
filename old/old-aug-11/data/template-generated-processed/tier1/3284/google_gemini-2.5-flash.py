def solve():
    """Index: 3284.
    Returns: the number of toonies Antonella initially had.
    """
    # L1
    spent_amount = 3 # bought a $3 Frappuccino
    remaining_amount = 11 # still has $11
    initial_total_money = spent_amount + remaining_amount

    # Variables needed for solving the system of equations, not directly tied to templated solution lines L2-L7
    loonie_value = 1 # A loonie equals $1
    toonie_value = 2 # a toonie equals $2
    total_coins_initial = 10 # ten Canadian coins

    # Implicit calculation for L (number of loonies) by solving the system of equations:
    # L + T = total_coins_initial
    # loonie_value * L + toonie_value * T = initial_total_money
    # Substituting T = total_coins_initial - L into the second equation:
    # loonie_value * L + toonie_value * (total_coins_initial - L) = initial_total_money
    # L + 2 * (10 - L) = 14
    # L + 20 - 2L = 14
    # 20 - L = 14
    # L = 20 - 14
    num_loonies = (toonie_value * total_coins_initial) - initial_total_money

    # L8
    num_toonies = total_coins_initial - num_loonies

    # FA
    answer = num_toonies
    return answer