def solve():
    """Index: 2181.
    Returns: the amount John paid for the camera rental.
    """
    # L1
    camera_value = 5000 # $5000 camera
    rental_percent = 0.1 # 10% of the value per week
    rental_fee_per_week = camera_value * rental_percent

    # L2
    num_weeks = 4 # rent one for 4 weeks
    total_rental_fee = rental_fee_per_week * num_weeks

    # L3
    friend_share_percent = 0.4 # friend agreed to pay 40% of the rental fee
    friend_payment = total_rental_fee * friend_share_percent

    # L4
    john_payment = total_rental_fee - friend_payment

    # FA
    answer = john_payment
    return answer