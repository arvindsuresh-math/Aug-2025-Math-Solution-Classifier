def solve():
    """Index: 3870.
    Returns: the number of more joggers Christopher bought than Alexander.
    """
    # L1
    christopher_joggers = 80 # Christopher bought 80 joggers
    christopher_multiplier = 20 # twenty times as many joggers as Tyson
    tyson_joggers = christopher_joggers / christopher_multiplier

    # L2
    alexander_more_than_tyson = 22 # Alexander Bought 22 more joggers than Tyson
    alexander_joggers = tyson_joggers + alexander_more_than_tyson

    # L3
    christopher_more_than_alexander = christopher_joggers - alexander_joggers

    # FA
    answer = christopher_more_than_alexander
    return answer