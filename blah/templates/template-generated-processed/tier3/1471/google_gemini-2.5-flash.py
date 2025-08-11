def solve():
    """Index: 1471.
    Returns: the number of $20 bills.
    """
    # L4
    total_amount = 120 # amount to $120
    effective_value_per_n = 40 # The number of $10 bills is twice as many $20 bills, so for each $20 bill (n), there are two $10 bills (2n), making the value per n unit $10*2 + $20*1 = $40.
    num_20_dollar_bills = total_amount / effective_value_per_n

    # FA
    answer = num_20_dollar_bills
    return answer