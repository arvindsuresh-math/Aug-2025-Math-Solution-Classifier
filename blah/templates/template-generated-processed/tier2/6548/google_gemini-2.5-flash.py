def solve():
    """Index: 6548.
    Returns: the money left to spend on lunch and snacks.
    """
    # L1
    ticket_cost_per_person = 5 # $5 per person
    num_people = 2 # Noah and Ava
    total_ticket_cost = ticket_cost_per_person * num_people

    # L2
    bus_fare_one_way_per_person = 1.50 # $1.50 per person one way
    num_trips = 2 # WK
    total_bus_fare = bus_fare_one_way_per_person * num_people * num_trips

    # L3
    total_transport_and_entry_cost = total_ticket_cost + total_bus_fare

    # L4
    initial_money = 40 # $40 with them
    money_left_for_lunch_snacks = initial_money - total_transport_and_entry_cost

    # FA
    answer = money_left_for_lunch_snacks
    return answer