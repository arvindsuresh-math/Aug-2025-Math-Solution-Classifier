def solve():
    """Index: 3410.
    Returns: the amount each person has to pay for the rental.
    """
    # L1
    weekday_rate = 420 # The rental rate for weekdays is $420 per day
    num_weekday_days = 2 # 4 days from Thursday to Sunday (Thursday and Friday are weekdays)
    weekday_cost = weekday_rate * num_weekday_days

    # L2
    weekend_rate = 540 # The weekend rental rate is $540 per day
    num_weekend_days = 2 # 4 days from Thursday to Sunday (Saturday and Sunday are weekend days)
    weekend_cost = weekend_rate * num_weekend_days

    # L3
    total_rental_cost = weekday_cost + weekend_cost

    # L4
    num_people = 6 # Suzie and 5 of her friends
    cost_per_person = total_rental_cost / num_people

    # FA
    answer = cost_per_person
    return answer