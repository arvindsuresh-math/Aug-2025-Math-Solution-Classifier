def solve():
    """Index: 4446.
    Returns: the total deposit Hans has to pay for the restaurant reservation.
    """
    # L1
    total_people = 12 # twelve people
    num_children = 2 # Two of the people in Hans’s party are his kid cousins
    num_adults = total_people - num_children

    # L2
    cost_per_adult = 3 # $3 per adult
    cost_adults = cost_per_adult * num_adults

    # L3
    cost_per_child = 1 # $1 per child
    cost_children = num_children * cost_per_child

    # L4
    flat_deposit = 20 # flat $20
    total_deposit = cost_adults + cost_children + flat_deposit

    # FA
    answer = total_deposit
    return answer