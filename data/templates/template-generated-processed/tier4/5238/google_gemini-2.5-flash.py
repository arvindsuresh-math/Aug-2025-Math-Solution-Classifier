def solve():
    """Index: 5238.
    Returns: the total money received from recycling.
    """
    # L1
    total_cans = 144 # 144 cans
    cans_per_set = 12 # every 12 cans
    num_can_sets = total_cans / cans_per_set

    # L2
    money_per_can_set = 0.50 # $0.50
    money_from_cans = money_per_can_set * num_can_sets

    # L3
    total_newspapers_kg = 20 # 20 kilograms of newspapers
    kg_per_newspaper_set = 5 # every 5 kilograms of newspapers
    num_newspaper_sets = total_newspapers_kg / kg_per_newspaper_set

    # L4
    money_per_newspaper_set = 1.50 # $1.50
    money_from_newspapers = money_per_newspaper_set * num_newspaper_sets

    # L5
    total_money_received = money_from_cans + money_from_newspapers

    # FA
    answer = total_money_received
    return answer