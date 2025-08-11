from fractions import Fraction

def solve():
    """Index: 3375.
    Returns: the number of boys who did not join varsity clubs.
    """
    # L1
    total_percentage = 100 # WK
    girls_percentage = 60 # 60% are girls
    boys_percentage = total_percentage - girls_percentage

    # L2
    total_students = 150 # 150 students
    num_boys = total_students * boys_percentage / total_percentage

    # L3
    fraction_joined_clubs = Fraction(1, 3) # 1/3 of the boys
    boys_joined_clubs = num_boys * fraction_joined_clubs

    # L4
    boys_not_joined_clubs = num_boys - boys_joined_clubs

    # FA
    answer = boys_not_joined_clubs
    return answer