def solve():
    """Index: 3060.
    Returns: the number of days it will take half of the people to shovel the target amount of coal.
    """
    # L1
    initial_people = 10 # 10 people
    initial_coal_pounds = 10000 # 10,000 pounds of coal
    initial_days = 10 # 10 days
    pounds_per_day_per_10_people = initial_coal_pounds / initial_days

    # L2
    pounds_per_day_per_person = pounds_per_day_per_10_people / initial_people

    # L3
    half_divisor = 2 # half of these ten people
    new_people = initial_people / half_divisor

    # L4
    pounds_per_day_per_new_people = new_people * pounds_per_day_per_person

    # L5
    target_coal_pounds = 40000 # 40,000 pounds of coal
    days_needed = target_coal_pounds / pounds_per_day_per_new_people

    # FA
    answer = days_needed
    return answer