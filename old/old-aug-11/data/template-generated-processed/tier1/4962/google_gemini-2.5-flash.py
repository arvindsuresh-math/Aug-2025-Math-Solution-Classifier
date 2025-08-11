def solve():
    """Index: 4962.
    Returns: the number of shirts Kendra needs for a two-week laundry cycle.
    """
    # L1
    shirts_per_weekday = 1 # one shirt to school
    num_weekdays = 5 # five weekdays
    school_day_shirts = shirts_per_weekday * num_weekdays

    # L2
    shirts_per_club_day = 1 # a different shirt for an after-school club
    num_club_days = 3 # Three days a week
    club_shirts = shirts_per_club_day * num_club_days

    # L3
    sunday_church_shirt = 1 # a different shirt to church
    sunday_rest_of_day_shirt = 1 # than she does for the rest of the day
    sunday_shirts = sunday_church_shirt + sunday_rest_of_day_shirt

    # L4
    saturday_shirt = 1 # one shirt all day (Saturday)
    total_shirts_per_week = school_day_shirts + club_shirts + saturday_shirt + sunday_shirts

    # L5
    num_weeks_laundry_cycle = 2 # once every two weeks
    total_shirts_needed = total_shirts_per_week * num_weeks_laundry_cycle

    # FA
    answer = total_shirts_needed
    return answer