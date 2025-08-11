def solve():
    """Index: 1297.
    Returns: the number of students who have both puppies and parrots.
    """
    # L1
    total_students = 40 # 40 students
    puppy_owners_percent_decimal = 0.8 # 80 percent have puppies
    students_with_puppies = total_students * puppy_owners_percent_decimal

    # L2
    parrot_owners_percent_decimal = 0.25 # 25% also have parrots
    students_with_both = students_with_puppies * parrot_owners_percent_decimal

    # L3
    # FA
    answer = students_with_both
    return answer