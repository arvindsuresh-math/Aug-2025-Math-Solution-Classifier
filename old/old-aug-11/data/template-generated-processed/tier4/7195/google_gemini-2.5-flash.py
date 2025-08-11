def solve():
    """Index: 7195.
    Returns: the number of puppies Dorchester washed that day.
    """
    # L1
    total_earned = 76 # Dorchester earned $76
    daily_base_pay = 40 # paid $40 per day
    earned_from_puppies = total_earned - daily_base_pay

    # L2
    pay_per_puppy = 2.25 # $2.25 for each puppy he washes
    num_puppies = earned_from_puppies / pay_per_puppy

    # FA
    answer = num_puppies
    return answer