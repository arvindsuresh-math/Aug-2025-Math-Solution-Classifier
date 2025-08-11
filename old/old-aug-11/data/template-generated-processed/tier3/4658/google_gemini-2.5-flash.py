from fractions import Fraction

def solve():
    """Index: 4658.
    Returns: the amount of money left for Toby.
    """
    # L1
    fraction_given_to_each_brother = Fraction(1, 7) # 1/7 of $343
    total_money_given_by_father = 343 # $343 for passing the test
    money_given_to_each_brother = fraction_given_to_each_brother * total_money_given_by_father

    # L2
    number_of_brothers = 2 # his two brothers
    total_money_given_to_brothers = number_of_brothers * money_given_to_each_brother

    # L3
    money_left_for_toby = total_money_given_by_father - total_money_given_to_brothers

    # FA
    answer = money_left_for_toby
    return answer