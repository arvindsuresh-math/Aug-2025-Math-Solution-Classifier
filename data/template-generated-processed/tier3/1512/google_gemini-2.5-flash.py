from fractions import Fraction

def solve():
    """Index: 1512.
    Returns: the total bonus points Tom earned.
    """
    # L1
    hours_worked = 8 # for 8 hours
    customers_per_hour = 10 # 10 customers per hour
    total_customers_served = hours_worked * customers_per_hour

    # L2
    bonus_percentage = Fraction(20, 100) # 20% of the number of customers served
    bonus_points = bonus_percentage * total_customers_served

    # FA
    answer = bonus_points
    return answer