def solve():
    """Index: 607.
    Returns: the number of additional tokens Sandy will have compared to any of her siblings.
    """
    # L1
    total_tokens = 1000000 # 1 million Safe Moon tokens
    keep_fraction_denominator = 2 # half of them
    tokens_for_self = total_tokens / keep_fraction_denominator

    # L2
    num_siblings = 4 # 4 siblings
    tokens_per_sibling = tokens_for_self / num_siblings

    # L3
    difference_in_tokens = tokens_for_self - tokens_per_sibling

    # FA
    answer = difference_in_tokens
    return answer