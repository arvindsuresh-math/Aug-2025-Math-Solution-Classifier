def solve():
    """Index: 5933.
    Returns: the number of $100 bills Marly will have.
    """
    # L1
    bill_value_20 = 20 # $20 bills
    num_20_bills = 10 # ten $20 bills
    total_20_bills_value = bill_value_20 * num_20_bills

    # L2
    bill_value_10 = 10 # $10 bills
    num_10_bills = 8 # eight $10 bills
    total_10_bills_value = bill_value_10 * num_10_bills

    # L3
    bill_value_5 = 5 # $5 bills
    num_5_bills = 4 # four $5 bills
    total_5_bills_value = bill_value_5 * num_5_bills

    # L4
    total_money = total_20_bills_value + total_10_bills_value + total_5_bills_value

    # L5
    target_bill_value = 100 # $100 bills
    num_100_bills = total_money / target_bill_value

    # FA
    answer = num_100_bills
    return answer