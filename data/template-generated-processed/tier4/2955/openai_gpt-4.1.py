def solve():
    """Index: 2955.
    Returns: the percentage of Mo's money spent on Valentine cards.
    """
    # L1
    num_students = 30 # 30 students
    percent_to_give = 0.6 # give a Valentine to 60% of them
    num_cards = num_students * percent_to_give

    # L2
    card_cost = 2 # $2 each
    total_spent = num_cards * card_cost

    # L3
    total_money = 40 # he has $40
    proportion_spent = total_spent / total_money

    # L4
    percent_factor = 100 # WK
    percent_spent = proportion_spent * percent_factor

    # FA
    answer = percent_spent
    return answer