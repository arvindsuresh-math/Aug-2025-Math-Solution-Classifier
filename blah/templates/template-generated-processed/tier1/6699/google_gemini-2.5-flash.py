def solve():
    """Index: 6699.
    Returns: the total cost of the entire gardening project.
    """
    # L1
    rose_bush_cost = 150 # Each rose bush costs $150
    num_rose_bushes = 20 # all 20 of his rose bushes
    roses_cost = rose_bush_cost * num_rose_bushes

    # L2
    gardener_days = 4 # 4 days
    gardener_hours_per_day = 5 # 5 hours each day
    gardener_total_hours = gardener_days * gardener_hours_per_day

    # L3
    gardener_hourly_rate = 30 # $30 an hour
    gardener_cost = gardener_hourly_rate * gardener_total_hours

    # L4
    soil_cost_per_cubic_foot = 5 # $5 per cubic foot
    soil_cubic_feet = 100 # 100 cubic feet of soil
    soil_cost = soil_cost_per_cubic_foot * soil_cubic_feet

    # L5
    total_cost = roses_cost + gardener_cost + soil_cost

    # FA
    answer = total_cost
    return answer