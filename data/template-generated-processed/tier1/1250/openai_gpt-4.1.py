def solve():
    """Index: 1250.
    Returns: the total cost of Lucia’s dance classes in one week.
    """
    # L1
    hiphop_classes_per_week = 2 # 2 hip-hop classes a week
    hiphop_class_cost = 10 # One hip-hop class costs $10
    hiphop_total = hiphop_classes_per_week * hiphop_class_cost

    # L2
    ballet_classes_per_week = 2 # 2 ballet classes a week
    ballet_class_cost = 12 # One ballet class costs $12
    ballet_total = ballet_classes_per_week * ballet_class_cost

    # L3
    jazz_classes_per_week = 1 # 1 jazz class a week
    jazz_class_cost = 8 # one jazz class costs $8
    jazz_total = jazz_classes_per_week * jazz_class_cost

    # L4
    total_cost = hiphop_total + ballet_total + jazz_total

    # FA
    answer = total_cost
    return answer