def solve():
    """Index: 3680.
    Returns: the total number of genuine purses and handbags.
    """
    # L1
    total_purses = 26 # 26 purses
    genuine_purse_divisor = 2 # Half the purses
    genuine_purses = total_purses / genuine_purse_divisor

    # L2
    total_handbags = 24 # 24 handbags
    fake_handbag_divisor = 4 # 1/4 the handbags are fake
    fake_handbags = total_handbags / fake_handbag_divisor

    # L3
    genuine_handbags = total_handbags - fake_handbags

    # L4
    total_genuine_items = genuine_purses + genuine_handbags

    # FA
    answer = total_genuine_items
    return answer