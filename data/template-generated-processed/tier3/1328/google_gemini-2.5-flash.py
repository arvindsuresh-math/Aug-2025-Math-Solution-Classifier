from fractions import Fraction

def solve():
    """Index: 1328.
    Returns: the total earnings from Monday to Wednesday.
    """
    # L1
    monday_delivery = 20 # Every Monday he delivers 20 yards of fabric
    tuesday_multiplier = 2 # twice the amount of fabric he delivers on Monday
    tuesday_delivery = monday_delivery * tuesday_multiplier

    # L2
    wednesday_fraction = Fraction(1, 4) # 1/4 of the amount of fabric he delivers on Tuesday
    wednesday_delivery = tuesday_delivery * wednesday_fraction

    # L3
    total_fabric_delivered = monday_delivery + tuesday_delivery + wednesday_delivery

    # L4
    cost_per_yard = 2 # each yard of fabric costs $2
    total_earnings = cost_per_yard * total_fabric_delivered

    # FA
    answer = total_earnings
    return answer