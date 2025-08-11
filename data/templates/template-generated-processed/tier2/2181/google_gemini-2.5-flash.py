def solve():
    """Index: 2181.
    Returns: the amount John paid for the camera rental.
    """
    # L1
    camera_value = 5000 # $5000 camera
    rental_rate_percent = 0.1 # 10% of the value per week
    weekly_rental_fee = camera_value * rental_rate_percent

    # L2
    rental_duration_weeks = 4 # 4 weeks
    total_rental_cost = weekly_rental_fee * rental_duration_weeks

    # L3
    friend_share_percent = 0.4 # 40% of the rental fee
    friend_payment = total_rental_cost * friend_share_percent

    # L4
    john_payment = total_rental_cost - friend_payment

    # FA
    answer = john_payment
    return answer