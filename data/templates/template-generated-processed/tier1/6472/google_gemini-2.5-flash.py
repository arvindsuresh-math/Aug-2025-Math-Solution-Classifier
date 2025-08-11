def solve():
    """Index: 6472.
    Returns: the number of shirts and pants that are neither plaid nor purple.
    """
    # L1
    total_shirts = 5 # 5 shirts
    plaid_shirts = 3 # 3 of Teairra's shirts are plaid
    non_plaid_shirts = total_shirts - plaid_shirts

    # L2
    total_pants = 24 # 24 pairs of pants
    purple_pants = 5 # 5 of Teairra's pants are purple
    non_purple_pants = total_pants - purple_pants

    # L3
    total_non_plaid_non_purple = non_purple_pants + non_plaid_shirts

    # FA
    answer = total_non_plaid_non_purple
    return answer