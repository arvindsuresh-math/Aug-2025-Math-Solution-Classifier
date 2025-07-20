def solve():
    """Index: 3837.
    Returns: the total number of bones in the original pile.
    """
    # L1
    first_dog_bones = 3 # The first dog carried off 3 bones
    second_dog_less_than_first = 1 # 1 less bone than the first dog
    second_dog_bones = first_dog_bones - second_dog_less_than_first

    # L2
    multiplier_for_twice = 2 # twice as many
    third_dog_bones = second_dog_bones * multiplier_for_twice

    # L3
    fourth_dog_bones = 1 # The fourth dog carried off one bone
    multiplier_for_fifth_dog = 2 # twice the number of bones
    fifth_dog_bones = multiplier_for_fifth_dog * fourth_dog_bones

    # L4
    total_bones = first_dog_bones + second_dog_bones + third_dog_bones + fourth_dog_bones + fifth_dog_bones

    # FA
    answer = total_bones
    return answer