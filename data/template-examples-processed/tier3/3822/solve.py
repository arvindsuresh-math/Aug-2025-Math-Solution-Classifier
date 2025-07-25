def solve():
    """Index: 3822.
    Returns: the number of additional votes Alec needs.
    """
    # L1
    total_students = 60 # Alec's class has 60 students
    goal_denominator = 4 # three-quarters of the class
    one_quarter_of_class = total_students / goal_denominator

    # L2
    goal_numerator = 3 # three-quarters of the class
    goal_votes = one_quarter_of_class * goal_numerator

    # L3
    initial_committed_denominator = 2 # Half of the class
    initial_committed_votes = total_students / initial_committed_denominator

    # L4
    thinking_about_it = 5 # only 5 have said they are thinking
    votes_after_thinking = initial_committed_votes + thinking_about_it

    # L5
    students_not_voting_for_alec = total_students - votes_after_thinking

    # L6
    converted_denominator = 5 # a fifth of these students
    newly_converted_votes = students_not_voting_for_alec / converted_denominator

    # L7
    total_actual_votes = votes_after_thinking + newly_converted_votes

    # L8
    votes_still_needed = goal_votes - total_actual_votes

    # FA
    answer = votes_still_needed
    return answer