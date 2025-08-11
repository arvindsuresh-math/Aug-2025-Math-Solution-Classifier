from fractions import Fraction

def solve():
    """Index: 751.
    Returns: the speed Harry ran on Friday.
    """
    # L1
    monday_speed = 10 # He ran 10 meters per hour on Monday
    faster_percentage_tue_thu = Fraction(50, 100) # 50% faster than on Monday
    speed_increase_tue_thu = monday_speed * faster_percentage_tue_thu

    # L2
    tue_thu_speed = monday_speed + speed_increase_tue_thu

    # L3
    faster_percentage_friday = Fraction(60, 100) # 60% faster than he ran on Thursday
    speed_increase_friday = tue_thu_speed * faster_percentage_friday

    # L4
    friday_speed = tue_thu_speed + speed_increase_friday

    # FA
    answer = friday_speed
    return answer