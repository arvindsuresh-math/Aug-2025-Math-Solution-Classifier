def solve():
    """Index: 6434.
    Returns: the amount of change Clive will have.
    """
    # L1
    olives_needed = 80 # needs 80 olives
    olives_per_jar = 20 # A jar of 20 olives
    jars_needed = olives_needed / olives_per_jar

    # L2
    cost_per_jar = 1.50 # costs $1.50
    total_cost = jars_needed * cost_per_jar

    # L3
    initial_money = 10 # He has $10 to spend
    change = initial_money - total_cost

    # FA
    answer = change
    return answer