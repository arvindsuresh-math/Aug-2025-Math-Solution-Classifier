def solve():
    """Index: 3618.
    Returns: the total money Maurice would make.
    """
    # L1
    total_tasks = 30 # finishing 30 tasks
    tasks_for_bonus = 10 # every 10 tasks finished
    bonus_frequency = total_tasks / tasks_for_bonus

    # L2
    bonus_amount = 6 # $6 bonus
    total_bonus_money = bonus_frequency * bonus_amount

    # L3
    money_per_task = 2 # $2 for every finished task
    money_from_tasks = total_tasks * money_per_task

    # L4
    total_money = money_from_tasks + total_bonus_money

    # FA
    answer = total_money
    return answer