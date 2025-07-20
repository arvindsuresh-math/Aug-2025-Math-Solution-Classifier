def solve():
    """Index: 6137.
    Returns: the total money Lori earned from renting cars.
    """
    # L1
    num_white_cars = 2 # two white cars
    cost_per_minute_white_car = 2 # costs $2 for every minute
    cost_white_cars_per_minute = num_white_cars * cost_per_minute_white_car

    # L2
    num_red_cars = 3 # three red cars
    cost_per_minute_red_car = 3 # the red car $3 for every minute
    cost_red_cars_per_minute = num_red_cars * cost_per_minute_red_car

    # L3
    total_cost_per_minute = cost_white_cars_per_minute + cost_red_cars_per_minute

    # L4
    rental_hours = 3 # All cars were rented for 3 hours
    minutes_per_hour = 60 # WK
    total_rental_minutes = rental_hours * minutes_per_hour
    total_earned = total_cost_per_minute * total_rental_minutes

    # FA
    answer = total_earned
    return answer