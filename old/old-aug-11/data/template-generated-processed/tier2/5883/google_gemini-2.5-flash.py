def solve():
    """Index: 5883.
    Returns: the number of pennies Iain will have left.
    """
    # L1
    total_pennies = 200 # 200 pennies
    older_pennies = 30 # 30 of his pennies are older than he is
    remaining_pennies_after_older = total_pennies - older_pennies

    # L2
    throw_out_percent = 0.20 # throw out 20% of his remaining pennies
    pennies_to_throw_out = remaining_pennies_after_older * throw_out_percent

    # L3
    final_pennies_left = remaining_pennies_after_older - pennies_to_throw_out

    # FA
    answer = final_pennies_left
    return answer