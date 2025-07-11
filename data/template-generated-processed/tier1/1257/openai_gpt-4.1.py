def solve():
    """Index: 1257.
    Returns: how much more money Bob has now than Alice after investing.
    """
    # L1
    initial_investment = 2000 # each given $2000 to invest
    alice_multiplier = 2 # doubles her money
    alice_final = initial_investment * alice_multiplier

    # L2
    bob_multiplier = 5 # makes five times more money than he invested
    bob_profit = initial_investment * bob_multiplier

    # L3
    bob_final = bob_profit + initial_investment

    # L4
    difference = bob_final - alice_final

    # FA
    answer = difference
    return answer