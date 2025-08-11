def solve():
    """Index: 5639.
    Returns: the number of years it will take Zach to accomplish his goal.
    """
    # L1
    cost_per_stadium = 900 # $900 per stadium
    num_stadiums = 30 # 30 major league baseball stadiums
    total_cost = cost_per_stadium * num_stadiums

    # L2
    savings_per_year = 1500 # save $1,500 per year
    years_to_accomplish_goal = total_cost / savings_per_year

    # FA
    answer = years_to_accomplish_goal
    return answer