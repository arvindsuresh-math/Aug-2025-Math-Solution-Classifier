def solve():
    """Index: 3059.
    Returns: the average weight of all the dogs.
    """
    # L1
    brown_dog_weight = 4 # The brown dog weighs 4 pounds
    black_dog_weight_more = 1 # 1 pound more than the brown dog
    black_dog_weight = black_dog_weight_more + brown_dog_weight

    # L2
    white_dog_multiplier = 2 # weighs twice as much as the brown dog
    white_dog_weight = brown_dog_weight * white_dog_multiplier

    # L3
    grey_dog_weight_less = 2 # weighs 2 pounds less than the black dog
    grey_dog_weight = black_dog_weight - grey_dog_weight_less

    # L4
    total_weight = brown_dog_weight + black_dog_weight + white_dog_weight + grey_dog_weight

    # L5
    num_dogs = 4 # 4 different colored dogs
    average_weight = total_weight / num_dogs

    # FA
    answer = average_weight
    return answer