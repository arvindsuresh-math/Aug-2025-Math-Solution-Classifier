def solve():
    # Total number of people consumed over three hundred years
    total_people_consumed = 847

    # Let 'x' be the number of people on the ship in the first hundred years.
    # The number of people on the ship in the second hundred years is 2 * x.
    # The number of people on the ship in the third hundred years is 2 * (2 * x) = 4 * x.

    # The total number of people consumed is x + 2x + 4x = 7x.
    # So, 7x = total_people_consumed

    # Calculate the sum of the multipliers for each ship
    # First ship: 1x
    # Second ship: 2x
    # Third ship: 4x
    sum_of_multipliers = 1 + 2 + 4

    # Calculate the number of people on the first ship
    people_on_first_ship = total_people_consumed / sum_of_multipliers

    return int(people_on_first_ship)

# Execute the function to get the answer
# print(solve())