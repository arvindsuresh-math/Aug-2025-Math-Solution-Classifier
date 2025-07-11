def solve():
    """Index: 2962.
    Returns: the total dollars Hayden is owed for his work today.
    """
    # L1
    num_groups_rides = 3 # gave rides to three groups
    wage_per_ride = 5 # $5 for every ride he gives
    owed_for_rides = num_groups_rides * wage_per_ride

    # L2
    hourly_wage = 15 # hourly wage is $15
    hours_driven = 8 # drove for eight hours
    owed_for_hours = hourly_wage * hours_driven

    # L3
    gallons_gas = 17 # put 17 gallons of gas
    cost_per_gallon = 3 # $3 per gallon
    owed_for_gas = gallons_gas * cost_per_gallon

    # L4
    num_good_reviews = 2 # got two good reviews
    bonus_per_review = 20 # $20 bonus
    owed_for_reviews = num_good_reviews * bonus_per_review

    # L5
    total_owed = owed_for_rides + owed_for_hours + owed_for_gas + owed_for_reviews

    # FA
    answer = total_owed
    return answer