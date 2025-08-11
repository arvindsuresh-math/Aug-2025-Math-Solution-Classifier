def solve():
    """Index: 5602.
    Returns: the number of more cats than dogs Carmen has now.
    """
    # L1
    initial_cats = 28 # 28 cats
    cats_given_up = 3 # gave 3 of the cats up for adoption
    remaining_cats = initial_cats - cats_given_up

    # L2
    num_dogs = 18 # 18 dogs
    difference_cats_dogs = remaining_cats - num_dogs

    # FA
    answer = difference_cats_dogs
    return answer