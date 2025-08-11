def solve():
    """Index: 1626.
    Returns: the total amount of money Ali has in his wallet.
    """
    # L1
    num_5_bills = 7 # 7 bills of 5 dollars
    value_5_bill = 5 # 5 dollars
    value_from_5_bills = num_5_bills * value_5_bill

    # L2
    value_10_bill = 10 # 1 bill of 10 dollars
    total_money = value_from_5_bills + value_10_bill

    # FA
    answer = total_money
    return answer