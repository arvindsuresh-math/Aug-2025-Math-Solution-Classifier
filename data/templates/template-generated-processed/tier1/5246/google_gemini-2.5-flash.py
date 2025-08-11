def solve():
    """Index: 5246.
    Returns: the total money Greg earns from dog walking.
    """
    # L1
    charge_per_dog = 20 # charges $20 per dog
    cost_per_minute_per_dog = 1 # $1 per minute per dog
    minutes_dog1 = 10 # walks one dog for 10 minutes
    cost_dog1 = charge_per_dog + (minutes_dog1 * cost_per_minute_per_dog)

    # L2
    num_dogs_batch2 = 2 # two dogs
    minutes_dog2 = 7 # for 7 minutes
    cost_dog2 = num_dogs_batch2 * (charge_per_dog + (minutes_dog2 * cost_per_minute_per_dog))

    # L3
    num_dogs_batch3 = 3 # three dogs
    minutes_dog3 = 9 # for 9 minutes
    cost_dog3 = num_dogs_batch3 * (charge_per_dog + (minutes_dog3 * cost_per_minute_per_dog))

    # L4
    total_earnings = cost_dog1 + cost_dog2 + cost_dog3

    # FA
    answer = total_earnings
    return answer