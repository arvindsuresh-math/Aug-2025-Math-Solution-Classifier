def solve():
    """Index: 6870.
    Returns: the total money spent on the vacation.
    """
    # L1
    cost_plane_ticket_per_person = 24 # $24 for each person
    num_people = 2 # Jamie and Oliver
    total_plane_ticket_cost = cost_plane_ticket_per_person * num_people

    # L2
    cost_hotel_per_person_per_day = 12 # $12 for each person per day
    cost_hotel_per_day_for_two = cost_hotel_per_person_per_day * num_people

    # L3
    num_days_stay = 3 # stay for 3 days
    total_hotel_cost = cost_hotel_per_day_for_two * num_days_stay

    # L4
    total_vacation_cost = total_hotel_cost + total_plane_ticket_cost

    # FA
    answer = total_vacation_cost
    return answer