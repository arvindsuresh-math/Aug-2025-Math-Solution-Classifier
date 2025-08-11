from fractions import Fraction

def solve():
    """Index: 6671.
    Returns: the number of children who attended the party.
    """
    # L1
    total_attendees = 100 # One hundred people attended a party
    women_percentage = Fraction(50, 100) # Fifty percent of the attendees are women
    num_women = total_attendees * women_percentage

    # L2
    men_percentage = Fraction(35, 100) # thirty-five percent of them are men
    num_men = total_attendees * men_percentage

    # L3
    total_men_women = num_women + num_men

    # L4
    num_children = total_attendees - total_men_women

    # FA
    answer = num_children
    return answer