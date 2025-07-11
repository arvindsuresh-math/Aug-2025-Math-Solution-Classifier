def solve():
    """Index: 1626.
    Returns: the total amount of money Ali has.
    """
    # L1
    num_five_dollar_bills = 7 # 7 bills of 5 dollars
    five_dollar_value = 5 # 5 dollars
    money_from_fives = num_five_dollar_bills * five_dollar_value

    # L2
    ten_dollar_bill_value = 10 # 1 bill of 10 dollars
    total_money = money_from_fives + ten_dollar_bill_value

    # FA
    answer = total_money
    return answer