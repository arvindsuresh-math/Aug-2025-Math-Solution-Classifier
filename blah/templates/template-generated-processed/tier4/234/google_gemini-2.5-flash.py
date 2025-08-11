def solve():
    """Index: 234.
    Returns: the number of nickels Mark gets in his change.
    """
    # L1
    cash_given = 7.00 # He gives the cashier $7.00
    bread_cost = 4.20 # a loaf of bread for $4.20
    cheese_cost = 2.05 # some cheese for $2.05
    total_change = cash_given - bread_cost - cheese_cost

    # L2
    quarter_value = 0.25 # WK
    dime_value = 0.10 # WK
    change_in_nickels_amount = total_change - quarter_value - dime_value

    # L3
    nickel_value = 0.05 # WK
    num_nickels = change_in_nickels_amount / nickel_value

    # FA
    answer = num_nickels
    return answer