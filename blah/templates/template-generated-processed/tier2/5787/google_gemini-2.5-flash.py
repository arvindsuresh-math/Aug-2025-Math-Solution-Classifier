def solve():
    """Index: 5787.
    Returns: the total cost to buy apples for the family.
    """
    # L1
    original_price_per_pound = 1.6 # $1.6 per pound
    price_increase_percent = 0.25 # raised 25%
    price_increase_amount = original_price_per_pound * price_increase_percent

    # L2
    new_price_per_pound = original_price_per_pound + price_increase_amount

    # L3
    pounds_per_person = 2 # 2 pounds of apples for each person
    num_family_members = 4 # 4 member family
    total_pounds_bought = pounds_per_person * num_family_members

    # L4
    total_cost = total_pounds_bought * new_price_per_pound

    # FA
    answer = total_cost
    return answer