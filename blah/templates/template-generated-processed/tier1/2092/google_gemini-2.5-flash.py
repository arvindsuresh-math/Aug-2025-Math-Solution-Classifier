def solve():
    """Index: 2092.
    Returns: the total number of classes Eduardo and Frankie taught.
    """
    # L1
    eduardo_classes = 3 # taught 3 classes last week
    double_multiplier = 2 # taught double what Eduardo teaches
    frankie_classes = eduardo_classes * double_multiplier

    # L2
    total_classes = eduardo_classes + frankie_classes

    # FA
    answer = total_classes
    return answer