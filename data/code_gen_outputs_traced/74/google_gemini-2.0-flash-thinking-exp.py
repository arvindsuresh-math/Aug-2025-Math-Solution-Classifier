def solve(
    num_people: int = 4, # Four people
    total_weight_lost: int = 103, # lost a total of 103 kilograms
    weight_lost_person1: int = 27, # The first person lost 27 kilograms
    weight_diff_person2: int = 7, # The second person lost 7 kilograms less than the first person
    num_remaining_people: int = 2 # The two remaining people
):
    """Index: 74.
    Returns: the number of kilograms each of the last two people lost.
    """

    #: L1
    weight_lost_person2 = weight_lost_person1 - weight_diff_person2 # eval: 20 = 27 - 7

    #: L2
    weight_lost_remaining = total_weight_lost - weight_lost_person1 - weight_lost_person2 # eval: 56 = 103 - 27 - 20

    #: L3
    weight_lost_each_remaining = weight_lost_remaining / num_remaining_people # eval: 28.0 = 56 / 2

    #: FA
    answer = weight_lost_each_remaining
    return answer # eval: return 28.0
