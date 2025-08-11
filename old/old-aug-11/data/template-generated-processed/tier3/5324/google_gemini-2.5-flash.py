def solve():
    """Index: 5324.
    Returns: the total sum of money shared by Parker and Richie.
    """
    # L1
    parker_share = 50 # Parker got $50
    parker_ratio = 2 # ratio 2:3
    unit_share = parker_share / parker_ratio

    # L2
    richie_ratio = 3 # ratio 2:3
    richie_share = richie_ratio * unit_share

    # L3
    total_shared_money = parker_share + richie_share

    # FA
    answer = total_shared_money
    return answer