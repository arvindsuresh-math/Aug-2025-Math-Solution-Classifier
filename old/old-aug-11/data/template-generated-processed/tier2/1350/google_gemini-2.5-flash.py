def solve():
    """Index: 1350.
    Returns: the total money John makes from selling butterflies.
    """
    # L1
    num_jars = 4 # 4 jars
    caterpillars_per_jar = 10 # 10 caterpillars each
    total_caterpillars = num_jars * caterpillars_per_jar

    # L2
    failure_rate_decimal = 0.4 # 40% of them fail
    failed_caterpillars = total_caterpillars * failure_rate_decimal

    # L3
    successful_butterflies = total_caterpillars - failed_caterpillars

    # L4
    price_per_butterfly = 3 # sells the butterflies for $3 each
    total_money_made = successful_butterflies * price_per_butterfly

    # FA
    answer = total_money_made
    return answer