def solve():
    """Index: 5658.
    Returns: the number of marbles each friend had at the end of the day.
    """
    # L1
    dilan_marbles = 14 # Dilan had 14 marbles
    martha_marbles = 20 # Martha had 20 marbles
    phillip_marbles = 19 # Phillip had 19 marbles
    veronica_marbles = 7 # Veronica had only 7 marbles
    total_marbles = dilan_marbles + martha_marbles + phillip_marbles + veronica_marbles

    # L2
    num_friends = 4 # Dilan, Martha, Phillip, and Veronica
    marbles_per_friend = total_marbles / num_friends

    # FA
    answer = marbles_per_friend
    return answer