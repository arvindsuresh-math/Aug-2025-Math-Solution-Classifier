from fractions import Fraction

def solve():
    """Index: 4370.
    Returns: the target number of apples they had to pick.
    """
    # L1
    number_of_people = 2 # WK
    apples_per_person_first_round = 400 # After picking 400 apples each
    total_apples_first_round = number_of_people * apples_per_person_first_round

    # L2
    fraction_second_round = Fraction(3, 4) # 3/4 times as many as they had picked earlier
    apples_per_person_second_round = fraction_second_round * apples_per_person_first_round

    # L3
    total_apples_second_round = number_of_people * apples_per_person_second_round

    # L4
    total_apples_picked_so_far = total_apples_first_round + total_apples_second_round

    # L5
    apples_needed_per_person = 600 # still needed to pick 600 apples each
    total_apples_still_needed = number_of_people * apples_needed_per_person

    # L6
    target_apples = total_apples_still_needed + total_apples_picked_so_far

    # FA
    answer = target_apples
    return answer