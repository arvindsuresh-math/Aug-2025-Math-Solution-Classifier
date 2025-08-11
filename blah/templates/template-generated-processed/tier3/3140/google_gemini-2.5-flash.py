from fractions import Fraction

def solve():
    """Index: 3140.
    Returns: the number of vacant seats from the students that can be given to the parents.
    """
    # L1
    rows_for_awardees = 1 # The first row is reserved for the awardees
    rows_for_admin_teachers = 2 # the second and third rows are for the administrators and teachers
    rows_for_parents = 2 # The last two rows are then reserved for the parents
    non_student_rows = rows_for_awardees + rows_for_admin_teachers + rows_for_parents

    # L2
    total_rows = 10 # There are 10 rows
    student_rows = total_rows - non_student_rows

    # L3
    chairs_per_row = 15 # 15 chairs set up
    total_student_seats = student_rows * chairs_per_row

    # L4
    occupied_fraction = Fraction(4, 5) # 4/5 of the seats reserved for the students are occupied
    occupied_student_seats = total_student_seats * occupied_fraction

    # L5
    vacant_student_seats = total_student_seats - occupied_student_seats

    # FA
    answer = vacant_student_seats
    return answer