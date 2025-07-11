def solve():
    """Index: 1944.
    Returns: the number of cans Yoki picked up.
    """
    # L1
    ladonna_cans = 25 # LaDonna picked up 25 cans

    # L2
    prikya_multiplier = 2 # Prikya picked up twice as many times as many cans as LaDonna
    prikya_cans = prikya_multiplier * ladonna_cans

    # L3
    total_cans = 85 # Eighty-five cans were collected
    yoki_cans = total_cans - ladonna_cans - prikya_cans

    # FA
    answer = yoki_cans
    return answer