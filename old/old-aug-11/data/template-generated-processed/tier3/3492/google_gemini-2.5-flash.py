def solve():
    """Index: 3492.
    Returns: the total number of bills Samuel has in his wallet.
    """
    # L1
    num_20_dollar_bills = 4 # he has 4 $20-bills
    value_20_dollar_bill = 20 # $20 bills
    amount_20_dollar_bills = num_20_dollar_bills * value_20_dollar_bill

    # L2
    amount_10_dollar_bills = 50 # His $10-bills amount to $50
    total_amount_10_and_20_bills = amount_20_dollar_bills + amount_10_dollar_bills

    # L3
    total_amount_in_wallet = 150 # amount to $150 in his wallet
    amount_5_dollar_bills = total_amount_in_wallet - total_amount_10_and_20_bills

    # L4
    value_5_dollar_bill = 5 # $5 bills
    num_5_dollar_bills = amount_5_dollar_bills / value_5_dollar_bill

    # L5
    value_10_dollar_bill = 10 # $10 bills
    num_10_dollar_bills = amount_10_dollar_bills / value_10_dollar_bill

    # L6
    total_bills = num_5_dollar_bills + num_20_dollar_bills + num_10_dollar_bills

    # FA
    answer = total_bills
    return answer