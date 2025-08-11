def solve():
    """Index: 4301.
    Returns: the total number of stocking stuffers Hannah buys.
    """
    # L1
    candy_canes_per_kid = 4 # 4 candy canes
    beanie_babies_per_kid = 2 # 2 beanie babies
    books_per_kid = 1 # 1 book
    stuffers_per_kid = candy_canes_per_kid + beanie_babies_per_kid + books_per_kid

    # L2
    num_kids = 3 # 3 kids
    total_stuffers = stuffers_per_kid * num_kids

    # FA
    answer = total_stuffers
    return answer