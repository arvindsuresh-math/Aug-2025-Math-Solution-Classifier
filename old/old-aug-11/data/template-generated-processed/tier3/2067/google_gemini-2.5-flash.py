def solve():
    """Index: 2067.
    Returns: the amount of money each person still needs to raise.
    """
    # L1
    cost_per_student = 450 # each of them needs at least $450
    num_students = 6 # group of 6 students
    misc_expenses = 3000 # need $3000 for their miscellaneous collective expenses
    total_goal = (cost_per_student * num_students) + misc_expenses

    # L2
    day1_fundraising = 600 # receive $600
    day2_fundraising = 900 # receive $900
    day3_fundraising = 400 # receive $400
    first_three_days_raised = day1_fundraising + day2_fundraising + day3_fundraising

    # L3
    half_divisor = 2 # only half of what they raised
    next_four_days_raised = first_three_days_raised / half_divisor

    # L4
    total_raised_week = first_three_days_raised + next_four_days_raised

    # L5
    money_still_needed = total_goal - total_raised_week

    # L6
    per_person_needed = money_still_needed / num_students

    # FA
    answer = per_person_needed
    return answer