def solve():
    """Index: 6908.
    Returns: the ratio of his lifting total to bodyweight.
    """
    # L1
    initial_total_pounds = 2200 # powerlifting total of 2200 pounds
    total_gain_percent = 0.15 # gain 15% on his total
    total_added_pounds = initial_total_pounds * total_gain_percent

    # L2
    new_total_pounds = initial_total_pounds + total_added_pounds

    # L3
    initial_bodyweight_pounds = 245 # bodyweight of 245 pounds
    bodyweight_gain_pounds = 8 # 8 pounds of body weight
    new_bodyweight_pounds = initial_bodyweight_pounds + bodyweight_gain_pounds

    # L4
    lifting_to_bodyweight_ratio = new_total_pounds / new_bodyweight_pounds

    # FA
    answer = lifting_to_bodyweight_ratio
    return answer