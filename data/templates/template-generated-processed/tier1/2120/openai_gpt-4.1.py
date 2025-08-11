def solve():
    """Index: 2120.
    Returns: how many more pins in total Richard knocked down than Patrick.
    """
    # L1
    patrick_first = 70 # Patrick knocked down a total of 70 pins
    richard_first_more = 15 # Richard knocked down 15 more pins than Patrick
    richard_first = patrick_first + richard_first_more

    # L2
    patrick_second_multiplier = 2 # Patrick knocked down twice as many pins as Richard in the first round
    patrick_second = richard_first * patrick_second_multiplier

    # L3
    richard_second_less = 3 # Richard knocked down 3 less than Patrick
    richard_second = patrick_second - richard_second_less

    # L4
    patrick_total = patrick_first + patrick_second

    # L5
    richard_total = richard_first + richard_second

    # L6
    difference = richard_total - patrick_total

    # FA
    answer = difference
    return answer