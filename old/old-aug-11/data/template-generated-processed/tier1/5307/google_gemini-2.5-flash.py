def solve():
    """Index: 5307.
    Returns: the number of legs a spider has.
    """
    # L1
    human_legs = 2 # two legs
    double_factor = 2 # double the number
    doubled_human_legs = human_legs * double_factor

    # L2
    times_more_factor = 2 # two times more than
    spider_legs = doubled_human_legs * times_more_factor

    # FA
    answer = spider_legs
    return answer