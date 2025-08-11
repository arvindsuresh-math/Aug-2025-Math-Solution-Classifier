def solve():
    """Index: 5731.
    Returns: the new balance on Marian's credit card.
    """
    # L1
    groceries_cost = 60.00 # $60.00 worth of groceries
    gas_divisor = 2 # half that amount in gas
    gas_cost = groceries_cost / gas_divisor

    # L2
    initial_balance = 126.00 # $126.00
    balance_after_additions = initial_balance + groceries_cost + gas_cost

    # L3
    returned_amount = 45.00 # $45.00
    final_balance = balance_after_additions - returned_amount

    # FA
    answer = final_balance
    return answer