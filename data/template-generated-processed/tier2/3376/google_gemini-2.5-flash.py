def solve():
    """Index: 3376.
    Returns: John's new total lift.
    """
    # L1
    initial_squat_lift = 700 # lift 700 for squat
    squat_loss_percent = 0.3 # lost 30% of his lift
    squat_loss_amount = initial_squat_lift * squat_loss_percent

    # L2
    new_squat_lift = initial_squat_lift - squat_loss_amount

    # L3
    initial_deadlift = 800 # 800 for deadlift
    deadlift_loss_amount = 200 # lost 200 pounds on deadlift
    new_deadlift = initial_deadlift - deadlift_loss_amount

    # L4
    initial_bench_lift = 400 # 400 for bench
    total_new_lift = new_squat_lift + new_deadlift + initial_bench_lift

    # FA
    answer = total_new_lift
    return answer