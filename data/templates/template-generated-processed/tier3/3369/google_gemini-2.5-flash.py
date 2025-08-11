from fractions import Fraction

def solve():
    """Index: 3369.
    Returns: the total number of berries they will be able to sell.
    """
    # L1
    blueberries = 30 # Iris picked 30 blueberries
    cranberries = 20 # her sister picked 20 cranberries
    raspberries = 10 # her brother was able to pick 10 raspberries
    total_picked_berries = blueberries + cranberries + raspberries

    # L2
    rotten_fraction = Fraction(1, 3) # 1/3 of the total berries they were able to pick are rotten
    rotten_berries = rotten_fraction * total_picked_berries

    # L3
    fresh_berries = total_picked_berries - rotten_berries

    # L4
    kept_fraction = Fraction(1, 2) # the remaining 1/2 of the fresh berries need to be kept
    berries_to_keep = kept_fraction * fresh_berries

    # L5
    berries_to_sell = fresh_berries - berries_to_keep

    # FA
    answer = berries_to_sell
    return answer