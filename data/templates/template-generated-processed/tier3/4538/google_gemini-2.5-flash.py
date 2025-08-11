def solve():
    """Index: 4538.
    Returns: the total number of dog paws on the ground.
    """
    # L1
    total_dogs = 12 # 12 dogs on stage
    half_divisor = 2 # Half of the dogs
    dogs_on_back_legs = total_dogs / half_divisor

    # L2
    paws_per_back_standing_dog = 2 # A dog has 2 back legs
    paws_from_back_standing_dogs = paws_per_back_standing_dog * dogs_on_back_legs

    # L3
    paws_per_all_four_standing_dog = 4 # all 4 legs
    paws_from_all_four_standing_dogs = dogs_on_back_legs * paws_per_all_four_standing_dog

    # L4
    total_paws_on_ground = paws_from_back_standing_dogs + paws_from_all_four_standing_dogs

    # FA
    answer = total_paws_on_ground
    return answer