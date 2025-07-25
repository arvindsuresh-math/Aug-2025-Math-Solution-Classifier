def solve():
    """Index: 362.
    Returns: the difference in weight between Kevin's laptop and Karen's tote.
    """
    # L1
    full_briefcase_multiplier = 2 # it is twice the weight of Karen’s tote
    karen_tote_weight = 8 # Karen’s tote weighs 8 pounds
    full_briefcase_weight = full_briefcase_multiplier * karen_tote_weight

    # L2
    empty_briefcase_divisor = 2 # twice the weight of her husband Kevin’s briefcase when the briefcase is empty
    empty_briefcase_weight = karen_tote_weight / empty_briefcase_divisor

    # L3
    contents_weight = full_briefcase_weight - empty_briefcase_weight

    # L4
    papers_divisor = 6 # a sixth of the weight of the contents
    work_papers_weight = contents_weight / papers_divisor

    # L5
    laptop_weight = contents_weight - work_papers_weight

    # L6
    weight_difference = laptop_weight - karen_tote_weight

    # FA
    answer = weight_difference
    return answer