def solve():
    """Index: 1297.
    Returns: the number of students who have both puppies and parrots.
    """
    # L1
    total_students = 40 # there are 40 students
    puppy_percent = 0.8 # 80 percent have puppies
    students_with_puppies = total_students * puppy_percent

    # L2
    parrot_percent = 0.25 # 25% also have parrots
    students_with_both = students_with_puppies * parrot_percent

    # FA
    answer = students_with_both
    return answer