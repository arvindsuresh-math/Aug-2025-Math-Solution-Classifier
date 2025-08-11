def solve():
    """Index: 5707.
    Returns: the price Max needs to set for each yellow stamp.
    """
    # L1
    num_red_stamps = 20 # 20 red stamps
    price_red_stamp = 1.1 # $1.1 for each stamp
    earnings_red_stamps = num_red_stamps * price_red_stamp

    # L2
    num_blue_stamps = 80 # 80 blue stamps
    price_blue_stamp = 0.8 # $0.8 for each stamp
    earnings_blue_stamps = num_blue_stamps * price_blue_stamp

    # L3
    current_earnings = earnings_red_stamps + earnings_blue_stamps

    # L4
    target_total_earnings = 100 # total of $100
    needed_more_earnings = target_total_earnings - current_earnings

    # L5
    num_yellow_stamps = 7 # 7 yellow ones
    price_yellow_stamp = needed_more_earnings / num_yellow_stamps

    # FA
    answer = price_yellow_stamp
    return answer