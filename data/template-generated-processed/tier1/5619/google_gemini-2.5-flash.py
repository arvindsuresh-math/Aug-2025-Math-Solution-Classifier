def solve():
    """Index: 5619.
    Returns: the amount of money Jack will be handing in.
    """
    # L1
    num_100_bills = 2 # 2 $100 bills
    denomination_100 = 100 # WK
    num_50_bills = 1 # 1 $50 bill
    denomination_50 = 50 # WK
    num_20_bills = 5 # 5 $20 bills
    denomination_20 = 20 # WK
    num_10_bills = 3 # 3 $10 bills
    denomination_10 = 10 # WK
    num_5_bills = 7 # 7 $5 bills
    denomination_5 = 5 # WK
    num_1_bills = 27 # 27 $1 bills
    denomination_1 = 1 # WK
    value_100 = num_100_bills * denomination_100
    value_50 = num_50_bills * denomination_50
    value_20 = num_20_bills * denomination_20
    value_10 = num_10_bills * denomination_10
    value_5 = num_5_bills * denomination_5
    value_1 = num_1_bills * denomination_1
    total_bills_value = value_100 + value_50 + value_20 + value_10 + value_5 + value_1

    # L2
    amount_to_leave = 300 # leave $300 in notes
    amount_to_hand_in = total_bills_value - amount_to_leave

    # FA
    answer = amount_to_hand_in
    return answer