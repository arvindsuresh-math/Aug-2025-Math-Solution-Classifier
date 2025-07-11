from fractions import Fraction

def solve():
    """Index: 1324.
    Returns: the total cost of lunch for all three friends.
    """
    # L1
    jose_lunch_cost = 45 # If Jose ate lunch worth $45
    adam_fraction = Fraction(2, 3) # two-thirds as much money on lunch as Rick
    adam_lunch_cost = adam_fraction * jose_lunch_cost

    # L2
    rick_lunch_cost = 45 # Rick and Jose eat lunch of the same price
    total_lunch_cost = adam_lunch_cost + jose_lunch_cost + rick_lunch_cost

    # FA
    answer = total_lunch_cost
    return answer