def solve(
    rent_apt1: int = 800, # Rent for apt 1
    utilities_apt1: int = 260, # Utilities for apt 1
    miles_apt1: int = 31, # Miles driven per day for apt 1
    rent_apt2: int = 900, # Rent for apt 2
    utilities_apt2: int = 200, # Utilities for apt 2
    miles_apt2: int = 21, # Miles driven per day for apt 2
    cost_per_mile: float = 0.58, # Cost per mile in dollars
    work_days_per_month: int = 20 # Work days per month
):
    """Code for Q 1202 from the GSM8K dataset (train).
    Returns the difference in total costs between the two apartments."""
    
    # The mileage cost for the first apartment will be 31*20*0.58 = $<<31*20*0.58=359.60>>359.60
    mileage_cost_apt1 = miles_apt1 * cost_per_mile * work_days_per_month

    # This makes the total monthly cost of the first apartment 359.60 + 800 + 260 = $<<359.60+800+260=1419.60>>1419.60
    total_cost_apt1 = rent_apt1 + utilities_apt1 + mileage_cost_apt1

    # Similarly, the mileage cost for the second apartment will be 21*20*0.58 = $<<21*20*0.58=243.60>>243.60
    mileage_cost_apt2 = miles_apt2 * cost_per_mile * work_days_per_month

    # Thus, the total monthly cost of the second apartment is 243.60 + 900 + 200 = <<243.60+900+200=1343.60>>1343.60
    total_cost_apt2 = rent_apt2 + utilities_apt2 + mileage_cost_apt2

    # Therefore, the difference in total monthly costs is 1419.60 - 1343.60 = $<<1419.60-1343.60=76>>76
    cost_difference = total_cost_apt1 - total_cost_apt2

    # The final answer is the cost difference
    return cost_difference