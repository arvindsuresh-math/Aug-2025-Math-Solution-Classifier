def solve():
    """Index: 1923.
    Returns: the total amount of money Katrina and her friends made.
    """
    # L1
    first_day_friends = 5 # 5 friends sign up that day
    end_week_friends = 7 # another 7 friends by the end of the week
    total_friends = first_day_friends + end_week_friends

    # L2
    friend_reward = 5 # friend would receive $5.00
    total_friends_reward = total_friends * friend_reward

    # L3
    katrina_per_friend_reward = 5 # she would receive another $5.00 per friend
    katrina_friends_reward = total_friends * katrina_per_friend_reward

    # L4
    katrina_initial_reward = 5 # earn $5.00 for signing up
    total_money = katrina_initial_reward + total_friends_reward + katrina_friends_reward

    # FA
    answer = total_money
    return answer