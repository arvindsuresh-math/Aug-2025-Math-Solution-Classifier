from fractions import Fraction

def solve():
    """Index: 301.
    Returns: the number of students who do not read novels.
    """
    # L1
    total_students = 240 # 240 sixth-grade students
    three_or_more_fraction = Fraction(1, 6) # 1/6 of students read three or more novels
    students_three_or_more = three_or_more_fraction * total_students

    # L2
    two_novels_percentage = Fraction(35, 100) # 35% of students read two novels
    students_two_novels = two_novels_percentage * total_students

    # L3
    one_novel_fraction = Fraction(5, 12) # 5/12 of students read one novel
    students_one_novel = one_novel_fraction * total_students

    # L4
    students_no_novels = total_students - (students_three_or_more + students_two_novels + students_one_novel)

    # FA
    answer = students_no_novels
    return answer