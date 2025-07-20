def solve():
    """Index: 3417.
    Returns: the percentage of all kittens with blue eyes.
    """
    # L1
    first_cat_blue_eyed_kittens = 3 # 3 blue-eyed kittens
    second_cat_blue_eyed_kittens = 4 # 4 blue-eyed kittens
    total_blue_eyed_kittens = first_cat_blue_eyed_kittens + second_cat_blue_eyed_kittens

    # L2
    first_cat_brown_eyed_kittens = 7 # 7 brown-eyed kittens
    second_cat_brown_eyed_kittens = 6 # 6 brown-eyed kittens
    total_brown_eyed_kittens = first_cat_brown_eyed_kittens + second_cat_brown_eyed_kittens

    # L3
    total_kittens = total_blue_eyed_kittens + total_brown_eyed_kittens

    # L4
    percentage_multiplier = 100 # 100%
    percentage_blue_eyed = (total_blue_eyed_kittens / total_kittens) * percentage_multiplier

    # FA
    answer = percentage_blue_eyed
    return answer