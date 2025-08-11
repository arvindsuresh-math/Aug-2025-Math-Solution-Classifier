def solve():
    """Index: 4673.
    Returns: the total amount Leon paid.
    """
    # L1
    cost_per_organizer_set = 78 # $78 per set
    num_organizer_sets = 3 # 3 sets of toy organizers
    cost_organizers = cost_per_organizer_set * num_organizer_sets

    # L2
    cost_per_chair = 83 # $83 each
    num_gaming_chairs = 2 # 2 gaming chairs
    cost_chairs = cost_per_chair * num_gaming_chairs

    # L3
    total_sales = cost_organizers + cost_chairs

    # L4
    delivery_fee_percentage_numerator = 5 # 5% of the total sales
    delivery_fee_percentage_denominator = 100 # 5% of the total sales
    delivery_fee = total_sales * delivery_fee_percentage_numerator / delivery_fee_percentage_denominator

    # L5
    total_paid = total_sales + delivery_fee

    # FA
    answer = total_paid
    return answer