def solve():
    """Index: 1380.
    Returns: the number of social media followers the girl with the most total followers had.
    """
    # L1
    susy_initial_followers = 100 # Susy had 100 social media followers
    susy_gained_week1 = 40 # She gained 40 new followers in the first week
    susy_followers_week1 = susy_initial_followers + susy_gained_week1

    # L2
    half_divisor = 2 # half that in the second week
    susy_gained_week2 = susy_gained_week1 / half_divisor

    # L3
    susy_gained_week3 = susy_gained_week2 / half_divisor

    # L4
    susy_total_followers = susy_followers_week1 + susy_gained_week2 + susy_gained_week3

    # L5
    sarah_initial_followers = 50 # Sarah only had 50 social media followers
    sarah_gained_week1 = 90 # she gained 90 new followers the first week
    sarah_followers_week1 = sarah_initial_followers + sarah_gained_week1

    # L6
    third_divisor = 3 # a third of that in the second week
    sarah_gained_week2 = sarah_gained_week1 / third_divisor

    # L7
    sarah_gained_week3 = sarah_gained_week2 / third_divisor

    # L8
    sarah_total_followers = sarah_followers_week1 + sarah_gained_week2 + sarah_gained_week3

    # L9
    # FA
    answer = max(susy_total_followers, sarah_total_followers)
    return answer