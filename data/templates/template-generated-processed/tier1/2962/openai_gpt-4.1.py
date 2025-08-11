def solve():
    """Index: 2962.
    Returns: the total amount Hayden is owed for his work today in dollars.
    """
    # L1
    num_rides = 3 # gave rides to three groups
    pay_per_ride = 5 # paid an additional $5 for every ride
    ride_pay = num_rides * pay_per_ride

    # L2
    hourly_wage = 15 # hourly wage is $15
    hours_worked = 8 # drove for eight hours
    wage_pay = hourly_wage * hours_worked

    # L3
    gallons = 17 # put 17 gallons of gas
    price_per_gallon = 3 # $3 per gallon
    gas_reimbursement = gallons * price_per_gallon

    # L4
    num_good_reviews = 2 # got two good reviews
    bonus_per_review = 20 # $20 bonus per good review
    review_bonus = num_good_reviews * bonus_per_review

    # L5
    total_owed = ride_pay + wage_pay + gas_reimbursement + review_bonus

    # FA
    answer = total_owed
    return answer