from fractions import Fraction

def solve():
    """Index: 4424.
    Returns: the total number of people wearing rabbit ears.
    """
    # L1
    female_percentage = Fraction(40, 100) # 40% of the guests are women
    total_guests = 200 # total number of guests at the party is 200
    female_guests = female_percentage * total_guests

    # L2
    female_rabbit_ears_percentage = Fraction(80, 100) # 80% of the women are wearing rabbit ears
    female_rabbit_ears = female_rabbit_ears_percentage * female_guests

    # L3
    male_guests = total_guests - female_guests

    # L4
    male_rabbit_ears_percentage = Fraction(60, 100) # 60% of the males are wearing rabbit ears
    male_rabbit_ears = male_rabbit_ears_percentage * male_guests

    # L5
    total_rabbit_ears = female_rabbit_ears + male_rabbit_ears

    # FA
    answer = total_rabbit_ears
    return answer