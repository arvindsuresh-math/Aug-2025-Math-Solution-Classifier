def solve():
    """Index: 1289.
    Returns: the combined cost of Gary's and Anna's gold.
    """
    # L1
    gary_grams = 30 # 30 grams of gold
    gary_cost_per_gram = 15 # $15 per gram
    gary_total_cost = gary_grams * gary_cost_per_gram

    # L2
    anna_grams = 50 # 50 grams of gold
    anna_cost_per_gram = 20 # $20 per gram
    anna_total_cost = anna_grams * anna_cost_per_gram

    # L3
    combined_cost = gary_total_cost + anna_total_cost

    # FA
    answer = combined_cost
    return answer