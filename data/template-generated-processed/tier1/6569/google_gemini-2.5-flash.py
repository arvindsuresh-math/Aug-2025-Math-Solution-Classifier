def solve():
    """Index: 6569.
    Returns: the total cost of their trip.
    """
    # L1
    price_per_person = 147 # $147 per person
    discount_per_person = 14 # discount of $14
    price_after_discount = price_per_person - discount_per_person

    # L2
    num_people = 2 # two of them
    total_cost = price_after_discount * num_people

    # FA
    answer = total_cost
    return answer