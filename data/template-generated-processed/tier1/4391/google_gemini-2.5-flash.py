def solve():
    """Index: 4391.
    Returns: the number of quarters Libby will have left.
    """
    # L1
    cost_of_dress_dollars = 35 # $35 to replace her sister’s dress
    quarters_per_dollar = 4 # WK
    cost_of_dress_quarters = cost_of_dress_dollars * quarters_per_dollar

    # L2
    initial_quarters = 160 # 160 quarters in her piggy bank
    remaining_quarters = initial_quarters - cost_of_dress_quarters

    # FA
    answer = remaining_quarters
    return answer