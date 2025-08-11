def solve():
    """Index: 5584.
    Returns: the number of people who said they are voting for Marty.
    """
    # L1
    biff_percent = 45 # 45% of the people polled said they were voting for Biff
    undecided_percent = 8 # 8% were undecided
    not_marty_percent = biff_percent + undecided_percent

    # L2
    total_percent = 100 # WK
    marty_percent_value = total_percent - not_marty_percent

    # L3
    total_people_polled = 200 # If 200 people were polled
    marty_percent_decimal = 0.47 # from solution text: 0.47 x 200
    num_voting_for_marty = marty_percent_decimal * total_people_polled

    # FA
    answer = num_voting_for_marty
    return answer