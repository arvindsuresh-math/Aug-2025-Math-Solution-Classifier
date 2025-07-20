def solve():
    """Index: 5177.
    Returns: the difference in correct answers between Sergio and Sylvia.
    """
    # L1
    total_questions = 50 # 50 questions
    sylvia_incorrect_fraction_denominator = 5 # one-fifth of incorrect answers
    sylvia_incorrect_answers = total_questions / sylvia_incorrect_fraction_denominator

    # L2
    sylvia_correct_answers = total_questions - sylvia_incorrect_answers

    # L3
    sergio_mistakes = 4 # Sergio got 4 mistakes
    sergio_correct_answers = total_questions - sergio_mistakes

    # L4
    difference_in_correct_answers = sergio_correct_answers - sylvia_correct_answers

    # FA
    answer = difference_in_correct_answers
    return answer