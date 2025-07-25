def solve():
    """Index: 4910.
    Returns: the amount of money the school can save.
    """
    # L1
    total_devices = 50 # cover 50 devices
    devices_per_package_40 = 5 # covers up to 5 devices
    num_packages_40 = total_devices / devices_per_package_40

    # L2
    cost_per_package_40 = 40 # $40
    total_cost_40 = cost_per_package_40 * num_packages_40

    # L3
    devices_per_package_60 = 10 # covers up to 10 devices
    num_packages_60 = total_devices / devices_per_package_60

    # L4
    cost_per_package_60 = 60 # $60
    total_cost_60 = cost_per_package_60 * num_packages_60

    # L5
    subtraction_value_in_solution = 100 # WK
    savings = total_cost_40 - subtraction_value_in_solution

    # FA
    answer = savings
    return answer