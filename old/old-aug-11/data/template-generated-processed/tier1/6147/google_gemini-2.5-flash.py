def solve():
    """Index: 6147.
    Returns: the total number of feet in the garden.
    """
    # L1
    num_dogs = 6 # 6 dogs
    feet_per_dog = 4 # WK
    dog_feet = num_dogs * feet_per_dog

    # L2
    num_ducks = 2 # 2 ducks
    feet_per_duck = 2 # WK
    duck_feet = num_ducks * feet_per_duck

    # L3
    total_feet = dog_feet + duck_feet

    # FA
    answer = total_feet
    return answer