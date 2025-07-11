def solve():
    """Index: 2914.
    Returns: the number of weeks Leah can feed her birds.
    """
    # L1
    parrot_weekly_consumption = 100 # her parrot eats 100 grams of seeds each week
    cockatiel_weekly_consumption = 50 # her cockatiel eats 50 grams of seeds in a week
    total_weekly_consumption = parrot_weekly_consumption + cockatiel_weekly_consumption

    # L2
    boxes_bought = 3 # Leah bought 3 boxes of birdseed
    boxes_already_had = 5 # she already had 5 boxes in the pantry
    total_boxes = boxes_bought + boxes_already_had

    # L3
    grams_per_box = 225 # If each box of birdseed contains 225 grams
    total_grams_of_seed = total_boxes * grams_per_box

    # L4
    weeks_of_feed = total_grams_of_seed / total_weekly_consumption

    # FA
    answer = weeks_of_feed
    return answer