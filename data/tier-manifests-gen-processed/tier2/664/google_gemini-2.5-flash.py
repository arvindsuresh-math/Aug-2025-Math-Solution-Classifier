def solve():
    """Index: 664.
    Returns: how long a fish can live.
    """
    # L1
    dog_hamster_ratio = 4 # dogs live 4 times as long as hamsters live
    hamster_lifespan = 2.5 # hamsters live an average of 2.5 years
    dog_lifespan = dog_hamster_ratio * hamster_lifespan

    # L2
    fish_dog_difference = 2 # fish can live 2 years longer than dogs live
    fish_lifespan = dog_lifespan + fish_dog_difference

    # FA
    answer = fish_lifespan
    return answer