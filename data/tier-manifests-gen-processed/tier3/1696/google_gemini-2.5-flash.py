def solve():
    """Index: 1696.
    Returns: the amount one of the friends will pay.
    """
    # L1
    total_bill = 150 # The dinner bill for 6 friends came to $150
    silas_share_divisor = 2 # half of the bill
    silas_paid = total_bill / silas_share_divisor

    # L2
    tip_percentage_value = 10 # 10% tip
    percentage_divisor = 100 # WK
    tip_amount = (tip_percentage_value / percentage_divisor) * total_bill
    remaining_bill_with_tip = silas_paid + tip_amount

    # L3
    friends_to_split = 5 # the remaining friends could split the rest of the bill
    cost_per_friend = remaining_bill_with_tip / friends_to_split

    # L4
    # FA
    answer = cost_per_friend
    return answer