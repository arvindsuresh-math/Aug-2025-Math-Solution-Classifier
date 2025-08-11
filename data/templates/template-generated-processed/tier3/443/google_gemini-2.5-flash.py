def solve():
    """Index: 443.
    Returns: the amount each person will earn.
    """
    # L1
    num_shoes_sold = 6 # 6 pairs of shoes
    cost_per_shoe = 3 # $3 each
    earnings_shoes = num_shoes_sold * cost_per_shoe

    # L2
    num_shirts_sold = 18 # 18 shirts
    cost_per_shirt = 2 # $2
    earnings_shirts = num_shirts_sold * cost_per_shirt

    # L3
    total_earnings = earnings_shoes + earnings_shirts

    # L4
    num_people = 2 # each of them
    earnings_per_person = total_earnings / num_people

    # FA
    answer = earnings_per_person
    return answer