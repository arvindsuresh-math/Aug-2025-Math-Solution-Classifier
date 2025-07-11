def solve():
    """Index: 900.
    Returns: the total number of nuts in Mason's car.
    """
    # L1
    num_busy_squirrels = 2 # 2 busy squirrels
    nuts_per_day_per_busy_squirrel = 30 # stockpiling 30 nuts/day
    nuts_busy_squirrels_per_day = num_busy_squirrels * nuts_per_day_per_busy_squirrel

    # L2
    nuts_per_day_sleepy_squirrel = 20 # one sleepy squirrel has been stockpiling 20 nuts/day
    total_nuts_per_day = nuts_busy_squirrels_per_day + nuts_per_day_sleepy_squirrel

    # L3
    num_days = 40 # for 40 days
    total_nuts = total_nuts_per_day * num_days

    # FA
    answer = total_nuts
    return answer