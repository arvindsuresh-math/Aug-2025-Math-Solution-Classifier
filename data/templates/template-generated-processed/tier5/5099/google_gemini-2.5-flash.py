def solve():
    """Index: 5099.
    Returns: the number of cats taken in by the shelter.
    """
    # L3
    total_animals = 60 # total number of animals is c + d = 60
    cats_more_than_dogs = 20 # 20 more cats than dogs, subtracting 20 from both sides
    multiplier_for_dogs = 2 # 2d
    two_times_dogs = total_animals - cats_more_than_dogs

    # L4
    divisor_for_dogs = 2 # Dividing both sides by 2
    num_dogs = two_times_dogs / divisor_for_dogs

    # L5
    num_cats = cats_more_than_dogs + num_dogs

    # FA
    answer = num_cats
    return answer