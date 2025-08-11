def solve():
    """Index: 715.
    Returns: the total profit from selling 25 charm bracelets.
    """
    # L1
    string_cost = 1 # $1 on the string for each bracelet
    bead_cost = 3 # $3 on beads for each bracelet
    cost_per_bracelet = string_cost + bead_cost

    # L2
    bracelets_sold = 25 # sell 25 bracelets
    total_cost = bracelets_sold * cost_per_bracelet

    # L3
    sale_price = 6 # sell the bracelets for $6 each
    total_revenue = bracelets_sold * sale_price

    # L4
    total_profit = total_revenue - total_cost

    # FA
    answer = total_profit
    return answer