def solve():
    """Index: 6050.
    Returns: the total number of pairs of leggings Haleigh needs.
    """
    # L1
    num_dogs = 4 # 4 dogs
    legs_per_dog = 4 # WK
    total_dog_legs = num_dogs * legs_per_dog

    # L2
    num_cats = 3 # 3 cats
    legs_per_cat = 4 # WK
    total_cat_legs = legs_per_cat * num_cats

    # L3
    total_legs = total_dog_legs + total_cat_legs

    # L4
    legs_per_pair = 2 # WK
    pairs_of_leggings = total_legs / legs_per_pair

    # FA
    answer = pairs_of_leggings
    return answer