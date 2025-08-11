from fractions import Fraction

def solve():
    """Index: 6221.
    Returns: the total number of students at the competition.
    """
    # L1
    know_it_all_students = 50 # 50 students from Know It All High School
    karen_fraction = Fraction(3, 5) # 3/5 times as many students from Karen High as Know It All High School
    karen_students = karen_fraction * know_it_all_students

    # L2
    combined_know_it_all_karen = know_it_all_students + karen_students

    # L3
    novel_corona_multiplier = 2 # twice the combined number of students
    novel_corona_students = novel_corona_multiplier * combined_know_it_all_karen

    # L4
    total_students_competition = combined_know_it_all_karen + novel_corona_students

    # FA
    answer = total_students_competition
    return answer