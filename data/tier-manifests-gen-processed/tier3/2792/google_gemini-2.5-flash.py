from fractions import Fraction

def solve():
    """Index: 2792.
    Returns: the total number of artistic works created by the whole class.
    """
    # L1
    total_students = 10 # 10 students
    half_fraction = Fraction(1, 2) # 1/2 of them
    students_group_one = half_fraction * total_students

    # L2
    artworks_per_student_group_one = 3 # make 3 artworks each
    artworks_group_one = students_group_one * artworks_per_student_group_one

    # L3
    artworks_per_student_group_two = 4 # make 4 artworks each
    artworks_group_two = students_group_one * artworks_per_student_group_two

    # L4
    total_artworks = artworks_group_one + artworks_group_two

    # FA
    answer = total_artworks
    return answer