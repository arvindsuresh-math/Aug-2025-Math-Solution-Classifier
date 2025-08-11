def solve():
    """Index: 715.
    Returns: the total profit made from selling charm bracelets.
    """
    # L1
    string_cost_per_bracelet = 1 # $1 on the string for each bracelet
    beads_cost_per_bracelet = 3 # $3 on beads for each bracelet
    cost_per_bracelet = string_cost_per_bracelet + beads_cost_per_bracelet

    # L2
    num_bracelets_sold = 25 # sell 25 bracelets
    total_cost = num_bracelets_sold * cost_per_bracelet

    # L3
    selling_price_per_bracelet = 6 # sell the bracelets for $6 each
    total_revenue = num_bracelets_sold * selling_price_per_bracelet

    # L4
    total_profit = total_revenue - total_cost

    # FA
    answer = total_profit
    return answer