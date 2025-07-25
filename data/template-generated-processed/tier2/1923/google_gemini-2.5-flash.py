def solve():
    """Index: 1923.
    Returns: the total money Katrina and her friends made.
    """
    # L1
    initial_friends_signed_up = 5 # had 5 friends sign up
    additional_friends_signed_up = 7 # another 7 friends
    total_friends_signed_up = initial_friends_signed_up + additional_friends_signed_up

    # L2
    friend_reward_per_person = 5 # the friend would receive $5.00
    total_friends_reward = total_friends_signed_up * friend_reward_per_person

    # L3
    katrina_reward_per_friend = 5 # she would receive another $5.00 per friend
    total_katrina_referral_reward = total_friends_signed_up * katrina_reward_per_friend

    # L4
    katrina_initial_reward = 5 # she could earn $5.00
    total_money_made = katrina_initial_reward + total_friends_reward + total_katrina_referral_reward

    # FA
    answer = total_money_made
    return answer