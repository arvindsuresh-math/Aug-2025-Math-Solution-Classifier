def solve():
    """Index: 6026.
    Returns: the number of burritos John has left.
    """
    # L1
    boxes_given_away_numerator = 3 # a 3rd of them
    boxes_given_away_denominator = 3 # a 3rd of them
    boxes_given_away = boxes_given_away_numerator / boxes_given_away_denominator

    # L2
    initial_boxes = 3 # 3 boxes of burritos
    remaining_boxes = initial_boxes - boxes_given_away

    # L3
    burritos_per_box = 20 # Each box has 20 burritos
    total_burritos_after_giving_away = remaining_boxes * burritos_per_box

    # L4
    burritos_per_day = 3 # He eats 3 burritos per day
    number_of_days = 10 # for 10 days
    burritos_eaten = burritos_per_day * number_of_days

    # L5
    burritos_left = total_burritos_after_giving_away - burritos_eaten

    # FA
    answer = burritos_left
    return answer