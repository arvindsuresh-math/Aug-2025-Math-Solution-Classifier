from fractions import Fraction

def solve():
    """Index: 4832.
    Returns: Mandy's score.
    """
    # L1
    total_items = 100 # 100-item exam
    lowella_percentage = Fraction(35, 100) # 35% of the questions correctly
    lowella_score = total_items * lowella_percentage

    # L2
    pamela_additional_percentage = Fraction(20, 100) # 20% more correct answers
    pamela_additional_score = lowella_score * pamela_additional_percentage

    # L3
    pamela_score = lowella_score + pamela_additional_score

    # L4
    mandy_multiplier = 2 # twice Pamela's score
    mandy_score = pamela_score * mandy_multiplier

    # FA
    answer = mandy_score
    return answer