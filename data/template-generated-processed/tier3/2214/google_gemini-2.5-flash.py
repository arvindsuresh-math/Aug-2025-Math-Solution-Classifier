from fractions import Fraction

def solve():
    """Index: 2214.
    Returns: the time Matt spent on homework in other subjects.
    """
    # L1
    math_percentage_value = 30 # 30% of that time on math
    science_percentage_value = 40 # 40% on science
    combined_percentage_value = math_percentage_value + science_percentage_value

    # L2
    combined_percentage_fraction = Fraction(combined_percentage_value, 100)
    total_homework_minutes = 150 # Matt did his homework for 150 minutes
    time_on_math_science = combined_percentage_fraction * total_homework_minutes

    # L3
    time_on_other_subjects = total_homework_minutes - time_on_math_science

    # FA
    answer = time_on_other_subjects
    return answer