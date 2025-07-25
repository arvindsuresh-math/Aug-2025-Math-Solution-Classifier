def solve():
    """Index: 6646.
    Returns: the total cost of Mrs. Brown's utility bills.
    """
    # L1
    value_50_bill = 50 # $50 bills
    num_50_bills = 3 # 3 $50 bills
    amount_from_50_bills = value_50_bill * num_50_bills

    # L2
    value_10_bill = 10 # $10 bills
    num_10_bills = 2 # 2 $10 bills
    amount_from_10_bills = value_10_bill * num_10_bills

    # L3
    total_utility_bills = amount_from_50_bills + amount_from_10_bills

    # FA
    answer = total_utility_bills
    return answer