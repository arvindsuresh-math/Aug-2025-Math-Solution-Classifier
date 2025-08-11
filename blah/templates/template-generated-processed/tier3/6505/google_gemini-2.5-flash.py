from fractions import Fraction

def solve():
    """Index: 6505.
    Returns: the average marks scored by the three.
    """
    # L1
    dorothy_marks = 90 # Dorothy scored 90 marks
    ivanna_fraction = Fraction(3, 5) # Ivanna scored 3/5 times as many marks
    ivanna_marks = ivanna_fraction * dorothy_marks

    # L2
    dorothy_ivanna_total_marks = ivanna_marks + dorothy_marks

    # L3
    tatuya_multiplier = 2 # twice as much as Ivanna
    tatuya_marks = tatuya_multiplier * ivanna_marks

    # L4
    total_marks_three = tatuya_marks + dorothy_ivanna_total_marks

    # L5
    number_of_students = 3 # the three
    average_marks = total_marks_three / number_of_students

    # FA
    answer = average_marks
    return answer