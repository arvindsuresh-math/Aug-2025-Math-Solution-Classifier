def solve():
    """Index: 2619.
    Returns: the average number of people who attended class each day.
    """
    # L1
    monday_attendance = 10 # 10 people attended class on Monday
    tuesday_attendance = 15 # 15 on Tuesday
    wednesday_attendance = 10 # 10 on each day from Wednesday
    thursday_attendance = 10 # 10 on each day from Thursday
    friday_attendance = 10 # 10 on each day from Friday
    total_attendance = monday_attendance + tuesday_attendance + wednesday_attendance + thursday_attendance + friday_attendance

    # L2
    number_of_days = 5 # across the 5 days (Monday through Friday)
    average_attendance = total_attendance / number_of_days

    # FA
    answer = average_attendance
    return answer