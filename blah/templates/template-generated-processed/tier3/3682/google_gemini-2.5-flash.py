def solve():
    """Index: 3682.
    Returns: the number of $10 bills in Gail's wallet.
    """
    # L1
    five_dollar_bill_value = 5 # $5 bills
    num_five_dollar_bills = 4 # four $5 bills
    amount_from_five_dollar_bills = five_dollar_bill_value * num_five_dollar_bills

    # L2
    twenty_dollar_bill_value = 20 # $20 bills
    num_twenty_dollar_bills = 3 # three $20 bills
    amount_from_twenty_dollar_bills = twenty_dollar_bill_value * num_twenty_dollar_bills

    # L3
    total_from_five_and_twenty_bills = amount_from_five_dollar_bills + amount_from_twenty_dollar_bills

    # L4
    total_amount_in_wallet = 100 # amount to $100
    amount_from_ten_dollar_bills = total_amount_in_wallet - total_from_five_and_twenty_bills

    # L5
    ten_dollar_bill_value = 10 # $10 bills
    num_ten_dollar_bills = amount_from_ten_dollar_bills / ten_dollar_bill_value

    # FA
    answer = num_ten_dollar_bills
    return answer