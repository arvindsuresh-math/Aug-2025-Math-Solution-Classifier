def solve(
        fraction_needed_to_win: float = 3/4,  # f he can get three-quarters of the class to vote for him then there is no chance anyone else can beat him.
        fraction_voting_for_him: float = 1/2,  # Half of the class have already said they will vote for him
        students_thinking_about_it: int = 5,  # only 5 have said they are thinking about voting for him
        total_students: int = 60  # Alec's class has 60 students
):    
    """Index: 3822.
    Returns: the number of votes by which Alec is short of his goal.
    """
    #: L1
    students_per_quarter = total_students / 4

    #: L2
    votes_needed = students_per_quarter * 3

    #: L3
    votes_for_him = total_students * fraction_voting_for_him

    #: L4
    votes_so_far = votes_for_him + students_thinking_about_it

    #: L5
    students_not_voting_for_him = total_students - votes_so_far
    
    #: L6
    new_votes = students_not_voting_for_him / 5

    #: L7
    total_votes_for_him = votes_so_far + new_votes

    #: L8
    votes_short_of_goal = votes_needed - total_votes_for_him

    answer = votes_short_of_goal  # FINAL ANSWER
    return answer