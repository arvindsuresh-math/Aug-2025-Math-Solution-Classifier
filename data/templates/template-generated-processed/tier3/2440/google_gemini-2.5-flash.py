from fractions import Fraction

def solve():
    """Index: 2440.
    Returns: the number of tickets Finley gets.
    """
    # L1
    fraction_given_numerator = 3 # 3/4 of his 400 tickets
    fraction_given_denominator = 4 # 3/4 of his 400 tickets
    total_tickets = 400 # 400 tickets
    tickets_given_to_friends = Fraction(fraction_given_numerator, fraction_given_denominator) * total_tickets

    # L2
    jensen_ratio_part = 4 # share the tickets in a ratio of 4:11
    finley_ratio_part = 11 # share the tickets in a ratio of 4:11
    total_ratio_parts = jensen_ratio_part + finley_ratio_part

    # L3
    finley_tickets = Fraction(finley_ratio_part, total_ratio_parts) * tickets_given_to_friends

    # FA
    answer = finley_tickets
    return answer