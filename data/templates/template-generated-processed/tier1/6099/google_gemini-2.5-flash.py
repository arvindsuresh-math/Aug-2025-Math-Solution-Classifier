def solve():
    """Index: 6099.
    Returns: the total number of dolls they have altogether.
    """
    # L1
    grandmother_dolls = 50 # If their grandmother has 50 dolls
    sister_more_than_grandmother = 2 # two more dolls than their grandmother
    sister_dolls = grandmother_dolls + sister_more_than_grandmother

    # L2
    sister_and_grandmother_total = sister_dolls + grandmother_dolls

    # L3
    rene_multiplier = 3 # three times as many dolls as her sister
    rene_dolls = sister_dolls * rene_multiplier

    # L4
    total_dolls = rene_dolls + sister_and_grandmother_total

    # FA
    answer = total_dolls
    return answer