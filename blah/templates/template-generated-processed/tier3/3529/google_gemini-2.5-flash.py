from fractions import Fraction

def solve():
    """Index: 3529.
    Returns: the number of people who did not support either team.
    """
    # L1
    total_attendees = 50 # a total of 50 people attended
    first_team_percentage_from_solution = Fraction(60, 100) # 60/100
    first_team_supporters = total_attendees * first_team_percentage_from_solution

    # L2
    second_team_percentage = Fraction(34, 100) # thirty-four percent of the audiences are supporters of the second teams
    second_team_supporters = total_attendees * second_team_percentage

    # L3
    total_supporters = first_team_supporters + second_team_supporters

    # L4
    non_supporters = total_attendees - total_supporters

    # FA
    answer = non_supporters
    return answer