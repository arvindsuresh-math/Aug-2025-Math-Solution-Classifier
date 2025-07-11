def solve():
    """Index: 900.
    Returns: the total number of nuts in Mason's car after 40 days.
    """
    # L1
    num_busy_squirrels = 2 # 2 busy squirrels
    busy_squirrel_rate = 30 # 30 nuts/day
    busy_total_per_day = num_busy_squirrels * busy_squirrel_rate

    # L2
    sleepy_squirrel_rate = 20 # one sleepy squirrel has been stockpiling 20 nuts/day
    total_nuts_per_day = busy_total_per_day + sleepy_squirrel_rate

    # L3
    num_days = 40 # all for 40 days
    total_nuts = total_nuts_per_day * num_days

    # FA
    answer = total_nuts
    return answer