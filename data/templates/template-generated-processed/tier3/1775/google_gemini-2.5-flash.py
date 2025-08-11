def solve():
    """Index: 1775.
    Returns: the total number of squirrels counted by both students combined.
    """
    # L1
    first_student_count = 12 # counted 12 squirrels
    third_denominator = 3 # a third more squirrels
    additional_squirrels = first_student_count / third_denominator

    # L2
    second_student_count = first_student_count + additional_squirrels

    # L3
    total_squirrels = first_student_count + second_student_count

    # FA
    answer = total_squirrels
    return answer