from fractions import Fraction

def solve():
    """Index: 1274.
    Returns: the total number of non-pizza eaters at Esme's school.
    """
    # L1
    teachers_pizza_fraction = Fraction(2, 3) # 2/3 of the teachers
    total_teachers = 30 # 30 teachers
    teachers_ate_pizza = teachers_pizza_fraction * total_teachers

    # L2
    teachers_no_pizza = total_teachers - teachers_ate_pizza

    # L3
    staff_pizza_fraction = Fraction(4, 5) # 4/5 of the staff members
    total_staff = 45 # 45 staff members
    staff_ate_pizza = staff_pizza_fraction * total_staff

    # L4
    staff_no_pizza = total_staff - staff_ate_pizza

    # L5
    total_non_pizza_eaters = staff_no_pizza + teachers_no_pizza

    # FA
    answer = total_non_pizza_eaters
    return answer