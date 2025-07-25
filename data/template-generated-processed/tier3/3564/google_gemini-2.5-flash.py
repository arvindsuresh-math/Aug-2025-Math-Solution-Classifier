def solve():
    """Index: 3564.
    Returns: the percentage of the total cost that is ham and bread.
    """
    # L1
    cost_bread = 50 # a loaf of bread for $50
    cost_ham = 150 # 2oz of ham for $150
    total_cost_bread_ham = cost_bread + cost_ham

    # L2
    cost_cake = 200 # a cake for $200
    total_cost_all_items = total_cost_bread_ham + cost_cake

    # L3
    total_percentage = 100 # total percentage for all the items is 100%
    percent_ham_bread = total_cost_bread_ham / total_cost_all_items * total_percentage

    # FA
    answer = percent_ham_bread
    return answer