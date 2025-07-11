def solve():
    """Index: 2152.
    Returns: the number of jellybeans each nephew or niece received.
    """
    # L1
    nephews = 3 # 3 nephews
    nieces = 2 # 2 nieces
    total_children = nephews + nieces

    # L2
    total_jellybeans = 70 # 70 jellybeans
    jellybeans_per_child = total_jellybeans / total_children

    # FA
    answer = jellybeans_per_child
    return answer