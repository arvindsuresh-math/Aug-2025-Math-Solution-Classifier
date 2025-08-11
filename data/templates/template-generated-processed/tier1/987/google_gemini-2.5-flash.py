def solve():
    """Index: 987.
    Returns: the amount of money Linda had at the beginning.
    """
    # L1
    lucy_original_money = 20 # Lucy originally had $20
    amount_given = 5 # Lucy would give Linda $5
    lucy_money_after_giving = lucy_original_money - amount_given

    # L2
    # After Lucy gives money, Lucy and Linda have the same amount.
    # So, Linda's money after receiving is equal to Lucy's money after giving.
    linda_money_after_receiving = lucy_money_after_giving
    linda_original_money = linda_money_after_receiving - amount_given

    # FA
    answer = linda_original_money
    return answer