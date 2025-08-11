def solve():
    """Index: 1580.
    Returns: the number of red flowers Wilma has.
    """
    # L1
    num_rows = 6 # 6 rows
    flowers_per_row = 13 # 13 flowers in each row
    total_flowers_space = num_rows * flowers_per_row

    # L2
    green_multiplier = 2 # two times more green flowers
    yellow_flowers = 12 # 12 yellow flowers
    green_flowers = green_multiplier * yellow_flowers

    # L3
    red_flowers = total_flowers_space - green_flowers - yellow_flowers

    # FA
    answer = red_flowers
    return answer