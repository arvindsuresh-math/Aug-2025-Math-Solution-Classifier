def solve():
    """Index: 1944.
    Returns: the number of cans Yoki picked up.
    """
    # L1
    ladonna_cans = 25 # LaDonna picked up 25 cans.

    # L2
    multiplier_prikya = 2 # twice as many times as many cans as LaDonna
    prikya_cans = multiplier_prikya * ladonna_cans

    # L3
    total_cans_collected = 85 # Eighty-five cans were collected.
    yoki_cans = total_cans_collected - ladonna_cans - prikya_cans

    # FA
    answer = yoki_cans
    return answer