def solve():
    """Index: 6316.
    Returns: the total amount received by the hundred students.
    """
    # L1
    total_winnings = 155250 # $155250 in the lottery
    fraction_given_divisor = 1000 # one-thousandth
    amount_per_student = total_winnings / fraction_given_divisor

    # L2
    num_students = 100 # top 100 students
    total_amount_received = amount_per_student * num_students

    # FA
    answer = total_amount_received
    return answer