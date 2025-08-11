def solve():
    """Index: 3056.
    Returns: the current weight of the cat's bowl.
    """
    # L1
    grams_per_day = 60 # 60 grams per day
    fill_duration_days = 3 # every 3 days
    grams_added_to_bowl = grams_per_day * fill_duration_days

    # L2
    empty_bowl_weight = 420 # empty bowl weighs 420 grams
    total_weight_filled = empty_bowl_weight + grams_added_to_bowl

    # L3
    grams_eaten = 14 # she only ate 14 grams
    current_bowl_weight = total_weight_filled - grams_eaten

    # FA
    answer = current_bowl_weight
    return answer