from fractions import Fraction

def solve():
    """Index: 4914.
    Returns: the number of minutes Janice has left before the movie starts.
    """
    # L1
    homework_time = 30 # homework which takes 30 minutes
    room_cleaning_divisor = 2 # half as long as her homework
    room_cleaning_time = homework_time / room_cleaning_divisor

    # L2
    dog_walk_extra_time = 5 # 5 minutes more than making homework
    dog_walking_time = homework_time + dog_walk_extra_time

    # L3
    trash_fraction = Fraction(1, 6) # 1/6 of the time it takes her to do the homework
    trash_time = homework_time * trash_fraction

    # L4
    total_chore_time = homework_time + room_cleaning_time + dog_walking_time + trash_time

    # L5
    movie_duration_hours = 2 # watch a movie in 2 hours
    minutes_per_hour = 60 # WK
    movie_duration_minutes = movie_duration_hours * minutes_per_hour

    # L6
    minutes_left = movie_duration_minutes - total_chore_time

    # FA
    answer = minutes_left
    return answer