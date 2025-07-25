def solve():
    """Index: 1002.
    Returns: the sum of all their money.
    """
    # L1
    patricia_money = 60 # Patricia has $60
    patricia_jethro_multiplier = 3 # 3 times as much as Jethro
    jethro_money = patricia_money / patricia_jethro_multiplier

    # L2
    carmen_target_multiplier = 2 # twice the amount of money that Jethro has
    twice_jethro_money = jethro_money * carmen_target_multiplier

    # L3
    carmen_needs_more = 7 # $7 more
    carmen_money = twice_jethro_money - carmen_needs_more

    # L4
    total_money = patricia_money + jethro_money + carmen_money

    # FA
    answer = total_money
    return answer