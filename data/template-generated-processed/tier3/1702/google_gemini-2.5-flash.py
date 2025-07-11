from fractions import Fraction

def solve():
    """Index: 1702.
    Returns: the number of female guests who attended the party.
    """
    # L1
    total_guests = 60 # total number of guests were 60
    male_fraction = Fraction(2, 3) # 2/3 were male guests
    num_males = male_fraction * total_guests

    # L2
    num_females = total_guests - num_males

    # FA
    answer = num_females
    return answer