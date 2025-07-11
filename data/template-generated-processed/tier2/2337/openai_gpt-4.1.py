def solve():
    """Index: 2337.
    Returns: the total amount the P.T.O. spent on shirts for field day.
    """
    # L1
    num_kindergarten = 101 # 101 Kindergartners
    cost_kindergarten = 5.80 # $5.80 each
    kindergarten_total = num_kindergarten * cost_kindergarten

    # L2
    num_first = 113 # 113 first graders
    cost_first = 5 # $5 each
    first_total = num_first * cost_first

    # L3
    num_second = 107 # 107 second graders
    cost_second = 5.60 # $5.60 each
    second_total = num_second * cost_second

    # L4
    num_third = 108 # 108 third graders
    cost_third = 5.25 # $5.25 each
    third_total = num_third * cost_third

    # L5
    total_cost = kindergarten_total + first_total + second_total + third_total

    # FA
    answer = total_cost
    return answer