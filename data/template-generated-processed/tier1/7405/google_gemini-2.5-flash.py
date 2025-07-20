def solve():
    """Index: 7405.
    Returns: the amount of money Agatha has left to spend.
    """
    # L1
    frame_cost = 15 # $15 on the frame
    front_wheel_cost = 25 # $25 on the front wheel
    total_spent = frame_cost + front_wheel_cost

    # L2
    initial_money = 60 # $60 to spend
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer