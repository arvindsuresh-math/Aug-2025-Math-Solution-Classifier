def solve():
    """Index: 1176.
    Returns: the total number of tickets Paula needs.
    """
    # L2
    go_kart_rides = 1 # ride the go-karts 1 time
    go_kart_cost_per_ride = 4 # 4 tickets to ride the go-karts
    go_kart_total_tickets = go_kart_rides * go_kart_cost_per_ride

    # L3
    bumper_car_rides = 4 # the bumper cars 4 times
    bumper_car_cost_per_ride = 5 # 5 tickets to ride the bumper cars
    bumper_car_total_tickets = bumper_car_rides * bumper_car_cost_per_ride

    # L4
    total_tickets_needed = go_kart_total_tickets + bumper_car_total_tickets

    # FA
    answer = total_tickets_needed
    return answer