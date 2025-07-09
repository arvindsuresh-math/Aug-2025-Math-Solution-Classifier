def solve(
        num_people: int = 4, # Four people
        total_weight_lost: int = 103, # lost a total of 103 kilograms of weight
        first_person_lost: int = 27, # The first person lost 27 kilograms
        second_person_less_than_first: int = 7 # The second person lost 7 kilograms less than the first person
    ):
    """Index: 74.
    Returns: the number of kilograms each of the last two people lost.
    """

    #: L1
    second_person_lost = first_person_lost + second_person_less_than_first # eval: 34 = 27 + 7

    #: L2
    remaining_weight_lost = total_weight_lost - first_person_lost - second_person_lost # eval: 42 = 103 - 27 - 34

    #: L3
    weight_per_last_person = remaining_weight_lost / 2 # eval: 21.0 = 42 / 2

    #: FA
    answer = weight_per_last_person
    return answer # eval: return 21.0
