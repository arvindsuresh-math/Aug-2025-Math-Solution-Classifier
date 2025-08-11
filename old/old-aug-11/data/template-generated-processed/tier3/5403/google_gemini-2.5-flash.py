from fractions import Fraction

def solve():
    """Index: 5403.
    Returns: the number of hours of battery left in Brody's calculator.
    """
    # L1
    total_battery_capacity = 60 # 60 hours on a full battery
    battery_used_numerator = 3 # three quarters of its battery up
    battery_used_denominator = 4 # three quarters of its battery up
    remaining_fraction_numerator = battery_used_denominator - battery_used_numerator
    remaining_fraction_val = Fraction(remaining_fraction_numerator, battery_used_denominator)
    battery_remaining_divisor = battery_used_denominator
    battery_left_before_exam = total_battery_capacity * remaining_fraction_val

    # L2
    exam_duration_hours = 2 # two-hour math exam
    final_battery_left = battery_left_before_exam - exam_duration_hours

    # FA
    answer = final_battery_left
    return answer