def solve_62():
    # Given total oil and total number of cans
    total_oil_liters = 290
    total_cans = 24

    # Information about the first set of cans
    num_specific_cans = 10
    capacity_specific_can_liters = 8

    # L1: Calculate the total oil in the specific cans
    oil_in_specific_cans = num_specific_cans * capacity_specific_can_liters

    # L2: Calculate the remaining oil
    remaining_oil_liters = total_oil_liters - oil_in_specific_cans

    # L3: Calculate the number of remaining cans
    remaining_cans = total_cans - num_specific_cans

    # L4: Calculate how much oil each of the remaining cans is holding
    oil_per_remaining_can = remaining_oil_liters / remaining_cans

    return oil_per_remaining_can

# The final answer is the result of the function call
# print(solve_62())