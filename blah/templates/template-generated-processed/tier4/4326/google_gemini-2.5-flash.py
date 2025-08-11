def solve():
    """Index: 4326.
    Returns: the total amount saved for their mother's birthday gift.
    """
    # L1
    liam_oranges_picked = 40 # Liam picked 40 oranges
    liam_oranges_per_set = 2 # sold them at $2.50 for 2
    liam_sets_sold = liam_oranges_picked / liam_oranges_per_set

    # L2
    cost_per_set = 2.50 # $2.50 for 2
    liam_earned = cost_per_set * liam_sets_sold

    # L3
    claire_cost_per_orange = 1.20 # $1.20 each
    claire_oranges_picked = 30 # Claire picked 30 oranges
    claire_earned = claire_cost_per_orange * claire_oranges_picked

    # L4
    total_saved = liam_earned + claire_earned

    # FA
    answer = total_saved
    return answer