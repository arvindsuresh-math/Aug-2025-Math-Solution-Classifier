def solve():
    """Index: 1250.
    Returns: the total cost of Lucia’s dance classes in one week.
    """
    # L1
    hip_hop_classes_per_week = 2 # 2 hip-hop classes a week
    cost_hip_hop_class = 10 # One hip-hop class costs $10
    total_cost_hip_hop = hip_hop_classes_per_week * cost_hip_hop_class

    # L2
    ballet_classes_per_week = 2 # 2 ballet classes a week
    cost_ballet_class = 12 # One ballet class costs $12
    total_cost_ballet = ballet_classes_per_week * cost_ballet_class

    # L3
    jazz_classes_per_week = 1 # 1 jazz class a week
    cost_jazz_class = 8 # one jazz class costs $8
    total_cost_jazz = jazz_classes_per_week * cost_jazz_class

    # L4
    total_weekly_cost = total_cost_hip_hop + total_cost_ballet + total_cost_jazz

    # FA
    answer = total_weekly_cost
    return answer