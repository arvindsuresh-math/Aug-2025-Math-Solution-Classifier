def solve():
    """Index: 4917.
    Returns: the total cost Lizzy will pay for the shipment.
    """
    # L1
    total_pounds_fish = 540 # 540 pounds of fish
    pounds_per_crate = 30 # 30-pound crates
    num_crates = total_pounds_fish / pounds_per_crate

    # L2
    cost_per_crate = 1.5 # shipping cost of each crate is $1.5
    total_shipping_cost = cost_per_crate * num_crates

    # FA
    answer = total_shipping_cost
    return answer