def solve(
    total_weight_lost: int = 103,  # Four people lost a total of 103 kilograms of weight
    first_person_loss: int = 27,   # The first person lost 27 kilograms
    difference_second_first: int = 7  # The second person lost 7 kilograms less than the first person
):
    """Index: 74.
    Returns: the kilograms lost by each of the last two people.
    """
    #: L1
    second_person_loss = first_person_loss - difference_second_first # eval: 20 = 27 - 7
    #: L2
    remaining_weight_loss = total_weight_lost - first_person_loss - second_person_loss # eval: 56 = 103 - 27 - 20
    #: L3
    last_two_each_loss = remaining_weight_loss / 2 # eval: 28.0 = 56 / 2
    answer = last_two_each_loss  # FINAL ANSWER # eval: 28.0 = 28.0  # FINAL ANSWER
    return answer # eval: return 28.0