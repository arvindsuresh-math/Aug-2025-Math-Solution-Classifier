def solve():
    """Index: 6959.
    Returns: how many more dolls Andrena has than Debelyn.
    """
    # L1
    debelyn_initial_dolls = 20 # Debelyn had 20 dolls
    debelyn_gave_andrena = 2 # gave Andrena 2 dolls
    debelyn_remaining_dolls = debelyn_initial_dolls - debelyn_gave_andrena

    # L3
    christel_initial_dolls = 24 # Christel had 24 dolls
    christel_gave_andrena = 5 # giving Andrena 5 dolls
    christel_remaining_dolls = christel_initial_dolls - christel_gave_andrena

    # L4
    andrena_more_than_christel = 2 # Andrena now has 2 more dolls than Christel
    andrena_total_dolls = christel_remaining_dolls + andrena_more_than_christel

    # L5
    andrena_more_than_debelyn = andrena_total_dolls - debelyn_remaining_dolls

    # FA
    answer = andrena_more_than_debelyn
    return answer