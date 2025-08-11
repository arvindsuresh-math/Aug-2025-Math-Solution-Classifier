from fractions import Fraction

def solve():
    """Index: 6120.
    Returns: the combined number of students who like the color yellow and the color blue.
    """
    # L1
    blue_percentage = Fraction(30, 100) # thirty percent like the color blue
    total_students = 200 # 200 students in a class
    students_like_blue = blue_percentage * total_students

    # L2
    students_dont_like_blue = total_students - students_like_blue

    # L3
    red_percentage = Fraction(40, 100) # 40% like the color red
    students_like_red = red_percentage * students_dont_like_blue

    # L4
    students_like_yellow = students_dont_like_blue - students_like_red

    # L5
    combined_yellow_blue = students_like_yellow + students_like_blue

    # FA
    answer = combined_yellow_blue
    return answer