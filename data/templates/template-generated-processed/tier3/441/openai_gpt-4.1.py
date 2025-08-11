from fractions import Fraction

def solve():
    """Index: 441.
    Returns: the total number of people Martin invited to his party.
    """
    # L1
    hometown_invited = 5 # 5 people from his hometown
    school_multiplier = 2 # twice as many people from his school
    school_invited = hometown_invited * school_multiplier

    # L2
    sports_club_invited = hometown_invited + school_invited

    # L3
    total_main_invited = hometown_invited + school_invited + sports_club_invited

    # L4
    other_percentage = Fraction(20, 100) # 20% of the total previously mentioned
    other_invited = other_percentage * total_main_invited

    # L5
    total_invited = total_main_invited + other_invited

    # FA
    answer = total_invited
    return answer