def solve():
    """Index: 5202.
    Returns: the total money needed by the students.
    """
    # L1
    bags_per_student = 2 # 2 bags of chips
    num_students = 5 # 5 students
    total_bags_of_chips = bags_per_student * num_students

    # L2
    cost_per_chip_bag = 0.5 # chips for $.50 each
    total_chips_cost = total_bags_of_chips * cost_per_chip_bag

    # L3
    cost_per_candy_bar = 2 # candy bars for $2 each
    total_candy_bars_cost = num_students * cost_per_candy_bar

    # L4
    total_money_needed = total_candy_bars_cost + total_chips_cost

    # FA
    answer = total_money_needed
    return answer