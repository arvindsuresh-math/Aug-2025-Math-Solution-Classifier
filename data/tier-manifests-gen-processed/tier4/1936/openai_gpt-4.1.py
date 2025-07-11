def solve():
    """Index: 1936.
    Returns: the amount of money third place gets.
    """
    # L1
    num_friends = 7 # 7 friends
    josh = 1 # Josh himself
    num_people = num_friends + josh

    # L2
    dollars_per_person = 5 # 5 dollars into a pot
    total_pot = num_people * dollars_per_person

    # L3
    first_place_fraction = 0.8 # 80% of the money
    first_place_prize = total_pot * first_place_fraction

    # L4
    remaining_pot = total_pot - first_place_prize

    # L5
    split_places = 2 # second and third place split the rest
    third_place_prize = remaining_pot / split_places

    # FA
    answer = third_place_prize
    return answer