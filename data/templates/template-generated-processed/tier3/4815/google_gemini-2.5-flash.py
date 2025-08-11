def solve():
    """Index: 4815.
    Returns: the total amount of money Zayne made from selling bracelets.
    """
    # L1
    revenue_from_5_dollar_bracelets = 60 # made $60 from selling bracelets for $5 each
    price_per_bracelet = 5 # bracelets for $5 each
    num_bracelets_at_5_dollars = revenue_from_5_dollar_bracelets / price_per_bracelet

    # L2
    total_initial_bracelets = 30 # started with 30 bracelets
    num_bracelets_sold_in_pairs = total_initial_bracelets - num_bracelets_at_5_dollars

    # L3
    bracelets_per_pair = 2 # two for $8
    num_pairs_sold = num_bracelets_sold_in_pairs / bracelets_per_pair

    # L4
    price_per_pair = 8 # two for $8
    revenue_from_pairs = price_per_pair * num_pairs_sold

    # L5
    total_earnings = revenue_from_pairs + revenue_from_5_dollar_bracelets

    # FA
    answer = total_earnings
    return answer