def solve():
    """Index: 4407.
    Returns: the number of pins after Reese had been a member for a month.
    """
    # L1
    avg_pins_per_day_per_member = 10 # 10 pins per day
    num_people_in_group = 20 # group has 20 people
    total_new_pins_per_day = avg_pins_per_day_per_member * num_people_in_group

    # L2
    days_in_month = 30 # WK
    total_new_pins_after_month = days_in_month * total_new_pins_per_day

    # L3
    initial_total_pins = 1000 # total number of pins is 1000
    total_pins_before_deletion = total_new_pins_after_month + initial_total_pins

    # L4
    deleted_pins_per_week_per_person = 5 # 5 pins per week per person
    total_deleted_pins_per_week = deleted_pins_per_week_per_person * num_people_in_group

    # L5
    weeks_in_month = 4 # WK
    total_deleted_pins_after_month = total_deleted_pins_per_week * weeks_in_month

    # L6
    final_pins = total_pins_before_deletion - total_deleted_pins_after_month

    # FA
    answer = final_pins
    return answer