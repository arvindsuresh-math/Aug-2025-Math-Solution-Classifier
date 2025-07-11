def solve():
    """Index: 2654.
    Returns: the number of apples each person will get.
    """
    # L1
    total_apples = 55 # Jack bought 55 apples
    apples_for_father = 10 # give 10 to his father
    remaining_apples = total_apples - apples_for_father

    # L2
    number_of_people_sharing = 5 # him and his 4 friends
    apples_per_person = remaining_apples / number_of_people_sharing

    # FA
    answer = apples_per_person
    return answer