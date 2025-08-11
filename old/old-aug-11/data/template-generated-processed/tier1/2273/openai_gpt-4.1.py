def solve():
    """Index: 2273.
    Returns: the total amount Andrea spends on her pony in a year.
    """
    # L1
    food_per_day = 10 # $10 a day for food
    days_per_year = 365 # WK
    annual_food_cost = food_per_day * days_per_year

    # L2
    lesson_cost = 60 # $60/lesson
    lessons_per_week = 2 # two lessons a week
    weekly_lesson_cost = lesson_cost * lessons_per_week

    # L3
    weeks_per_year = 52 # WK
    annual_lesson_cost = weekly_lesson_cost * weeks_per_year

    # L4
    pasture_per_month = 500 # $500/month to rent a pasture
    months_per_year = 12 # WK
    annual_pasture_cost = pasture_per_month * months_per_year

    # L5
    total_cost = annual_pasture_cost + annual_lesson_cost + annual_food_cost

    # FA
    answer = total_cost
    return answer