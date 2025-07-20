def solve():
    """Index: 5546.
    Returns: the total amount of money Shelly has.
    """
    # L1
    num_ten_dollar_bills = 10 # ten $10 bills
    value_ten_dollar_bill = 10 # $10 bills
    amount_from_ten_dollar_bills = num_ten_dollar_bills * value_ten_dollar_bill

    # L2
    fewer_five_dollar_bills = 4 # four fewer $5 bills
    num_five_dollar_bills = num_ten_dollar_bills - fewer_five_dollar_bills

    # L3
    value_five_dollar_bill = 5 # $5 bills
    amount_from_five_dollar_bills = num_five_dollar_bills * value_five_dollar_bill

    # L4
    total_money = amount_from_ten_dollar_bills + amount_from_five_dollar_bills

    # FA
    answer = total_money
    return answer