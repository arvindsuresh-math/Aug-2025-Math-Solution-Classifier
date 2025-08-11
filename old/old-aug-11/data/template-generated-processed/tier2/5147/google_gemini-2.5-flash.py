def solve():
    """Index: 5147.
    Returns: the total money Rachel made in that hour.
    """
    # L1
    num_people_served = 20 # serves 20 different people
    tip_per_person = 1.25 # leave her a $1.25 tip
    tips_earned = num_people_served * tip_per_person

    # L2
    hourly_wage = 12.00 # makes $12.00 as a waitress
    total_money_made = hourly_wage + tips_earned

    # FA
    answer = total_money_made
    return answer