def solve():
    """Index: 686.
    Returns: the amount each friend paid.
    """
    # L1
    hourly_cost = 5 # costs $5 an hour
    rental_hours = 8 # rented it for eight hours
    total_cost = hourly_cost * rental_hours

    # L2
    number_of_friends = 2 # Jack and Jill shared the cost
    cost_per_friend = total_cost / number_of_friends

    # FA
    answer = cost_per_friend
    return answer