def solve():
    """Index: 415.
    Returns: the dog's full adult weight in pounds.
    """
    # L1
    initial_weight_7_weeks = 6 # At 7 weeks old, the puppy weighed 6 pounds
    doubling_factor = 2 # doubled in weight
    weight_at_week_9 = initial_weight_7_weeks * doubling_factor

    # L2
    weight_at_3_months = weight_at_week_9 * doubling_factor

    # L3
    weight_at_5_months = weight_at_3_months * doubling_factor

    # L4
    added_weight_final = 30 # adding another 30 pounds
    final_adult_weight = weight_at_5_months + added_weight_final

    # FA
    answer = final_adult_weight
    return answer