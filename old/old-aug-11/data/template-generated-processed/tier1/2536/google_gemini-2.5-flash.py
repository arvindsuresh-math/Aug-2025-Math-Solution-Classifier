def solve():
    """Index: 2536.
    Returns: the total money Tina earned.
    """
    # L1
    days_worked = 6 # for 6 days
    postcards_per_day = 30 # make 30 such postcards
    total_postcards_made = days_worked * postcards_per_day

    # L2
    price_per_postcard = 5 # gets $5
    total_money_earned = total_postcards_made * price_per_postcard

    # FA
    answer = total_money_earned
    return answer