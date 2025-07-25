def solve():
    """Index: 4952.
    Returns: the total number of people who bought tickets.
    """
    # L5
    adult_ticket_cost = 7 # An adult ticket costs $7
    child_ticket_cost = 3 # a child's ticket costs $3
    adults_multiplier_for_children = 3 # Three times as many children as adults
    total_collected_money = 6000 # collected a total of $6,000
    coefficient_of_X = adult_ticket_cost + child_ticket_cost * adults_multiplier_for_children
    num_adults = total_collected_money / coefficient_of_X

    # L6
    num_children = num_adults * adults_multiplier_for_children

    # L7
    total_people = num_adults + num_children

    # FA
    answer = total_people
    return answer