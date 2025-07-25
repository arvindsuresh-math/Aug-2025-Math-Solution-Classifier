def solve():
    """Index: 1834.
    Returns: the total amount Jimmy spent on lodging.
    """
    # L1
    first_days_count = 3 # The first 3 days
    hostel_cost_per_night = 15 # $15 per night
    cost_first_period = first_days_count * hostel_cost_per_night

    # L2
    next_days_count = 2 # The fourth and fifth days
    cabin_total_cost_per_night = 45 # $45 total per night
    total_cabin_cost_friends = cabin_total_cost_per_night * next_days_count

    # L3
    number_of_friends = 2 # 2 of his friends
    jimmy_count = 1 # WK
    total_people_sharing = jimmy_count + number_of_friends # WK
    jimmy_cabin_share = total_cabin_cost_friends / total_people_sharing

    # L4
    total_spent = cost_first_period + jimmy_cabin_share

    # FA
    answer = total_spent
    return answer