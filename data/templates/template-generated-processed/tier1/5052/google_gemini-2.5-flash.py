def solve():
    """Index: 5052.
    Returns: the total number of questions Professor Oscar must review.
    """
    # L1
    questions_per_exam = 10 # 10 questions on each exam
    students_per_class = 35 # 35 students each
    questions_per_class = questions_per_exam * students_per_class

    # L2
    num_classes = 5 # 5 classes
    total_questions_reviewed = questions_per_class * num_classes

    # FA
    answer = total_questions_reviewed
    return answer