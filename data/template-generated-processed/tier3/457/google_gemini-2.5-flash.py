def solve():
    """Index: 457.
    Returns: the total number of math questions completed by all three girls in 2 hours.
    """
    # L1
    fiona_questions = 36 # Fiona completed 36 math questions
    shirley_multiplier = 2 # twice as many math questions
    shirley_questions = fiona_questions * shirley_multiplier

    # L2
    fiona_shirley_sum = fiona_questions + shirley_questions

    # L3
    kiana_divisor = 2 # half of the sum
    kiana_questions = fiona_shirley_sum / kiana_divisor

    # L4
    total_questions_one_hour = fiona_shirley_sum + kiana_questions

    # L5
    hours = 2 # in 2 hours
    total_questions_two_hours = total_questions_one_hour * hours

    # FA
    answer = total_questions_two_hours
    return answer