def solve():
    """Index: 7143.
    Returns: the number of tokens Angus has.
    """
    # L1
    worth_less_dollars = 20 # $20 worth of tokens less
    token_value = 4 # each token is worth $4
    worth_less_tokens = worth_less_dollars / token_value

    # L2
    elsa_tokens = 60 # Elsa has 60 tokens
    angus_tokens = elsa_tokens - worth_less_tokens

    # FA
    answer = angus_tokens
    return answer