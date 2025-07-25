def solve():
    """Index: 7224.
    Returns: the total amount of money Meghan had.
    """
    # L1
    num_100_bills = 2 # 2 $100 bills
    value_100_bill = 100 # 2 $100 bills
    total_100_bills_value = num_100_bills * value_100_bill

    # L2
    num_50_bills = 5 # 5 $50 bills
    value_50_bill = 50 # 5 $50 bills
    total_50_bills_value = num_50_bills * value_50_bill

    # L3
    num_10_bills = 10 # 10 $10 bills
    value_10_bill = 10 # 10 $10 bills
    total_10_bills_value = num_10_bills * value_10_bill

    # L4
    final_total_value = total_100_bills_value + total_50_bills_value + total_10_bills_value

    # FA
    answer = final_total_value
    return answer