def solve():
    """Index: 1214.
    Returns: the total number of animal legs.
    """
    # L1
    num_dogs = 2 # 2 dogs
    legs_per_dog = 4 # WK
    total_dog_legs = num_dogs * legs_per_dog

    # L2
    # The solution directly states "2 chicken legs" without showing the multiplication (1 chicken * 2 legs/chicken).
    # Therefore, '2' is treated as a direct value for substitution.
    chicken_legs_value = 2 # WK
    total_legs = total_dog_legs + chicken_legs_value

    # FA
    answer = total_legs
    return answer