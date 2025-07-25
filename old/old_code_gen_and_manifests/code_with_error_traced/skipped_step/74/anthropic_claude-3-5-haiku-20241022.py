def solve(
    total_weight_loss: int = 103,  # Four people lost a total of 103 kilograms of weight
    first_person_loss: int = 27,   # The first person lost 27 kilograms
    second_person_difference: int = 7  # The second person lost 7 kilograms less than the first person
):
    """Index: 74.
    Returns: the amount of weight lost by each of the last two people."""

    #: L1
    second_person_loss = first_person_loss - second_person_difference # eval: 20 = 27 - 7

    #: L2
    remaining_weight_loss = total_weight_loss - first_person_loss - second_person_loss # eval: 56 = 103 - 27 - 20

    #: L3

    #: FA
    answer = total_weight_loss
    return answer # eval: return 103
