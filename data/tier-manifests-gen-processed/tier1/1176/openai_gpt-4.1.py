def solve():
    """Index: 1176.
    Returns: the total number of tickets Paula needs.
    """
    # L2
    go_kart_rides = 1 # ride the go-karts 1 time
    go_kart_ticket_cost = 4 # costs 4 tickets to ride the go-karts
    go_kart_tickets = go_kart_rides * go_kart_ticket_cost

    # L3
    bumper_car_rides = 4 # bumper cars 4 times
    bumper_car_ticket_cost = 5 # 5 tickets to ride the bumper cars
    bumper_car_tickets = bumper_car_rides * bumper_car_ticket_cost

    # L4
    total_tickets = go_kart_tickets + bumper_car_tickets

    # FA
    answer = total_tickets
    return answer