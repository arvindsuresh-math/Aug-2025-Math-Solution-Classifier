from fractions import Fraction

def solve():
    """Index: 3174.
    Returns: the difference in the number of women and men who stayed at the party.
    """
    # L1
    women_attendees = 30 # 30 women
    men_attendees = 20 # 20 men
    total_attendees = women_attendees + men_attendees

    # L2
    fraction_left = Fraction(2, 5) # 2/5 of the total number of people left
    people_left = total_attendees * fraction_left

    # L3
    men_left = 9 # 9 men left the party
    women_left = people_left - men_left

    # L4
    women_stayed = women_attendees - women_left

    # L5
    men_stayed = men_attendees - men_left

    # L6
    women_more_than_men = women_stayed - men_stayed

    # FA
    answer = women_more_than_men
    return answer