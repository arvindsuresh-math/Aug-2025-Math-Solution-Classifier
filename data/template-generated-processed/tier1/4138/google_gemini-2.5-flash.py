def solve():
    """Index: 4138.
    Returns: the initial amount of money Agatha had.
    """
    # L1
    frame_cost = 15 # spends $15 on the frame
    front_wheel_cost = 25 # and $25 on the front wheel
    total_spent_initial = frame_cost + front_wheel_cost

    # L2
    money_left = 20 # has $20 left
    total_money_at_first = total_spent_initial + money_left

    # FA
    answer = total_money_at_first
    return answer