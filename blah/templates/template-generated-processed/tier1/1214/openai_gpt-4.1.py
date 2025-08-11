def solve():
    """Index: 1214.
    Returns: the total number of animal legs Adlai has in all.
    """
    # L1
    num_dogs = 2 # Adlai has 2 dogs
    legs_per_dog = 4 # dogs have 4 legs
    dog_legs = num_dogs * legs_per_dog

    # L2
    chicken_legs = 2 # 1 chicken (implied 2 legs per chicken)
    total_legs = dog_legs + chicken_legs

    # FA
    answer = total_legs
    return answer