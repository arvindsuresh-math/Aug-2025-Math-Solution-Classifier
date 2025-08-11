from fractions import Fraction

def solve():
    """Index: 4125.
    Returns: the number of days it took Joey to learn swimming.
    """
    # L1
    days_per_week = 7 # WK
    extra_days = 2 # a week and 2 days
    alexa_vacation_days = days_per_week + extra_days

    # L3
    # The question states "3/4ths of the time". The solution uses its reciprocal "4/3".
    # These values are derived from the fraction stated in the question.
    reciprocal_numerator = 4 # derived from 3/4ths of the time
    reciprocal_denominator = 3 # derived from 3/4ths of the time
    ethan_learning_days = Fraction(reciprocal_numerator, reciprocal_denominator) * alexa_vacation_days

    # L4
    half_divisor = 2 # half as much
    joey_swimming_days = ethan_learning_days / half_divisor

    # FA
    answer = joey_swimming_days
    return answer