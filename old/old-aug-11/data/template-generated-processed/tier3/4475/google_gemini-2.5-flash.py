def solve():
    """Index: 4475.
    Returns: the average distance traveled per day.
    """
    # L1
    monday_distance = 12 # 12 miles on Monday
    tuesday_distance = 18 # 18 miles on Tuesday
    wednesday_distance = 21 # 21 miles on Wednesday
    total_distance = monday_distance + tuesday_distance + wednesday_distance

    # L2
    number_of_days = 3 # Monday, Tuesday, and Wednesday
    average_distance = total_distance / number_of_days

    # FA
    answer = average_distance
    return answer