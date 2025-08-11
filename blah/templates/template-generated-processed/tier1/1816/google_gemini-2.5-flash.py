def solve():
    """Index: 1816.
    Returns: the total number of legs' worth of organisms traveling together.
    """
    # L1
    num_humans = 2 # Johnny and his son
    legs_per_human = 2 # WK
    human_legs = num_humans * legs_per_human

    # L2
    num_dogs = 2 # two dogs
    legs_per_dog = 4 # WK
    dog_legs = num_dogs * legs_per_dog

    # L3
    total_legs = human_legs + dog_legs

    # FA
    answer = total_legs
    return answer