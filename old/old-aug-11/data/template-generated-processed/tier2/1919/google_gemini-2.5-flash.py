def solve():
    """Index: 1919.
    Returns: the amount of money Roger still owes on his house.
    """
    # L1
    house_cost = 100000 # Roger bought a house for $100,000
    down_payment_percent_decimal = 0.20 # pay 20% down
    down_payment_amount = house_cost * down_payment_percent_decimal

    # L2
    remaining_balance_after_down_payment = house_cost - down_payment_amount

    # L3
    parents_payment_percent_decimal = 0.30 # parents paid off an additional 30% of the remaining balance
    parents_payment_amount = remaining_balance_after_down_payment * parents_payment_percent_decimal

    # L4
    final_owed_amount = remaining_balance_after_down_payment - parents_payment_amount

    # FA
    answer = final_owed_amount
    return answer