def solve():
    """Index: 6531.
    Returns: the number of logs left after 3 hours.
    """
    # L1
    hours = 3 # after 3 hours
    logs_added_per_hour = 2 # two more logs added to it at the end of every hour
    total_logs_added = hours * logs_added_per_hour

    # L2
    logs_burned_per_hour = 3 # burns three logs every hour
    total_logs_burned = logs_burned_per_hour * hours

    # L3
    initial_logs = 6 # built with six logs to start
    logs_left = initial_logs + total_logs_added - total_logs_burned

    # FA
    answer = logs_left
    return answer