def solve():
    """Index: 664.
    Returns: the number of years a well-cared fish can live.
    """
    # L1
    dog_to_hamster_ratio = 4 # dogs live 4 times as long as hamsters
    hamster_lifespan = 2.5 # hamsters live an average of 2.5 years
    dog_lifespan = dog_to_hamster_ratio * hamster_lifespan

    # L2
    fish_lifespan_bonus = 2 # fish can live 2 years longer than dogs
    fish_lifespan = dog_lifespan + fish_lifespan_bonus

    # FA
    answer = fish_lifespan
    return answer