def solve():
    """Index: 7400.
    Returns: the total amount earned from selling the entire collection.
    """
    # L1
    earned_amount = 28 # for $28
    numerator_of_fraction_sold = 4 # 4/7 of her stamp collection
    value_of_one_seventh = earned_amount / numerator_of_fraction_sold

    # L2
    denominator_of_fraction_sold = 7 # 4/7 of her stamp collection
    total_collection_value = value_of_one_seventh * denominator_of_fraction_sold

    # FA
    answer = total_collection_value
    return answer