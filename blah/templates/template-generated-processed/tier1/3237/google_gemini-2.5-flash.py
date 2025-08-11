def solve():
    """Index: 3237.
    Returns: the number of additional pancakes Luther must make.
    """
    # L1
    num_people = 8 # His family has 8 people
    pancakes_per_person_for_seconds = 2 # everyone to have a second pancake
    pancakes_needed_for_seconds = num_people * pancakes_per_person_for_seconds

    # L2
    pancakes_made_initially = 12 # Luther made 12 pancakes
    additional_pancakes_needed = pancakes_needed_for_seconds - pancakes_made_initially

    # FA
    answer = additional_pancakes_needed
    return answer