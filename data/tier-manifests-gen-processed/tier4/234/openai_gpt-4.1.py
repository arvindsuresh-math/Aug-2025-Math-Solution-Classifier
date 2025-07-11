def solve():
    """Index: 234.
    Returns: the number of nickels Mark gets in his change.
    """
    # L1
    amount_given = 7.00 # Mark gives the cashier $7.00
    bread_cost = 4.20 # loaf of bread for $4.20
    cheese_cost = 2.05 # cheese for $2.05
    change = amount_given - bread_cost - cheese_cost

    # L2
    quarter_value = 0.25 # value of a quarter in dollars
    dime_value = 0.10 # value of a dime in dollars
    nickels_amount = change - quarter_value - dime_value

    # L3
    nickel_value = 0.05 # value per nickel in dollars
    num_nickels = nickels_amount / nickel_value

    # FA
    answer = num_nickels
    return answer