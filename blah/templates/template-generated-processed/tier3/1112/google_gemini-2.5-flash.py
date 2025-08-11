def solve():
    """Index: 1112.
    Returns: the number of blueberries picked.
    """
    # L1
    total_berries = 42 # 42 raspberries, blackberries, and blueberries were picked in total
    raspberry_divisor = 2 # half of all the berries
    raspberries_picked = total_berries / raspberry_divisor

    # L2
    blackberry_divisor = 3 # a third of the berries
    blackberries_picked = total_berries / blackberry_divisor

    # L3
    total_raspberries_blackberries = raspberries_picked + blackberries_picked

    # L4
    blueberries_picked = total_berries - total_raspberries_blackberries

    # FA
    answer = blueberries_picked
    return answer