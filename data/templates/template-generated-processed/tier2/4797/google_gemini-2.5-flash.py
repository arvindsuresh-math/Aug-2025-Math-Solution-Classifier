def solve():
    """Index: 4797.
    Returns: the total amount of money Zoe took.
    """
    # L1
    family_members = 5 # her 5 family members
    zoe_person = 1 # herself
    total_people = family_members + zoe_person

    # L2
    soda_cost_per_bottle = 0.5 # half a dollar
    total_soda_cost = total_people * soda_cost_per_bottle

    # L3
    pizza_cost_per_slice = 1 # each slice of pizza costs $1
    total_pizza_cost = total_people * pizza_cost_per_slice

    # L4
    total_money_taken = total_soda_cost + total_pizza_cost

    # FA
    answer = total_money_taken
    return answer