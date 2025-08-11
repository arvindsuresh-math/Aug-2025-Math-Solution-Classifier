def solve():
    """Index: 6631.
    Returns: the government's profit from this project.
    """
    # L1
    total_people = 1000 # 1000 people in it
    bottom_percent_decimal = 0.2 # bottom 20% of people
    num_people_receiving_stimulus = total_people * bottom_percent_decimal

    # L2
    stimulus_amount_per_person = 2000 # a $2000 stimulus
    total_cost = num_people_receiving_stimulus * stimulus_amount_per_person

    # L3
    return_multiplier = 5 # returns 5 times as much money
    total_revenue = return_multiplier * total_cost

    # L4
    government_profit = total_revenue - total_cost

    # FA
    answer = government_profit
    return answer