from fractions import Fraction

def solve():
    """Index: 5376.
    Returns: the total number of marks in all semesters.
    """
    # L1
    second_semester_math_marks = 80 # 80 marks in maths in the second semester
    math_mark_difference = 10 # ten more marks in maths in the first semester than the second
    first_semester_math_marks = second_semester_math_marks + math_mark_difference

    # L2
    second_semester_arts_marks = 90 # 90 marks in arts
    arts_mark_difference = 15 # 15 marks less in arts
    first_semester_arts_marks = second_semester_arts_marks - arts_mark_difference

    # L3
    science_fraction_less = Fraction(1, 3) # 1/3 marks less in science
    second_semester_science_marks = 90 # 90 in science
    science_mark_reduction = science_fraction_less * second_semester_science_marks

    # L4
    first_semester_science_marks = second_semester_science_marks - science_mark_reduction

    # L5
    total_first_semester_marks = first_semester_math_marks + first_semester_arts_marks + first_semester_science_marks

    # L6
    total_second_semester_marks = second_semester_arts_marks + second_semester_science_marks + second_semester_math_marks

    # L7
    combined_total_marks = total_second_semester_marks + total_first_semester_marks

    # FA
    answer = combined_total_marks
    return answer