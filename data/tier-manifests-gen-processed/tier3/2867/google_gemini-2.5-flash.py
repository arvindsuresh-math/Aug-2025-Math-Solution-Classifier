from fractions import Fraction

def solve():
    """Index: 2867.
    Returns: the total time the three take to complete the marathon.
    """
    # L1
    dean_time = 9 # If Dean takes 9 hours
    micah_speed_factor = Fraction(2, 3) # 2/3 times as fast as Dean
    micah_time = micah_speed_factor * dean_time

    # L2
    jake_additional_factor = Fraction(1, 3) # 1/3 times more time
    jake_additional_time = jake_additional_factor * micah_time

    # L3
    jake_total_time = micah_time + jake_additional_time

    # L4
    total_marathon_time = jake_total_time + micah_time + dean_time

    # FA
    answer = total_marathon_time
    return answer