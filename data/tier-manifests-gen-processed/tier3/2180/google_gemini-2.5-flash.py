def solve():
    """Index: 2180.
    Returns: the additional amount each friend has to pay.
    """
    # L1
    car_price = 1700 # The cost of the car is $1700
    car_wash_earnings = 500 # they earn $500
    remaining_cost = car_price - car_wash_earnings

    # L2
    initial_friends_count = 6 # A group of six friends
    initial_share_per_friend = remaining_cost / initial_friends_count

    # L3
    remaining_friends_count = 5 # Brad decided not to join in the purchase of the car
    additional_cost_per_friend = initial_share_per_friend / remaining_friends_count

    # FA
    answer = additional_cost_per_friend
    return answer