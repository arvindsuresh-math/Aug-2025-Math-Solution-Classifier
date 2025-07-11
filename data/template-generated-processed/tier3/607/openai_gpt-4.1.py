def solve():
    """Index: 607.
    Returns: the number of tokens Sandy will have more than any of her siblings.
    """
    # L1
    total_tokens = 1000000 # Sandy bought 1 million Safe Moon tokens
    keep_fraction_denominator = 2 # keep half of them to herself
    sandy_tokens = total_tokens / keep_fraction_denominator

    # L2
    siblings = 4 # She has 4 siblings
    sibling_tokens = sandy_tokens / siblings

    # L3
    tokens_more_than_sibling = sandy_tokens - sibling_tokens

    # FA
    answer = tokens_more_than_sibling
    return answer