def solve():
    """Index: 7338.
    Returns: the amount of money Joe has left after his trip expenses.
    """
    # L1
    flight_cost = 1200 # $1,200 on the flight
    hotel_cost = 800 # $800 on a hotel
    food_cost = 3000 # $3,000 on food
    total_spent = flight_cost + hotel_cost + food_cost

    # L2
    initial_savings = 6000 # $6,000 for his trip to Australia
    money_left = initial_savings - total_spent

    # FA
    answer = money_left
    return answer