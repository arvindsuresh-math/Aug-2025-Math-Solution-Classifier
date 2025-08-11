def solve():
    """Index: 4108.
    Returns: the latest time Justin could start his chores and homework.
    """
    # L1
    dinner_time = 45 # dinner would take 45 minutes
    homework_time = 30 # homework would take 30 minutes
    room_cleaning_time = 30 # clean his room, which would take 30 minutes
    trash_time = 5 # take out the trash, which would take about 5 minutes
    dishwasher_time = 10 # empty the dishwasher, which would take another 10 minutes
    total_minutes_work = dinner_time + homework_time + room_cleaning_time + trash_time + dishwasher_time

    # L2
    minutes_per_hour = 60 # WK
    total_hours_work = total_minutes_work / minutes_per_hour

    # L3
    movie_start_time_pm = 8 # movie that came on at 8 pm
    latest_start_time_pm = movie_start_time_pm - total_hours_work

    # FA
    answer = latest_start_time_pm
    return answer