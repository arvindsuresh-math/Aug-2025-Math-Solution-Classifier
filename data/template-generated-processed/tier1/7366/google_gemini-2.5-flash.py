def solve():
    """Index: 7366.
    Returns: the total number of packages to be delivered tomorrow.
    """
    # L1
    packages_yesterday = 80 # 80 packages yesterday
    multiplier_today = 2 # twice as many today
    packages_today = packages_yesterday * multiplier_today

    # L2
    total_packages = packages_yesterday + packages_today

    # FA
    answer = total_packages
    return answer