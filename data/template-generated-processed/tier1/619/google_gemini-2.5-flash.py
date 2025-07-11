def solve():
    """Index: 619.
    Returns: the total dollars Harry earns in a week.
    """
    # L1
    num_days_mon_wed_fri = 3 # WK
    dogs_mon_wed_fri_per_day = 7 # walks 7 dogs
    total_dogs_mon_wed_fri = num_days_mon_wed_fri * dogs_mon_wed_fri_per_day

    # L2
    dogs_tuesday = 12 # walks 12 dogs
    dogs_thursday = 9 # walks 9 dogs
    total_dogs_per_week = total_dogs_mon_wed_fri + dogs_tuesday + dogs_thursday

    # L3
    payment_per_dog = 5 # paid $5 for each dog
    total_earnings_per_week = payment_per_dog * total_dogs_per_week

    # FA
    answer = total_earnings_per_week
    return answer