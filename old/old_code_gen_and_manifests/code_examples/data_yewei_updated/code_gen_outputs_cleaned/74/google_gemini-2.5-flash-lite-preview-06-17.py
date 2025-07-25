def solve(
    total_weight_lost: int = 103, # Four people lost a total of 103 kilograms of weight.
    weight_lost_person1: int = 27, # The first person lost 27 kilograms.
    weight_lost_person2_diff: int = 7, # The second person lost 7 kilograms less than the first person.
    num_people: int = 4 # Four people lost a total of 103 kilograms of weight.
):
    """Index: 74.
    Returns: the weight in kilograms lost by each of the last two people.
    """
    #: L1
    weight_lost_person2 = weight_lost_person1 - weight_lost_person2_diff

    #: L2
    weight_lost_remaining = total_weight_lost - weight_lost_person1 - weight_lost_person2

    #: L3
    weight_lost_last_two_each = weight_lost_remaining / 2

    #: L4
    answer = weight_lost_last_two_each # FINAL ANSWER
    return answer