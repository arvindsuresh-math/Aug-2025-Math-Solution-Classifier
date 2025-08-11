def solve():
    """Index: 837.
    Returns: the number of dogs Mariel is walking.
    """
    # L1
    num_dog_walkers = 2 # WK
    legs_per_walker = 2 # WK
    walker_legs = num_dog_walkers * legs_per_walker

    # L2
    other_walker_dogs = 3 # their 3 dogs
    legs_per_dog = 4 # WK
    other_dogs_legs = other_walker_dogs * legs_per_dog

    # L3
    total_known_legs = walker_legs + other_dogs_legs

    # L4
    total_tangled_legs = 36 # 36 legs tangled up in leashes
    mariel_dogs_legs = total_tangled_legs - total_known_legs

    # L5
    mariel_dogs_count = mariel_dogs_legs / legs_per_dog

    # FA
    answer = mariel_dogs_count
    return answer