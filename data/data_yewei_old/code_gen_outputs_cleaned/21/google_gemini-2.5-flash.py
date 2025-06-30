def solve_21():
    # Given rates
    beetles_per_bird = 12
    birds_per_snake = 3
    snakes_per_jaguar = 5

    # Number of jaguars in the forest
    num_jaguars = 6

    # Step 1: Calculate the total number of snakes eaten by the jaguars
    # Each jaguar eats 5 snakes, and there are 6 jaguars.
    total_snakes_eaten = snakes_per_jaguar * num_jaguars
    # total_snakes_eaten = 5 * 6 = 30

    # Step 2: Calculate the total number of birds eaten by those snakes
    # Each snake eats 3 birds, and there are 30 snakes.
    total_birds_eaten = total_snakes_eaten * birds_per_snake
    # total_birds_eaten = 30 * 3 = 90

    # Step 3: Calculate the total number of beetles eaten by those birds
    # Each bird eats 12 beetles, and there are 90 birds.
    total_beetles_eaten = total_birds_eaten * beetles_per_bird
    # total_beetles_eaten = 90 * 12 = 1080

    return total_beetles_eaten

# Execute the function to get the answer
# print(solve_21())