def solve():
    """Index: 1257.
    Returns: how much more money Bob has than Alice after investments.
    """
    # L1
    initial_investment = 2000 # Alice and Bob are each given $2000 to invest
    alice_multiplier = 2 # Alice ... doubles her money
    alice_final_money = initial_investment * alice_multiplier

    # L2
    bob_multiplier = 5 # Bob ... makes five times more money than he invested
    bob_money_made = initial_investment * bob_multiplier

    # L3
    bob_total_money = bob_money_made + initial_investment

    # L4
    difference_bob_alice = bob_total_money - alice_final_money

    # FA
    answer = difference_bob_alice
    return answer