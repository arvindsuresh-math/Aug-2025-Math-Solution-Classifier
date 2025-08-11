from fractions import Fraction

def solve():
    """Index: 5772.
    Returns: the amount of money Will has left.
    """
    # L1
    shoe_cost = 30 # a pair of shoes for $30
    refund_percentage_lost = Fraction(10, 100) # lost 10% of the money
    money_lost_on_shoes = refund_percentage_lost * shoe_cost

    # L2
    sweater_cost = 9 # a sweater for $9
    tshirt_cost = 11 # a T-shirt for $11
    total_spent = sweater_cost + tshirt_cost + money_lost_on_shoes

    # L3
    initial_money = 74 # gave him $74 to go shopping
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer