from fractions import Fraction

def solve():
    """Index: 4436.
    Returns: the additional money Mike needs to buy the phone.
    """
    # L1
    percentage_had = Fraction(40, 100) # 40% of the amount
    phone_cost = 1300 # The cost of the phone is $1300
    money_mike_has = percentage_had * phone_cost

    # L2
    money_needed_more = phone_cost - money_mike_has

    # FA
    answer = money_needed_more
    return answer