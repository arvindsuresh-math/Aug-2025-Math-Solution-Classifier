def solve():
    """Index: 6629.
    Returns: the total number of questions Cameron answered.
    """
    # L1
    questions_per_tourist = 2 # two questions per tourist
    first_group_size = 6 # first group was only 6 people
    questions_first_group = questions_per_tourist * first_group_size

    # L2
    second_group_size = 11 # following group was a busy group of 11
    questions_second_group = questions_per_tourist * second_group_size

    # L3
    third_group_size = 8 # The third group had 8 people
    inquisitive_tourist_count = 1 # one was inquisitive
    normal_tourists_third_group = third_group_size - inquisitive_tourist_count

    # L4
    inquisitive_multiplier = 3 # asked three times as many questions as usual
    questions_inquisitive_tourist = inquisitive_tourist_count * questions_per_tourist * inquisitive_multiplier

    # L5
    normal_tourists_third_group_subtotal = normal_tourists_third_group * questions_per_tourist
    questions_third_group = normal_tourists_third_group_subtotal + questions_inquisitive_tourist

    # L6
    last_group_size = 7 # last group of the day was a late group of 7
    questions_last_group = last_group_size * questions_per_tourist

    # L7
    total_questions = questions_first_group + questions_second_group + questions_third_group + questions_last_group

    # FA
    answer = total_questions
    return answer