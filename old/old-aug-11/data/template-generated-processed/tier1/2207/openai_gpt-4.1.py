def solve():
    """Index: 2207.
    Returns: the total calories each player burns during the exercise.
    """
    # L1
    stairs_one_way = 32 # 32 stairs one way
    up_and_down = 2 # up and down
    stairs_per_run = stairs_one_way * up_and_down

    # L2
    num_runs = 40 # run up and down the bleachers 40 times
    total_stairs = stairs_per_run * num_runs

    # L3
    calories_per_stair = 2 # each stair burns 2 calories
    total_calories = total_stairs * calories_per_stair

    # FA
    answer = total_calories
    return answer