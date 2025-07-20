def solve():
    """Index: 5944.
    Returns: the number of crops the farmer still has.
    """
    # L1
    num_corn_rows = 10 # 10 rows of corn stalks
    corn_cobs_per_row = 9 # 9 corn cobs each
    total_corn_cobs = num_corn_rows * corn_cobs_per_row

    # L2
    num_potato_rows = 5 # 5 rows of potatoes
    potatoes_per_row = 30 # 30 potatoes each
    total_potatoes = num_potato_rows * potatoes_per_row

    # L3
    total_initial_crops = total_corn_cobs + total_potatoes

    # L4
    destroyed_fraction = 0.5 # half of his crops
    remaining_crops = total_initial_crops * destroyed_fraction

    # FA
    answer = remaining_crops
    return answer