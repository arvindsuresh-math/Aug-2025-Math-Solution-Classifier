def solve():
    """Index: 930.
    Returns: the total number of apples bought by two men and three women.
    """
    # L1
    num_men = 2 # two men
    apples_per_man = 30 # each bought 30 apples
    apples_men = num_men * apples_per_man

    # L2
    less_than_woman = 20 # 20 less than the number of apples bought by each woman
    apples_per_woman = less_than_woman + apples_per_man

    # L3
    num_women = 3 # three women
    apples_women = num_women * apples_per_woman

    # L4
    total_apples = apples_men + apples_women

    # FA
    answer = total_apples
    return answer