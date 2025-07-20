def solve():
    """Index: 3967.
    Returns: the number of unwilted flowers remaining.
    """
    # L1
    initial_dozens = 2 # two dozen roses
    roses_per_dozen = 12 # WK
    initial_roses = initial_dozens * roses_per_dozen

    # L2
    roses_after_trade = roses_per_dozen + initial_roses

    # L3
    wilt_divisor_day1 = 2 # half of the roses wilted
    roses_after_day1_wilt = roses_after_trade / wilt_divisor_day1

    # L4
    wilt_divisor_day2 = 2 # another half of the remaining flowers wilted
    unwilted_roses_remaining = roses_after_day1_wilt / wilt_divisor_day2

    # FA
    answer = unwilted_roses_remaining
    return answer