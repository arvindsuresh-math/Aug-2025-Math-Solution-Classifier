def solve_69():
    # Number of starfish collected
    num_starfish = 7
    # Number of arms per starfish
    arms_per_starfish = 5
    # Number of seastar arms
    seastar_arms = 14

    # Calculate the total number of arms from the starfish
    total_starfish_arms = num_starfish * arms_per_starfish

    # Calculate the total number of arms from all animals
    total_arms = total_starfish_arms + seastar_arms

    return total_arms