from fractions import Fraction

def solve():
    """Index: 4959.
    Returns: the number of additional questions Meryll needs to write.
    """
    # L1
    total_mc_questions = 35 # 35 multiple-choice questions
    mc_written_fraction = Fraction(2, 5) # 2/5 of the multiple-choice
    mc_written = total_mc_questions * mc_written_fraction

    # L2
    total_ps_questions = 15 # 15 problem-solving questions
    ps_written_fraction = Fraction(1, 3) # 1/3 of the problem-solving questions
    ps_written = total_ps_questions * ps_written_fraction

    # L3
    total_questions_to_write = total_mc_questions + total_ps_questions

    # L4
    total_questions_written = mc_written + ps_written

    # L5
    questions_needed_more = total_questions_to_write - total_questions_written

    # FA
    answer = questions_needed_more
    return answer