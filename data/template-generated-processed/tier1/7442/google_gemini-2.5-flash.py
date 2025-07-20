def solve():
    """Index: 7442.
    Returns: the amount of money Sally needs to pay out of pocket.
    """
    # L1
    num_students = 30 # 30 students in her class
    cost_per_book = 12 # A reading book costs $12
    total_cost_needed = num_students * cost_per_book

    # L2
    money_given = 320 # $320 to spend on books
    out_of_pocket_payment = total_cost_needed - money_given

    # FA
    answer = out_of_pocket_payment
    return answer