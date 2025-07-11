def solve():
    """Index: 1541.
    Returns: the number of bunches if 12 flowers were in each bunch.
    """
    # L1
    bunches_count = 8 # 8 bunches of flowers
    flowers_per_bunch = 9 # 9 flowers in each bunch
    total_flowers = bunches_count * flowers_per_bunch

    # L2
    new_flowers_per_bunch = 12 # 12 flowers in each bunch
    new_bunches_count = total_flowers / new_flowers_per_bunch

    # FA
    answer = new_bunches_count
    return answer