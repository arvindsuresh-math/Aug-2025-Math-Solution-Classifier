from fractions import Fraction

def solve():
    """Index: 441.
    Returns: the total number of people Martin invited to his party.
    """
    # L1
    hometown_people = 5 # 5 people from his hometown
    school_multiplier = 2 # twice as many people from his school
    school_people = hometown_people * school_multiplier

    # L2
    sports_club_people = hometown_people + school_people

    # L3
    total_initial_invitations = hometown_people + school_people + sports_club_people

    # L4
    remaining_percentage = Fraction(20, 100) # 20% of the total previously mentioned
    remaining_invitations = remaining_percentage * total_initial_invitations

    # L5
    total_people_invited = total_initial_invitations + remaining_invitations

    # FA
    answer = total_people_invited
    return answer