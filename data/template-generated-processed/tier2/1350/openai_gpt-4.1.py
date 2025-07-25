def solve():
    """Index: 1350.
    Returns: the total money John makes from selling butterflies.
    """
    # L1
    num_jars = 4 # 4 jars
    caterpillars_per_jar = 10 # 10 caterpillars each
    total_caterpillars = num_jars * caterpillars_per_jar

    # L2
    fail_percent = 0.4 # 40% of them fail
    num_failed = total_caterpillars * fail_percent

    # L3
    num_butterflies = total_caterpillars - num_failed

    # L4
    price_per_butterfly = 3 # $3 each
    total_money = num_butterflies * price_per_butterfly

    # FA
    answer = total_money
    return answer