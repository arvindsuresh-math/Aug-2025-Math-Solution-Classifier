def solve():
    """Index: 3939.
    Returns: the total amount all the ladies spent on dresses.
    """
    # L1
    pauline_dress_cost = 30 # Pauline's dress was $30
    jean_less_than_pauline = 10 # Jean's dress was $10 less than Pauline's dress
    jean_dress_cost = pauline_dress_cost - jean_less_than_pauline

    # L2
    ida_more_than_jean = 30 # Ida's dress was $30 more than Jean's dress
    ida_dress_cost = ida_more_than_jean + jean_dress_cost

    # L3
    patty_more_than_ida = 10 # Patty's dress was $10 more than Ida's dress
    patty_dress_cost = ida_dress_cost + patty_more_than_ida

    # L4
    total_spent = patty_dress_cost + ida_dress_cost + jean_dress_cost + pauline_dress_cost

    # FA
    answer = total_spent
    return answer