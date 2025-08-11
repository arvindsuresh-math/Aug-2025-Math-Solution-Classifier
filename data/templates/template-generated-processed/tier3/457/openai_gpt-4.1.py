def solve():
    """Index: 457.
    Returns: the total number of math questions all three girls completed in 2 hours.
    """
    # L1
    fiona_questions = 36 # Fiona completed 36 math questions in an hour
    shirley_multiplier = 2 # Shirley was able to complete twice as many
    shirley_questions = fiona_questions * shirley_multiplier

    # L2
    sum_fiona_shirley = fiona_questions + shirley_questions

    # L3
    kiana_divisor = 2 # Kiana completed half of the sum
    kiana_questions = sum_fiona_shirley / kiana_divisor

    # L4
    total_one_hour = sum_fiona_shirley + kiana_questions

    # L5
    total_hours = 2 # they each did the same number of questions the following hour
    total_two_hours = total_one_hour * total_hours

    # FA
    answer = total_two_hours
    return answer