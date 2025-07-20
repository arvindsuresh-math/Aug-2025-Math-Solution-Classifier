from fractions import Fraction

def solve():
    """Index: 4862.
    Returns: the number of incorrect answers Rose had.
    """
    # L1
    total_items = 60 # In a 60-item exam
    liza_correct_percentage = Fraction(90, 100) # 90% of the items correctly
    liza_correct_answers = total_items * liza_correct_percentage

    # L2
    more_correct_answers_rose = 2 # got 2 more correct answers than her
    rose_correct_answers = liza_correct_answers + more_correct_answers_rose

    # L3
    rose_incorrect_answers = total_items - rose_correct_answers

    # FA
    answer = rose_incorrect_answers
    return answer