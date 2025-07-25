def solve():
    """Index: 2955.
    Returns: the percentage of money Mo will spend on Valentine's cards.
    """
    # L1
    num_students = 30 # 30 students
    percent_students_for_cards = 0.6 # 60% of them
    num_cards_needed = num_students * percent_students_for_cards

    # L2
    cost_per_card = 2 # $2 each
    total_cost_cards = num_cards_needed * cost_per_card

    # L3
    initial_money = 40 # he has $40
    proportion_spent = total_cost_cards / initial_money

    # L4
    percent_multiplier = 100 # WK
    percentage_spent = proportion_spent * percent_multiplier

    # FA
    answer = percentage_spent
    return answer