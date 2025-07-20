def solve():
    """Index: 4270.
    Returns: the combined weight of Barney and the five regular dinosaurs.
    """
    # L1
    num_regular_dinosaurs = 5 # five regular dinosaurs
    weight_each_regular_dinosaur = 800 # each regular dinosaur weighs 800 pounds
    combined_weight_five_regular_dinosaurs = num_regular_dinosaurs * weight_each_regular_dinosaur

    # L2
    barney_extra_weight = 1500 # weighs 1500 pounds more
    barney_weight = combined_weight_five_regular_dinosaurs + barney_extra_weight

    # L3
    total_combined_weight = barney_weight + combined_weight_five_regular_dinosaurs

    # FA
    answer = total_combined_weight
    return answer