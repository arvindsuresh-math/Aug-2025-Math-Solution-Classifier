from fractions import Fraction

def solve():
    """Index: 6634.
    Returns: the number of girls at the school.
    """
    # L1
    total_percentage_val = 100 # WK
    girls_percentage_val = 60 # 60% of the students at school are girls
    boys_percentage_val = total_percentage_val - girls_percentage_val

    # L2
    number_of_boys = 300 # the number of boys is 300
    percentage_denominator = 100 # WK
    boys_fraction_for_calc = Fraction(boys_percentage_val, percentage_denominator)
    total_students = number_of_boys / boys_fraction_for_calc

    # L3
    girls_fraction_for_calc = Fraction(girls_percentage_val, percentage_denominator)
    number_of_girls = girls_fraction_for_calc * total_students

    # FA
    answer = number_of_girls
    return answer