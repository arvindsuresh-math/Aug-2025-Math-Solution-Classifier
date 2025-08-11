def solve():
    """Index: 3126.
    Returns: the number of bags of corn seeds each kid used.
    """
    # L1
    num_kids = 4 # 4 kids
    dinner_cost_per_kid = 36 # $36 per kid
    total_dinner_cost = num_kids * dinner_cost_per_kid

    # L2
    money_spent_fraction_denominator = 2 # half their money
    total_money_earned = total_dinner_cost * money_spent_fraction_denominator

    # L3
    pay_per_row = 1.5 # $1.5 per row
    total_rows_planted = total_money_earned / pay_per_row

    # L4
    ears_per_row = 70 # 70 ears
    total_ears_planted = total_rows_planted * ears_per_row

    # L5
    ears_per_kid = total_ears_planted / num_kids

    # L6
    seeds_per_ear = 2 # 2 seeds per ear of corn
    seeds_per_kid = ears_per_kid * seeds_per_ear

    # L7
    seeds_per_bag = 48 # 48 seeds
    bags_per_kid = seeds_per_kid / seeds_per_bag

    # FA
    answer = bags_per_kid
    return answer