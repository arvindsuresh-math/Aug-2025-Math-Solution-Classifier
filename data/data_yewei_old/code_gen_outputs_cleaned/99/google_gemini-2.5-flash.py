def solve_99():
    # Given information
    first_tank_gallons = 48
    fish_size_first_tank = 3  # inches
    fish_size_second_tank = 2  # inches
    gallons_per_inch_of_fish = 1 # rule: 1 gallon of water per inch of fish

    # L1: Calculate the size of the second tank.
    # The first tank is twice the size of the second tank, so the second tank is half the size of the first.
    second_tank_gallons = first_tank_gallons / 2

    # L2: Calculate the number of fish in the second tank.
    # Each 2-inch fish needs 2 * 1 = 2 gallons of water.
    gallons_per_fish_second_tank = fish_size_second_tank * gallons_per_inch_of_fish
    num_fish_second_tank = second_tank_gallons / gallons_per_fish_second_tank

    # L3: Calculate the number of fish initially in the first tank.
    # Each 3-inch fish needs 3 * 1 = 3 gallons of water.
    gallons_per_fish_first_tank = fish_size_first_tank * gallons_per_inch_of_fish
    initial_num_fish_first_tank = first_tank_gallons / gallons_per_fish_first_tank

    # L4: Calculate the number of fish in the first tank after one eats another.
    num_fish_first_tank_after_event = initial_num_fish_first_tank - 1

    # L5: Calculate how many more fish are in the first tank than the second tank.
    difference_in_fish = num_fish_first_tank_after_event - num_fish_second_tank

    return int(difference_in_fish)