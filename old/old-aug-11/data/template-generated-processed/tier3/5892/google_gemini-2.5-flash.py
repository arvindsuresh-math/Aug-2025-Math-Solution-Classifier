from fractions import Fraction

def solve():
    """Index: 5892.
    Returns: the total number of children involved in the cleaning event.
    """
    # L1
    men_percentage = Fraction(30, 100) # 30% were adult men
    total_community_members = 2000 # Out of 2000 community members
    adult_men = men_percentage * total_community_members

    # L2
    women_multiplier = 2 # twice as many adult women
    adult_women = women_multiplier * adult_men

    # L3
    total_adults = adult_women + adult_men

    # L4
    children = total_community_members - total_adults

    # FA
    answer = children
    return answer