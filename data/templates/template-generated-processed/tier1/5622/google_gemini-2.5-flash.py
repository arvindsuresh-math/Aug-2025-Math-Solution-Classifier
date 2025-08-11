def solve():
    """Index: 5622.
    Returns: the remaining weight Michael needs to lose to meet his goal.
    """
    # L1
    lost_march = 3 # lost 3 pounds in March
    lost_april = 4 # lost 4 pounds in April
    total_lost_march_april = lost_march + lost_april

    # L2
    goal_weight_loss = 10 # lose 10 pounds by June
    remaining_weight_to_lose = goal_weight_loss - total_lost_march_april

    # FA
    answer = remaining_weight_to_lose
    return answer