def solve():
    """Index: 74.
    Returns: the number of kilograms each of the last two people lost.
    """
    # L1
    first_person_loss = 27 # The first person lost 27 kilograms
    second_person_difference = 7 # The second person lost 7 kilograms less than the first person
    second_person_loss = first_person_loss - second_person_difference

    # L2
    total_loss = 103 # Four people lost a total of 103 kilograms
    remaining_loss = total_loss - first_person_loss - second_person_loss

    # L3
    remaining_people = 2 # The two remaining people lost the same amount
    each_last_person_loss = remaining_loss / remaining_people

    # FA
    answer = each_last_person_loss
    return answer