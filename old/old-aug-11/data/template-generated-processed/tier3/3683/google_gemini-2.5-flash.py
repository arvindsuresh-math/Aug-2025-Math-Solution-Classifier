from fractions import Fraction

def solve():
    """Index: 3683.
    Returns: the number of girls at the party.
    """
    # L1
    total_people = 50 # 50 people
    boys_percentage = Fraction(30, 100) # 30% of them are boys
    num_boys = total_people * boys_percentage

    # L2
    num_girls = total_people - num_boys

    # FA
    answer = num_girls
    return answer