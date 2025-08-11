def solve():
    """Index: 6515.
    Returns: the total amount of money they all paid together.
    """
    # L1
    cost_per_night_per_person = 40 # $40 per night per person
    num_nights = 3 # stayed for three nights
    cost_per_person = cost_per_night_per_person * num_nights

    # L2
    num_people = 3 # Jenny and two of her friends
    total_cost = cost_per_person + cost_per_person + cost_per_person

    # FA
    answer = total_cost
    return answer