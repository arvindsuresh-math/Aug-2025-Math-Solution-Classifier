from fractions import Fraction

def solve():
    """Index: 3460.
    Returns: the number of scoops each person bought.
    """
    # L1
    num_brothers = 2 # Aaron and his brother Carson
    money_per_brother = 40 # each saved up $40
    total_initial_money = num_brothers * money_per_brother

    # L2
    bill_fraction = Fraction(3, 4) # 3/4 of their total money
    money_spent_on_dinner = total_initial_money * bill_fraction

    # L3
    money_left_for_ice_cream = total_initial_money - money_spent_on_dinner

    # L4
    change_per_person = 1 # $1 in change each
    total_change_left = num_brothers * change_per_person

    # L5
    money_spent_on_ice_cream = money_left_for_ice_cream - total_change_left

    # L6
    cost_per_scoop = 1.5 # Each scoop costs $1.5
    total_scoops = money_spent_on_ice_cream / cost_per_scoop

    # L7
    scoops_per_person = total_scoops / num_brothers

    # FA
    answer = scoops_per_person
    return answer