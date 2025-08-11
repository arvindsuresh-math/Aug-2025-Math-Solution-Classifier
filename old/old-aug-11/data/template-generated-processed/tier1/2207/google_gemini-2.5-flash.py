def solve():
    """Index: 2207.
    Returns: the total number of calories each player burns during the exercise.
    """
    # L1
    stairs_one_way = 32 # 32 stairs one way
    multiplier_up_down = 2 # up and down
    stairs_per_run = stairs_one_way * multiplier_up_down

    # L2
    num_runs = 40 # 40 times
    total_stairs_climbed = stairs_per_run * num_runs

    # L3
    calories_per_stair = 2 # 2 calories
    total_calories_burned = total_stairs_climbed * calories_per_stair

    # FA
    answer = total_calories_burned
    return answer