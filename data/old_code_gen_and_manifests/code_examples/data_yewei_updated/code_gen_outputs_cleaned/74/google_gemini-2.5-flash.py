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
    second_person_lost = first_person_lost - second_person_less_than_first

    #: L2
    remaining_weight_for_last_two = total_weight_lost - first_person_lost - second_person_lost

    #: L3
    weight_per_last_person = remaining_weight_for_last_two / 2

    #: L4
    # The last two people each lost 28 kilograms of weight. (This is a descriptive line, not a calculation)

    answer = weight_per_last_person # FINAL ANSWER
    return answer