from fractions import Fraction

def solve():
    """Index: 1213.
    Returns: the difference in correct answers between Lyssa and Precious.
    """
    # L1
    total_items = 75 # 75 items in the exam
    lyssa_incorrect_percentage = Fraction(20, 100) # 20% of the items incorrectly
    lyssa_mistakes = total_items * lyssa_incorrect_percentage

    # L2
    lyssa_score = total_items - lyssa_mistakes

    # L3
    precious_mistakes = 12 # Precious got 12 mistakes
    precious_score = total_items - precious_mistakes

    # L4
    difference_in_correct_answers = precious_score - lyssa_score

    # FA
    answer = difference_in_correct_answers
    return answer