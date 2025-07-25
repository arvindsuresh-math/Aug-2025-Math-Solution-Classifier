def solve():
    """Index: 74.
    Returns: the weight lost by each of the last two people.
    """
    # L1
    first_person_loss = 27 # The first person lost 27 kilograms
    less_than_first = 7 # 7 kilograms less than the first person
    second_person_loss = first_person_loss - less_than_first

    # L2
    total_loss = 103 # lost a total of 103 kilograms
    remaining_loss = total_loss - first_person_loss - second_person_loss

    # L3
    num_remaining_people = 2 # The two remaining people
    loss_per_person = remaining_loss / num_remaining_people

    # FA
    answer = loss_per_person
    return answer