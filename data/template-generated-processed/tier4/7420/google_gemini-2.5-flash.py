def solve():
    """Index: 7420.
    Returns: the number of jobs Nikola completed.
    """
    # L1
    num_ants = 400 # 400 ants in his farm
    ounces_per_ant = 2 # Each ant needs 2 ounces of food
    total_ounces_food = num_ants * ounces_per_ant

    # L2
    cost_per_ounce = 0.1 # Every ounce of ant food costs $.1
    total_food_cost = total_ounces_food * cost_per_ounce

    # L3
    num_leaves_raked = 6000 # raked 6,000 leaves
    cost_per_leaf = 0.01 # Each leaf he rakes costs 1 penny
    earnings_from_leaves = num_leaves_raked * cost_per_leaf

    # L4
    earnings_from_jobs_only = total_food_cost - earnings_from_leaves

    # L5
    job_start_fee = 5 # charges $5 to start a job
    num_jobs_completed = earnings_from_jobs_only / job_start_fee

    # FA
    answer = num_jobs_completed
    return answer