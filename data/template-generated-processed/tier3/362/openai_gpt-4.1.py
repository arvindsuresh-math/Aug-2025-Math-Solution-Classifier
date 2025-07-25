def solve():
    """Index: 362.
    Returns: how many more pounds Kevin's laptop weighs than Karen's tote.
    """
    # L1
    tote_weight = 8 # Karen’s tote weighs 8 pounds
    full_briefcase_multiplier = 2 # Kevin's full briefcase is twice the weight of Karen's tote
    full_briefcase_weight = full_briefcase_multiplier * tote_weight

    # L2
    empty_briefcase_divisor = 2 # Karen’s work tote bag is twice the weight of her husband Kevin’s briefcase when the briefcase is empty
    empty_briefcase_weight = tote_weight / empty_briefcase_divisor

    # L3
    briefcase_contents_weight = full_briefcase_weight - empty_briefcase_weight

    # L4
    papers_divisor = 6 # work papers are a sixth of the weight of the contents
    papers_weight = briefcase_contents_weight / papers_divisor

    # L5
    laptop_weight = briefcase_contents_weight - papers_weight

    # L6
    laptop_vs_tote_difference = laptop_weight - tote_weight

    # FA
    answer = laptop_vs_tote_difference
    return answer