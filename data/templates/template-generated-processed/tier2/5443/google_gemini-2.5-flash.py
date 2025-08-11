def solve():
    """Index: 5443.
    Returns: the total amount of candy Neil got.
    """
    # L1
    maggie_candy = 50 # who only collected 50 pieces
    harper_more_percent_num = 30 # 30% more pieces of Halloween candy
    harper_more_percent_decimal = 0.30 # from solution text: .30*50
    percent_factor = 0.01 # WK
    harper_more_candy = harper_more_percent_decimal * maggie_candy

    # L2
    harper_total_candy = maggie_candy + harper_more_candy

    # L3
    neil_more_percent_num = 40 # 40% more candy
    neil_more_percent_decimal = 0.40 # from solution text: .40*65
    neil_more_candy = neil_more_percent_decimal * harper_total_candy

    # L4
    neil_total_candy = harper_total_candy + neil_more_candy

    # FA
    answer = neil_total_candy
    return answer