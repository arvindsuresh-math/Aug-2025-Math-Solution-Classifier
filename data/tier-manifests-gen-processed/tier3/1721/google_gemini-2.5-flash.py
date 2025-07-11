def solve():
    """Index: 1721.
    Returns: the total weight of the dogs.
    """
    # L1
    evan_dog_weight = 63 # Evan’s dog weighs 63 pounds
    weight_multiple = 7 # it weighs 7 times as much as Ivan’s dog
    ivan_dog_weight = evan_dog_weight / weight_multiple

    # L2
    total_weight = evan_dog_weight + ivan_dog_weight

    # FA
    answer = total_weight
    return answer