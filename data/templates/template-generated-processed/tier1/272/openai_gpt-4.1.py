def solve():
    """Index: 272.
    Returns: how much more money Oliver has than William.
    """
    # L1
    oliver_num_20 = 10 # Oliver has 10 $20 bills
    bill_20 = 20 # $20 bills
    oliver_20_total = bill_20 * oliver_num_20

    # L2
    oliver_num_5 = 3 # Oliver has 3 $5 bills
    bill_5 = 5 # $5 bills
    oliver_5_total = bill_5 * oliver_num_5

    # L3
    oliver_total = oliver_20_total + oliver_5_total

    # L4
    william_num_10 = 15 # William has 15 $10 bills
    bill_10 = 10 # $10 bills
    william_10_total = bill_10 * william_num_10

    # L5
    william_num_5 = 4 # William has 4 $5 bills
    william_5_total = bill_5 * william_num_5

    # L6
    william_total = william_10_total + william_5_total

    # L7
    difference = oliver_total - william_total

    # FA
    answer = difference
    return answer