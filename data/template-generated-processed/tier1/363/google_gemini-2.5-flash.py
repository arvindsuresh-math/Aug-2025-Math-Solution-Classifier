def solve():
    """Index: 363.
    Returns: the cost of a bunch of bananas.
    """
    # L1
    tony_paid = 7 # Tony paid $7
    arnold_paid = 5 # Arnold paid $5
    tony_paid_more = tony_paid - arnold_paid

    # L3
    # The difference in price Tony paid ($2) corresponds to the cost of the extra dozen apples he bought.
    cost_per_dozen_apples = tony_paid_more

    # L4
    cost_of_bananas = arnold_paid - cost_per_dozen_apples

    # FA
    answer = cost_of_bananas
    return answer