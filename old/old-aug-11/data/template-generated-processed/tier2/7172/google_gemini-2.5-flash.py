def solve():
    """Index: 7172.
    Returns: the number of candy bars Carl will be able to buy.
    """
    # L1
    weekly_pay = 0.75 # pay him $0.75 every week
    num_weeks = 4 # four weeks
    total_earnings = weekly_pay * num_weeks

    # L2
    candy_bar_cost = 0.50 # earned $0.50 he would go to the corner market and buy a candy bar
    num_candy_bars = total_earnings / candy_bar_cost

    # FA
    answer = num_candy_bars
    return answer