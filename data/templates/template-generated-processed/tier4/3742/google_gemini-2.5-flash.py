def solve():
    """Index: 3742.
    Returns: the price of one shirt.
    """
    # L1
    total_paid = 120 # 2 shirts and 3 pairs of pants for $120 in total
    refund_percent_num = 25 # refunded 25%
    percent_factor = 0.01 # WK
    refund_amount = refund_percent_num * percent_factor * total_paid

    # L2
    price_of_2_shirts = total_paid - refund_amount

    # L3
    num_shirts = 2 # 2 shirts
    price_of_1_shirt = price_of_2_shirts / num_shirts

    # FA
    answer = price_of_1_shirt
    return answer