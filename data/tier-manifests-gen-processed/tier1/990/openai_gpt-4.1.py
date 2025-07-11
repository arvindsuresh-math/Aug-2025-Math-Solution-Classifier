def solve():
    """Index: 990.
    Returns: the total amount of money Grace earned in September.
    """
    # L1
    mow_hours = 63 # mowed lawns for 63 hours
    mow_rate = 6 # $6 an hour for mowing lawns
    mow_earnings = mow_hours * mow_rate

    # L2
    weed_hours = 9 # pulled weeds for 9 hours
    weed_rate = 11 # $11 for pulling weeds
    weed_earnings = weed_hours * weed_rate

    # L3
    mulch_hours = 10 # put down mulch for 10 hours
    mulch_rate = 9 # $9 for putting down mulch
    mulch_earnings = mulch_hours * mulch_rate

    # L4
    total_earnings = mow_earnings + weed_earnings + mulch_earnings

    # FA
    answer = total_earnings
    return answer