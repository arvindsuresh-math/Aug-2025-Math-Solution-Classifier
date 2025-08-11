def solve():
    """Index: 1072.
    Returns: the total number of buttons GooGoo will use to manufacture all shirts for the order.
    """
    # L1
    num_first_type = 200 # 200 of the first type of shirt
    buttons_first_type = 3 # 3 buttons (first type)
    buttons_needed_first = num_first_type * buttons_first_type

    # L2
    num_second_type = 200 # 200 of the second type of shirt
    buttons_second_type = 5 # 5 buttons (second type)
    buttons_needed_second = num_second_type * buttons_second_type

    # L3
    total_buttons = buttons_needed_first + buttons_needed_second

    # FA
    answer = total_buttons
    return answer