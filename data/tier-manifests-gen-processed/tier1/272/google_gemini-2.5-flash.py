def solve():
    """Index: 272.
    Returns: how much more money Oliver has than William.
    """
    # L1
    bill_value_oliver_20 = 20 # 20
    num_bills_oliver_20 = 10 # 10 $20
    oliver_total_20_bills = bill_value_oliver_20 * num_bills_oliver_20

    # L2
    bill_value_oliver_5 = 5 # 5
    num_bills_oliver_5 = 3 # 3 $5 bills
    oliver_total_5_bills = bill_value_oliver_5 * num_bills_oliver_5

    # L3
    oliver_total_money = oliver_total_20_bills + oliver_total_5_bills

    # L4
    bill_value_william_10 = 10 # 10
    num_bills_william_10 = 15 # 15 $10
    william_total_10_bills = bill_value_william_10 * num_bills_william_10

    # L5
    bill_value_william_5 = 5 # 5
    num_bills_william_5 = 4 # 4 $5 bills
    william_total_5_bills = bill_value_william_5 * num_bills_william_5

    # L6
    william_total_money = william_total_10_bills + william_total_5_bills

    # L7
    difference_in_money = oliver_total_money - william_total_money

    # FA
    answer = difference_in_money
    return answer