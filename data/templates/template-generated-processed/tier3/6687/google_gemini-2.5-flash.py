def solve():
    """Index: 6687.
    Returns: the cost of each soda.
    """
    # L1
    twenty_dollar_bill = 20 # pays with a 20 dollar bill
    change_received = 14 # gets $14 in change
    total_paid = twenty_dollar_bill - change_received

    # L2
    number_of_sodas = 3 # buys 3 sodas
    cost_per_soda = total_paid / number_of_sodas

    # FA
    answer = cost_per_soda
    return answer