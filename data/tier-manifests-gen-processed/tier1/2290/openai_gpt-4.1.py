def solve():
    """Index: 2290.
    Returns: the total number of stickers Victor has.
    """
    # L1
    flower_stickers = 8 # Victor has 8 flower stickers
    fewer_animal_than_flower = 2 # He has 2 fewer animal stickers than flower stickers
    animal_stickers = flower_stickers - fewer_animal_than_flower

    # L2
    total_stickers = flower_stickers + animal_stickers

    # FA
    answer = total_stickers
    return answer