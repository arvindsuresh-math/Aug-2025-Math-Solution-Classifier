def solve():
    """Index: 1635.
    Returns: how much higher Janet's semester 1 average was compared to her semester 2 average.
    """
    # L1
    grade1 = 90 # Janet's grades for her first semester of college were 90
    grade2 = 80 # Janet's grades for her first semester of college were 80
    grade3 = 70 # Janet's grades for her first semester of college were 70
    grade4 = 100 # Janet's grades for her first semester of college were 100
    semester1_grades_sum = grade1 + grade2 + grade3 + grade4

    # L2
    num_grades_semester1 = 4 # WK
    semester1_average = semester1_grades_sum / num_grades_semester1

    # L3
    semester2_average = 82 # her semester 2 average was 82 percent
    difference_in_averages = semester1_average - semester2_average

    # FA
    answer = difference_in_averages
    return answer