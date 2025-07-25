def solve():
    """Index: 5069.
    Returns: the total cost Jake pays for sausages.
    """
    # L1
    package_weight = 2 # 2-pound packages
    num_packages = 3 # buys 3 of them
    total_pounds = package_weight * num_packages

    # L2
    price_per_pound = 4 # $4 a pound
    total_cost = total_pounds * price_per_pound

    # FA
    answer = total_cost
    return answer