from fractions import Fraction

def solve():
    """Index: 6702.
    Returns: the number of boys who attended the school dance.
    """
    # L1
    total_attendees = 100 # 100 people in attendance
    faculty_staff_percent_value = 0.1 # Ten percent of the attendees were school faculty and staff
    faculty_staff_count = faculty_staff_percent_value * total_attendees

    # L2
    remaining_students = total_attendees - faculty_staff_count

    # L3
    girls_fraction = Fraction(2, 3) # two-thirds were girls
    girls_count = girls_fraction * remaining_students

    # L4
    boys_count = remaining_students - girls_count

    # FA
    answer = boys_count
    return answer