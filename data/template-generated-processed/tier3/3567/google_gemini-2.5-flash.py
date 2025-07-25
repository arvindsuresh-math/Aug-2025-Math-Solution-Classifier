from fractions import Fraction

def solve():
    """Index: 3567.
    Returns: the number of invited students who attended the party.
    """
    # L1
    invited_percentage = Fraction(70, 100) # 70% of the students who showed up were invited
    total_students_showed_up = 400 # 400 students show up to the party
    invited_students = invited_percentage * total_students_showed_up

    # L2
    revoked_percentage = Fraction(40, 100) # 40% of those invited to the party had their invitation revoked
    students_with_revoked_invitation = revoked_percentage * invited_students

    # L3
    invited_students_attended = invited_students - students_with_revoked_invitation

    # FA
    answer = invited_students_attended
    return answer